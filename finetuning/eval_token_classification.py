#!/usr/bin/env python3
"""
Evaluation script for finetuned NER/POS classification models.
"""

import sys
import hydra
from omegaconf import DictConfig
from hydra import compose, initialize
from pathlib import Path
from typing import Optional, cast
import torch
from omegaconf import OmegaConf as om
from sequence_classification import update_batch_size_info, load_model
import numpy as np
import json
from tabulate import tabulate
from datetime import datetime
from finetuning.dataloaders.build_dataloader import build_my_dataloader
import seqeval.metrics as seqeval_mt

torch.set_float32_matmul_precision('high')

def get_tag_mappings(cfg):
    # For wiki_ner: cfg.tag2id, for xtreme_ner: cfg.tag_names
    if cfg.dataset_name == "wiki_ann_ner":
        id2tag = {
            0: "O",
            1: "B-PER",
            2: "I-PER",
            3: "B-ORG",
            4: "I-ORG",
            5: "B-LOC",
            6: "I-LOC"
        }
        return id2tag
    elif hasattr(cfg, 'tag2id'):
        id2tag = {i: tag for tag, i in cfg.tag2id.items()}
        return id2tag
    elif hasattr(cfg, 'tag_names'):
        id2tag = {i: tag for i, tag in enumerate(cfg.tag_names)}
        return id2tag
    elif hasattr(cfg, 'train_loader'):
        return get_tag_mappings(cfg.train_loader)
    elif hasattr(cfg, 'eval_loader'):
        return get_tag_mappings(cfg.eval_loader)
    else:
        raise ValueError(f"No tag2id or tag_names found in config for NER task. Config is : {cfg}")

def evaluate(cfg: DictConfig, checkpoint_path: str, is_finetuned: bool, hyper_param_tuning: bool = False, eval_dataloader = None):
    cfg = update_batch_size_info(cfg)
    print("Initializing model...")
    model = load_model(cfg)

    print(f"Will the finetuned version be evaluated? {is_finetuned}")
    if is_finetuned:
        print("Loading finetuned weights!!")
        original_state = {name: param.clone() for name, param in model.named_parameters()}
        print(f"Loading checkpoint from {checkpoint_path}")
        checkpoint = torch.load(checkpoint_path, weights_only=False)
        if 'state' in checkpoint:
            state_dict = checkpoint['state']['model']
        else:
            state_dict = checkpoint
        missing_keys, unexpected_keys = model.load_state_dict(state_dict, strict=False)
        if missing_keys:
            print(f"Warning: Missing keys: {missing_keys[:5]}...")
        if unexpected_keys:
            print(f"Warning: Unexpected keys: {unexpected_keys[:5]}...")
        weights_changed = any(
            not torch.equal(original_state[name], param)
            for name, param in model.named_parameters()
            if name in original_state
        )
        print("✓ Model weights successfully updated" if weights_changed else "⚠ Warning: Model weights appear unchanged")

    model.eval()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)

    print("Creating test dataloader...")
    if hyper_param_tuning:
        test_loader = eval_dataloader
    else:
        test_loader = build_my_dataloader(cfg.eval_loader, cfg.dataset_name, cfg.device_eval_microbatch_size, 'test')

    id2tag = get_tag_mappings(cfg)

    all_predictions = []
    all_labels = []
    total_samples = 0

    print("Running evaluation...")
    with torch.no_grad():
        for batch in test_loader:
            # Move batch to device
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model.model(input_ids=batch['input_ids'], attention_mask=batch['attention_mask'])
            predictions = torch.argmax(outputs.logits, dim=-1)
            labels = batch['labels']
            word_ids_batch = batch['word_ids']
            for i in range(predictions.shape[0]):
                pred_ids = predictions[i].cpu().numpy()
                label_ids = labels[i].cpu().numpy()
                word_ids = word_ids_batch[i].cpu().numpy() if torch.is_tensor(word_ids_batch[i]) else word_ids_batch[i]
                pred_tags = []
                true_tags = []
                previous_word_idx = None
                for idx, word_idx in enumerate(word_ids):
                    if word_idx == -1 or word_idx == previous_word_idx or label_ids[idx] == -100:
                        continue
                    pred_tag = id2tag[pred_ids[idx]]
                    true_tag = id2tag[label_ids[idx]]
                    pred_tags.append(pred_tag)
                    true_tags.append(true_tag)
                    previous_word_idx = word_idx
                all_predictions.append(pred_tags)
                all_labels.append(true_tags)
                total_samples += 1
    
    print("\n=== Word-level Evaluation Results ===")
    report = seqeval_mt.classification_report(all_labels, all_predictions, output_dict=True)
    print(seqeval_mt.classification_report(all_labels, all_predictions, digits=5))
    
    acc = seqeval_mt.accuracy_score(all_labels, all_predictions)
    f1 = seqeval_mt.f1_score(all_labels, all_predictions)
    
    print(f"Word-level F1: {f1:.5f}")
    print(f"Word-level Accuracy: {acc:.5f}")
    
    results = {
        "test_samples": int(total_samples),
        "accuracy": acc,
        "macro_f1": f1,
        "classification_report": report,
        "model_name": cfg.model_path,
        "checkpoint_path": checkpoint_path,
        "task_type": cfg.task_type,
        "evaluation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    output_dir = Path("evaluation_results")
    output_dir.mkdir(exist_ok=True)
    model_name = cfg.hf_model_name.replace("/", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"eval_results_{model_name}_{timestamp}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(to_python_type(results), f, indent=2)
    print(f"\nResults saved to: {output_file}")

    # Print results in table format
    table_data = [
        ["Test samples", "F1 score"] + list(report.keys()),
        [f"{total_samples}", f"{f1:.4f}"] + [f"{report[tag]['f1-score']:.4f}" if isinstance(report[tag], dict) and 'f1-score' in report[tag] else "-" for tag in report.keys()]
    ]
    print("\nEvaluation Results:")
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))

    return report

def to_python_type(obj):
    """Recursively convert numpy/tensor types in a dict/list to native Python types."""
    if isinstance(obj, dict):
        return {k: to_python_type(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [to_python_type(v) for v in obj]
    elif isinstance(obj, (np.integer, np.int32, np.int64)):
        return int(obj)
    elif isinstance(obj, (np.floating, np.float32, np.float64)):
        return float(obj)
    elif isinstance(obj, torch.Tensor):
        return obj.item() if obj.numel() == 1 else obj.tolist()
    else:
        return obj

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python eval_token_classification.py <model_config_name> <task_config_name> <checkpoint_path> <finetuned_boolean>")
        sys.exit(1)

    model_config_name, task_config_name, checkpoint_path, is_finetuned = sys.argv[1], sys.argv[2], sys.argv[3], bool(int(sys.argv[4]))

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
    
    evaluate(cfg, checkpoint_path, is_finetuned) 