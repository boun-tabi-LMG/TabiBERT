# Copyright 2022 MosaicML Examples authors
# SPDX-License-Identifier: Apache-2.0
"""A starter script for fine-tuning a BERT model on your own dataset."""

import os
import sys
import operator
from typing import Optional, cast
import hydra
from hydra import compose, initialize
import torch
import gc

# Add folder root to path to allow us to use relative imports regardless of what directory the script is run from
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from transformers import AutoModelForSequenceClassification, AutoModelForTokenClassification, AutoModelForQuestionAnswering, AutoModelForMaskedLM
from composer import Trainer, algorithms, Evaluator
from composer.callbacks import LRMonitor, MemoryMonitor, OptimizerMonitor, RuntimeEstimator, SpeedMonitor, EarlyStopper
from composer.loggers import WandBLogger
from composer.optim import DecoupledAdamW
from composer.optim.scheduler import (
    ConstantWithWarmupScheduler,
    CosineAnnealingWithWarmupScheduler,
    LinearWithWarmupScheduler,
)
from transformers import default_data_collator, AutoTokenizer
from torch.utils.data import DataLoader, Subset
from scheduler import WarmupStableDecayScheduler
from composer.utils import dist, reproducibility
from omegaconf import DictConfig
from omegaconf import OmegaConf as om
from composer.models import HuggingFaceModel
from composer.metrics import LossMetric
from sklearn.metrics import f1_score
import numpy as np
from regression import RegressionHuggingFaceModel
from finetuning.dataloaders.build_dataloader import build_my_dataloader

class HuggingFaceModelWithTrainLoss(HuggingFaceModel):
    """Wraps HuggingFaceModel to expose a train/eval 'loss' metric for callbacks like EarlyStopper."""

    def get_metrics(self, is_train: bool = False):
        metrics = super().get_metrics(is_train)
        # Ensure a standard 'loss' metric exists for both train and eval
        def _loss_fn(outputs, batch):
            return self.loss(outputs, batch)
        metrics["loss"] = LossMetric(loss_function=_loss_fn)
        return metrics

class MLMMaskOnlyLossModel(HuggingFaceModel):
    """HuggingFaceModel wrapper that trains an MLM head but computes loss only at [MASK]."""
    def __init__(self, model):
        super().__init__(model)

    def forward(self, batch):
        return self.model(
            input_ids=batch['input_ids'],
            attention_mask=batch.get('attention_mask'),
            labels=batch.get('labels')
        )

    def loss(self, outputs, batch):
        # HF MLM with provided labels already computes token-level CE and averages over non -100 labels
        # Since labels are -100 everywhere except [MASK], this is already the desired loss
        if isinstance(outputs, dict) and 'loss' in outputs:
            return outputs['loss']
        return outputs.loss

    def get_metrics(self, is_train: bool = False):
        metrics = super().get_metrics(is_train)
        # Ensure a standard 'loss' metric exists for both train and eval
        def _loss_fn(outputs, batch):
            return self.loss(outputs, batch)
        metrics["loss"] = LossMetric(loss_function=_loss_fn)
        return metrics

def update_batch_size_info(cfg: DictConfig):
    global_batch_size, device_microbatch_size = cfg.global_train_batch_size, cfg.device_train_microbatch_size
    if global_batch_size % dist.get_world_size() != 0:
        raise ValueError(
            f"Global batch size {global_batch_size} is not divisible by {dist.get_world_size()} "
            "as a result, the batch size would be truncated, please adjust `global_batch_size` "
            f"to be divisible by world size, {dist.get_world_size()}.")
    device_train_batch_size = global_batch_size // dist.get_world_size()
    if isinstance(device_microbatch_size, int):
        if device_microbatch_size > device_train_batch_size:
            print(
                f"WARNING: device_train_microbatch_size > device_train_batch_size, "
                f"will be reduced from {device_microbatch_size} -> {device_train_batch_size}."
            )
            device_microbatch_size = device_train_batch_size
    cfg.n_gpus = dist.get_world_size()
    cfg.device_train_batch_size = device_train_batch_size
    cfg.device_train_microbatch_size = device_microbatch_size

    # Safely set `device_eval_microbatch_size` if not provided by user
    if "device_eval_microbatch_size" not in cfg:
        if cfg.device_train_microbatch_size == "auto":
            cfg.device_eval_microbatch_size = 1
        else:
            cfg.device_eval_microbatch_size = cfg.device_train_microbatch_size

    global_eval_batch_size, device_eval_microbatch_size = (
        cfg.get("global_eval_batch_size", global_batch_size),
        cfg.device_eval_microbatch_size,
    )
    device_eval_batch_size = global_eval_batch_size // dist.get_world_size()
    if isinstance(device_eval_microbatch_size, int):
        if device_eval_microbatch_size > device_eval_microbatch_size:
            print(
                f"WARNING: device_eval_microbatch_size > device_eval_batch_size, "
                f"will be reduced from {device_eval_microbatch_size} -> {device_eval_batch_size}."
            )
            device_eval_microbatch_size = device_eval_batch_size
    cfg.device_eval_batch_size = device_eval_batch_size
    cfg.device_eval_microbatch_size = device_eval_microbatch_size
    return cfg


def log_config(cfg: DictConfig):
    print(om.to_yaml(cfg))
    if "wandb" in cfg.get("loggers", {}):
        try:
            import wandb
        except ImportError as e:
            raise e
        if wandb.run:
            wandb.config.update(om.to_container(cfg, resolve=True))


def build_algorithm(name, kwargs):
    if name == "gradient_clipping":
        return algorithms.GradientClipping(**kwargs)
    elif name == "alibi":
        return algorithms.Alibi(**kwargs)
    elif name == "gated_linear_units":
        return algorithms.GatedLinearUnits(**kwargs)
    else:
        raise ValueError(f"Not sure how to build algorithm: {name}")


def build_callback(name, kwargs):
    if name == "lr_monitor":
        return LRMonitor()
    elif name == "memory_monitor":
        return MemoryMonitor()
    elif name == "speed_monitor":
        return SpeedMonitor(window_size=kwargs.get("window_size", 1),
                            gpu_flops_available=kwargs.get(
                                "gpu_flops_available", None))
    elif name == "runtime_estimator":
        return RuntimeEstimator()
    elif name == "optimizer_monitor":
        return OptimizerMonitor(log_optimizer_metrics=kwargs.get(
            "log_optimizer_metrics", True), )
    elif name == "early_stopper":
        # Default to minimizing loss; if monitoring a metric, flip comparison
        monitor_name = kwargs.get("monitor", "loss")
        default_comp = operator.lt if "loss" in str(monitor_name).lower() else operator.gt
        comp = kwargs.get("comp", default_comp)
        # Handle string comparison operators
        if isinstance(comp, str):
            if comp in ["gt", "greater"]:
                comp = operator.gt
            elif comp in ["lt", "less"]:
                comp = operator.lt
            else:
                raise ValueError(f"Unrecognized comp string: {comp}. Use 'gt', 'greater', 'lt', or 'less'")

        return EarlyStopper(
            monitor=monitor_name,
            dataloader_label=kwargs.get("dataloader_label", "train"),
            patience=kwargs.get("patience", "2ep"),
            min_delta=kwargs.get("min_delta", 0.0),
            comp=kwargs.get("comp", default_comp),
        )
    else:
        raise ValueError(f"Not sure how to build callback: {name}")


def build_logger(name, kwargs):
    if name == "wandb":
        return WandBLogger(**kwargs)
    else:
        raise ValueError(f"Not sure how to build logger: {name}")


def build_scheduler(cfg):
    if cfg.name == "constant_with_warmup":
        return ConstantWithWarmupScheduler(t_warmup=cfg.t_warmup)
    elif cfg.name == "cosine_with_warmup":
        return CosineAnnealingWithWarmupScheduler(t_warmup=cfg.t_warmup,
                                                  alpha_f=cfg.alpha_f)
    elif cfg.name == "linear_decay_with_warmup":
        return LinearWithWarmupScheduler(t_warmup=cfg.t_warmup,
                                         alpha_f=cfg.alpha_f)
    elif cfg.name == "warmup_stable_decay":
        return WarmupStableDecayScheduler(t_warmup=cfg.t_warmup,
                                          alpha_f=cfg.alpha_f)
    else:
        raise ValueError(f"Not sure how to build scheduler: {cfg.name}")


def build_optimizer(cfg, model):
    if cfg.name == "decoupled_adamw":
        return DecoupledAdamW(model.parameters(),
                              lr=cfg.lr,
                              betas=cfg.betas,
                              eps=cfg.eps,
                              weight_decay=cfg.weight_decay)
    else:
        raise ValueError(f"Not sure how to build optimizer: {cfg.name}")


def load_model(cfg: DictConfig):
    """Load model directly from Hugging Face Hub."""
    print(f"Loading model from Hugging Face Hub: {cfg.hf_model_name}")
    model_name = cfg.model_path
    trust_remote_code = True

    # NER support: use token classification head
    if cfg.task_type in ["ner", "pos"]:
        hf_model = AutoModelForTokenClassification.from_pretrained(
            model_name,
            num_labels=cfg.model.num_labels,
            trust_remote_code=trust_remote_code,
        )
        model = HuggingFaceModelWithTrainLoss(hf_model)
    # Regression support
    elif cfg.task_type == "regression":
        hf_model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            num_labels=cfg.model.num_labels,
            trust_remote_code=trust_remote_code,
        )
        model = RegressionHuggingFaceModel(hf_model)
    # QA:
    elif cfg.task_type == "qa":
        hf_model = AutoModelForQuestionAnswering.from_pretrained(
            model_name,
            trust_remote_code=trust_remote_code,
        )
        model = HuggingFaceModelWithTrainLoss(hf_model)
    # NLI and other classification tasks
    elif cfg.task_type in ["nli", "classification", "sentiment", "text_classification"]:
        hf_model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            num_labels=cfg.model.num_labels,
            trust_remote_code=trust_remote_code,
        )
        model = HuggingFaceModelWithTrainLoss(hf_model)
    # Default fallback to classification
    else:
        print(f"Warning: Unknown task_type '{cfg.task_type}', defaulting to classification")
        hf_model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            num_labels=cfg.model.num_labels,
            trust_remote_code=trust_remote_code,
        )
        model = HuggingFaceModelWithTrainLoss(hf_model)

    return model


def build_train_and_eval_loader(cfg: DictConfig):
    # Dataloaders
    print("Building train loader...")
    train_loader = build_my_dataloader(
        cfg.train_loader,
        cfg.dataset_name,
        cfg.global_train_batch_size // dist.get_world_size(),
        cfg.train_loader.split,
    )
    # For NER, ensure num_labels is set from tag2id
    if cfg.task_type == "ner" and hasattr(cfg, "tag2id"):
        cfg.model.num_labels = len(cfg.tag2id)
    elif cfg.task_type == "ner" and hasattr(cfg.train_loader, "tag2id"):
        cfg.model.num_labels = len(cfg.train_loader.tag2id)
        cfg.tag2id = cfg.train_loader.tag2id
    print("Building eval loader...")
    global_eval_batch_size = cfg.get("global_eval_batch_size",
                                     cfg.global_train_batch_size)
    eval_loader = build_my_dataloader(
        cfg.eval_loader,
        cfg.dataset_name,
        cfg.get("device_eval_batch_size",
                global_eval_batch_size // dist.get_world_size()),
        cfg.eval_loader.split,
    )
    eval_evaluator = Evaluator(
        label="eval",
        dataloader=eval_loader,
        device_eval_microbatch_size=cfg.get("device_eval_microbatch_size",
                                            None),
    )

    return train_loader, eval_loader, eval_evaluator


def train(cfg: DictConfig,
          do_train: bool = True,
          return_trained_model: bool = False,
          hyper_param_tuning: bool = False) -> Optional[Trainer]:
    print("Training using config: ")
    print(om.to_yaml(cfg))
    reproducibility.seed_all(cfg.seed)

    # Get batch size info
    cfg = update_batch_size_info(cfg)

    # Build Model
    print("Initializing model...")
    model = load_model(cfg)

    n_params = sum(p.numel() for p in model.parameters())
    print(f"{n_params=:.4e}")

    train_loader, eval_loader, eval_evaluator = build_train_and_eval_loader(cfg)

    # Optimizer
    optimizer = build_optimizer(cfg.optimizer, model)

    # Scheduler
    scheduler = build_scheduler(cfg.scheduler)

    # Loggers
    loggers = [
        build_logger(name, logger_cfg)
        for name, logger_cfg in cfg.get("loggers", {}).items()
    ]

    # Callbacks
    callbacks = [
        build_callback(name, callback_cfg)
        for name, callback_cfg in cfg.get("callbacks", {}).items()
    ]

    # Algorithms
    algorithms = [
        build_algorithm(name, algorithm_cfg)
        for name, algorithm_cfg in cfg.get("algorithms", {}).items()
    ]

    if cfg.get("run_name") is None:
        cfg.run_name = os.environ.get("COMPOSER_RUN_NAME",
                                      "sequence-classification")
    trainer = Trainer(
        run_name=cfg.run_name,
        seed=cfg.seed,
        model=model,
        algorithms=algorithms,
        train_dataloader=train_loader,
        eval_dataloader=eval_evaluator,
        train_subset_num_batches=cfg.get("train_subset_num_batches", -1),
        eval_subset_num_batches=cfg.get("eval_subset_num_batches", -1),
        optimizers=optimizer,
        schedulers=scheduler,
        max_duration=cfg.max_duration,
        eval_interval=cfg.eval_interval,
        progress_bar=cfg.progress_bar,
        log_to_console=cfg.log_to_console,
        console_log_interval=cfg.console_log_interval,
        loggers=loggers,
        callbacks=callbacks,
        precision=cfg.precision,
        device=cfg.get("device"),
        device_train_microbatch_size=cfg.get("device_train_microbatch_size",
                                             "auto"),
        save_folder=cfg.get("save_folder"),
        save_interval=cfg.get("save_interval", "1000ba"),
        save_num_checkpoints_to_keep=cfg.get("save_num_checkpoints_to_keep",
                                             -1),
        save_overwrite=cfg.get("save_overwrite", False),
        load_weights_only=True,
        load_strict_model_weights=False
    )

    print("Logging config...")
    log_config(cfg)

    if do_train:
        print("Starting training...")
        trainer.fit()
    del model
    gc.collect()
    torch.cuda.empty_cache()
    if return_trained_model:
        return trainer.state.model, trainer.state.timestamp
    if hyper_param_tuning:
        return eval_loader


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: composer sequence_classification.py <model_config_name> <task_config_name>")
        sys.exit(1)

    model_config_name, task_config_name = sys.argv[1], sys.argv[2]

    # Initialize Hydra and load task config with defaults
    with initialize(config_path="yamls", version_base=None):
        task_cfg = compose(config_name=task_config_name)
    om.set_struct(task_cfg, False)

    # Load model config:
    with open(model_config_name) as f:
        model_cfg = om.load(f)
    om.set_struct(model_cfg, False)

    cfg = om.merge(task_cfg, model_cfg)
    cfg = cast(DictConfig, cfg)

    train(cfg)
