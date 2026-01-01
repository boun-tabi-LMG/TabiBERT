import os
import sys
import csv
from typing import Optional, cast
import json

# Add folder root to path to allow us to use relative imports regardless of what directory the script is run from
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import itertools
import numpy as np
from datasets import Dataset, load_dataset, concatenate_datasets
from composer import Trainer, algorithms, Evaluator
from transformers import AutoTokenizer
from torch.utils.data import DataLoader
from transformers import default_data_collator
from omegaconf import DictConfig
from omegaconf import OmegaConf as om
from composer.utils import dist
from finetuning.dataloaders.build_dataloader import build_my_dataloader
from hyperparam_tuning import MODELS, TASKS
from hyperparam_qa_eval import evaluate_question_answering
from hyperparam_nli_eval import evaluate_nli
from hyperparam_sts_eval import evaluate_sts_regression
from sequence_classification import train
from utils import setup_logging
from pathlib import Path
from datetime import datetime
import torch
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from eval_text_classification import get_class_names
from seqeval.metrics import classification_report, f1_score
import sklearn.metrics as smt
from tabulate import tabulate
from hyperparam_token_eval import evaluate_token_classification
from hyperparam_retrieval_train import train_retrieval_model

# Set up logging
logger = setup_logging('hyperparameter_tuner.py')

# Define parameter grid
param_grid = {
    'weight_decay': [1e-5, 1e-6],
    'learning_rate': [5e-6, 1e-5, 2e-5, 3e-5],
    'epochs': [10],
    'batch_size': [16, 32]
}

# Generate all combinations
param_combinations = list(
    itertools.product(param_grid['learning_rate'], param_grid['weight_decay'],
                      param_grid['epochs'], param_grid['batch_size']))

# Load default config:
model_config_name = "finetuning/yamls/hyperparam_default.yaml"

with open(model_config_name) as f:
    default_cfg = om.load(f)
om.set_struct(default_cfg, False)
default_cfg = cast(DictConfig, default_cfg)


def evaluate_text_classification(cfg,
                                 checkpoint_path,
                                 dataset_name,
                                 test_dataloader,
                                 is_bert_model: bool = False):
    """Get predictions for a single fold."""
    from sequence_classification import load_model, update_batch_size_info

    # Get batch size info
    cfg = update_batch_size_info(cfg)

    # Build Model
    model = load_model(cfg)

    # Get model state before loading
    original_state = {
        name: param.clone()
        for name, param in model.named_parameters()
    }

    # Load checkpoint
    checkpoint = torch.load(checkpoint_path, weights_only=False)

    # Handle different checkpoint structures
    if 'state' in checkpoint:
        state_dict = checkpoint['state']['model']
    else:
        state_dict = checkpoint

    # Load state dict with strict=False to handle potential mismatches
    missing_keys, unexpected_keys = model.load_state_dict(state_dict,
                                                          strict=False)
    if missing_keys:
        logger.warning(f"Missing keys: {missing_keys[:5]}...")
    if unexpected_keys:
        logger.warning(f"Unexpected keys: {unexpected_keys[:5]}...")

    # Check if weights actually changed
    weights_changed = False
    for name, param in model.named_parameters():
        if name in original_state:
            if not torch.equal(original_state[name], param):
                weights_changed = True
                break

    if weights_changed:
        print("✓ Model weights successfully updated")
    else:
        print("⚠ Warning: Model weights appear unchanged")

    model.eval()

    # Move model to GPU if available
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)

    # Initialize metrics
    all_predictions = []
    all_labels = []
    total_samples = 0
    correct_predictions = 0
    # Run evaluation
    print("Running evaluation...")

    with torch.no_grad():
        for batch in test_dataloader:
            # Move batch to device
            for k, v in batch.items():
                if isinstance(v, torch.Tensor):
                    batch[k] = v.to(device)

            # Filter batch to only include keys that the BERT-based models expect
            if is_bert_model:
                label_str = 'labels'
            else:
                label_str = 'label'
            expected_keys = {'input_ids', 'attention_mask', label_str}
            model_inputs = {
                k: v
                for k, v in batch.items() if k in expected_keys
            }

            # Forward pass
            outputs = model.model(**
                                  model_inputs)  # Access the underlying model
            predictions = torch.argmax(outputs.logits, dim=-1)

            # Store predictions and labels
            all_predictions.extend(predictions.cpu().numpy())
            all_labels.extend(batch['labels'].cpu().numpy())

            # Update metrics
            total_samples += batch['labels'].size(0)
            correct_predictions += (
                predictions == batch['labels']).sum().item()

    # Convert to numpy arrays
    all_predictions = np.array(all_predictions)
    all_labels = np.array(all_labels)

    # Calculate accuracy
    accuracy = correct_predictions / total_samples

    # Calculate confusion matrix and per-class accuracy
    cm = confusion_matrix(all_labels, all_predictions)

    with np.errstate(divide='ignore', invalid='ignore'):
        class_accuracies = np.divide(cm.diagonal(), cm.sum(axis=1))
        class_accuracies = np.nan_to_num(class_accuracies, nan=0.0)

    class_names = get_class_names(dataset_name)

    classification_report_dict = smt.classification_report(
        all_labels,
        all_predictions,
        target_names=class_names,
        output_dict=True,
        zero_division=0)

    # Print results in table format
    table_data = [
        ["Test samples", "Correct predictions", "Accuracy"] + class_names,
        [f"{total_samples}", f"{correct_predictions}", f"{accuracy:.4f}"] +
        [f"{acc:.5f}" for acc in class_accuracies]
    ]

    logger.info("\nEvaluation Results:")
    logger.info(tabulate(table_data, headers="firstrow", tablefmt="grid"))

    # Print detailed classification report
    logger.info("\nDetailed Classification Report:")
    classificationReport = smt.classification_report(all_labels,
                                                     all_predictions,
                                                     target_names=class_names,
                                                     digits=5,
                                                     zero_division=0)

    logger.info(classificationReport)

    return {
        "test_samples": int(total_samples),
        "correct_predictions": int(correct_predictions),
        "accuracy": float(accuracy),
        "per_class_accuracy": {
            class_names[i]: float(acc)
            for i, acc in enumerate(class_accuracies)
        },
        "confusion_matrix": cm.tolist(),
        "classification_report": classification_report_dict,
        "evaluation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def hyperparameter_tuner():
    # Initialize DataFrame to store all results
    results_df = pd.DataFrame(columns=[
        'model_name', 'task_name', 'learning_rate', 'weight_decay', 'epochs',
        'batch_size', 'accuracy', 'correct_predictions', 'macro_avg_f1_score',
        'test_samples', 'weighted_avg_f1_score', 'evaluation_date'
    ])
    
    ner_results_df = pd.DataFrame(columns=[
        'model_name', 'task_name', 'learning_rate', 'weight_decay', 'epochs',
        'batch_size', 'f1_score', 'macro_avg_f1_score', 'test_samples',
        'weighted_avg_f1_score', 'evaluation_date'
    ])
    
    regression_results_df = pd.DataFrame(columns=[
        'model_name', 'task_name', 'learning_rate', 'weight_decay', 'epochs',
        'batch_size', 'mse', 'rmse', 'mae', 'pearson_correlation',
        'spearman_correlation', 'primary_score', 'test_samples', 'evaluation_date'
    ])
    
    qa_results_df = pd.DataFrame(columns=[
        'model_name', 'task_name', 'learning_rate', 'weight_decay', 'epochs',
        'batch_size', 'exact_match', 'f1_score', 'exact_match_raw', 'f1_score_raw',
        'predictions', 'gold_answers', 'individual_exact_matches',
        'individual_f1_scores', 'test_samples', 'evaluation_date'
    ])
    
    retrieval_results_df = pd.DataFrame(columns=[
        'model_name', 'task_name', 'learning_rate', 'weight_decay', 'epochs',
        'actual_epochs', 'batch_size', 'early_stopped', 'ndcg@10', 'map', 'mrr', 'recall@10',
        'test_samples', 'evaluation_date'
    ])
    
    # Save results to JSON and CSV
    output_dir = Path("hyperparameter_results")
    output_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    output_files = {}

    for model_name, model_content in MODELS.items():
        if model_name not in output_files.keys():
            model_name_concat = model_name.replace("/", "_")
            output_files[
                model_name] = output_dir / f"{model_name_concat}_{timestamp}.json"
        output_file = output_files[model_name]
    
        model_path = model_content['model_path']
        max_seq_len_model = model_content['max_position_embeddings']
        tokenizer_name = model_path
        if 'tokenizer_name' in model_content:
            tokenizer_name = model_content['tokenizer_name']
    
        model_config = om.create({
            'hf_model_name': model_name,
            'model_path': model_path,
            'tokenizer_name': tokenizer_name,
        })
    
        if model_name == "YTU/BERT" or model_name == "Sabanci/TurkishBERTweet":
            is_lower = True
        else:
            is_lower = False
    
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        logger.info(f"Model is loaded: {model_name}.")
    
        model_config = cast(DictConfig, model_config)
        om.set_struct(model_config, False)
    
        for task_name, task_content in TASKS.items():
            max_seq_len_task = task_content['max_seq_len']
    
            max_seq_len = min(max_seq_len_model, max_seq_len_task)
            task_type = task_content['task_type']
            task_config = om.create({
                'dataset_name': task_name,
                'task_type': task_type,
                'num_labels': task_content['num_labels'],
                'max_seq_len': max_seq_len,
            })
    
            logger.info(f"     Task is in the process: {task_name}.")
            task_config = cast(DictConfig, task_config)
            om.set_struct(task_config, False)
    
            merged_cfg = om.merge(default_cfg, task_config, model_config)
            merged_cfg = cast(DictConfig, merged_cfg)
    
            # Main grid search loop
            for config_idx, params in enumerate(param_combinations):
                lr, weight_decay, epochs, batch_size = params
                epochs_str = str(epochs) + "ep"
                logger.info(
                    f"          Configuration {config_idx+1}/48: LR={lr}, WD={weight_decay}, Epochs={epochs_str}, Batch size: {batch_size}"
                )
    
                save_folder_str = "./finetuning_checkpoints/${task_type}/${dataset_name}/${hf_model_name}/" + str(
                    lr) + "/" + str(weight_decay) + "/" + str(
                        epochs_str) + "/" + str(batch_size)
                
                save_folder_retrieval = f"./finetuning_checkpoints/{task_type}/{task_name}/{model_name}/" + str(
                    lr) + "/" + str(weight_decay) + "/" + str(
                        epochs_str) + "/" + str(batch_size)
                wandb_name = task_type + "/" + task_name + "/" + model_name + "/" + str(
                    lr) + "/" + str(weight_decay) + "/" + str(
                        epochs_str) + "/" + str(batch_size)
    
                hyperparams_config = om.create({
                    'optimizer': {
                        'name': 'decoupled_adamw',
                        'lr': float(lr),
                        'betas': [0.9, 0.98],
                        'eps': 1e-06,
                        'weight_decay': float(weight_decay),
                    },
                    'max_duration': epochs_str,
                    'save_folder': save_folder_str,
                    'wandb_name': wandb_name,
                    'device_eval_microbatch_size': batch_size,
                    'device_train_microbatch_size': batch_size,
                    'global_train_batch_size': batch_size,
                    'eval_interval': '1ep',
                })
    
                hyperparams_config = cast(DictConfig, hyperparams_config)
                om.set_struct(hyperparams_config, False)
    
                cfg = om.merge(merged_cfg, hyperparams_config)
                cfg = cast(DictConfig, cfg)
    
                logger.info("Training using config: ")
                logger.info(om.to_yaml(cfg))
    
                if task_type == "retrieval":
                    # Train retrieval model using the dedicated function
                    results = train_retrieval_model(
                        model_path=model_path,
                        tokenizer_name=tokenizer_name,
                        is_lower=is_lower,
                        task_name=task_name,
                        task_content=task_content,
                        max_seq_len=max_seq_len,
                        model_name=model_name,
                        hf_model_name=model_name,  # hf_model_name is set to model_name in model_config
                        dataset_name=task_name,  # dataset_name is set to task_name in task_config
                        task_type=task_type,
                        lr=lr,
                        weight_decay=weight_decay,
                        epochs=epochs,
                        batch_size=batch_size,
                        save_folder_str=save_folder_retrieval,
                        wandb_name=wandb_name,
                    )
                    
                    # Add row to DataFrame
                    new_row = pd.DataFrame([results])
                    retrieval_results_df = pd.concat([retrieval_results_df, new_row], ignore_index=True)
                    # Temporarily set option to display all columns
                    with pd.option_context('display.max_columns', None):
                        logger.info(f"Final retrieval results:\n{retrieval_results_df}")
                    
                    # Skip the standard evaluation path for retrieval tasks
                    torch.cuda.empty_cache()
                    continue
                else:
                    model, training_timestamp = train(
                        cfg,
                        return_trained_model=True,
                        hyper_param_tuning=True,
                    )
                    epoch_stopped = getattr(training_timestamp, "epoch",
                                            None) or epochs
    
                    from composer.core.time import TimeUnit
                    epoch_num = int(epoch_stopped.value)  # Extract the numeric value
                    unit = epoch_stopped.unit  # Extract the unit (TimeUnit.EPOCH)
    
                    if unit == TimeUnit.EPOCH:
                        if epoch_num < epochs:
                            epochs = epoch_num - 2
    
                    global_eval_batch_size = cfg.get("global_eval_batch_size",
                                                    cfg.global_train_batch_size)
                    eval_dataloader = build_my_dataloader(
                        cfg.eval_loader, cfg.dataset_name,
                        cfg.get("device_eval_batch_size",
                                global_eval_batch_size // dist.get_world_size()),
                        cfg.eval_loader.split)
    
                    checkpoint_path = cfg['save_folder']
    
                    logger.info(
                        f"Checkpoints are saved in the path: {checkpoint_path}")
    
                    latest_checkpoint = checkpoint_path + "/latest-rank0.pt"
    
                     # Check if checkpoint exists, if not save it explicitly
                    if not os.path.exists(latest_checkpoint):
                        logger.info(f"Checkpoint not found at {latest_checkpoint}, saving model explicitly...")
                        # Ensure directory exists
                        os.makedirs(checkpoint_path, exist_ok=True)
                        # Save model in Composer format
                        checkpoint = {
                            'state': {
                                'model': model.state_dict()
                            }
                        }
                        torch.save(checkpoint, latest_checkpoint)
                        logger.info(f"Model checkpoint saved to: {latest_checkpoint}")
                    else:
                        logger.info(f"Checkpoint already exists at: {latest_checkpoint}")
    
                    logger.info(f"Latest checkpoint is read from: {latest_checkpoint}")
    
                    if task_name in [
                            "wiki_ner", "xtreme_ner", "xtreme_pos", "wiki_ann_ner",
                            "pos_ud_boun", "pos_ud_imst"
                    ]:
                        # Get predictions
                        evaluation_results = evaluate_token_classification(
                            cfg, latest_checkpoint, task_name, task_type,
                            eval_dataloader)
    
                        test_samples = evaluation_results['test_samples']
                        f1_score = evaluation_results['f1_score']
                        macro_avg_f1_score = evaluation_results['macro_avg_f1_score']
                        weighted_avg_f1_score = evaluation_results[
                            'weighted_avg_f1_score']
                        evaluation_date = evaluation_results['evaluation_date']
    
                        # Add row to DataFrame
                        new_row = pd.DataFrame([{
                            'model_name': model_name,
                            'task_name': task_name,
                            'learning_rate': lr,
                            'weight_decay': weight_decay,
                            'epochs': epochs,
                            'batch_size': batch_size,
                            'f1_score': f1_score,
                            'macro_avg_f1_score': macro_avg_f1_score,
                            'weighted_avg_f1_score': weighted_avg_f1_score,
                            'test_samples': test_samples,
                            'evaluation_date': evaluation_date,
                        }])
    
                        ner_results_df = pd.concat([ner_results_df, new_row],
                                                ignore_index=True)
                        # Temporarily set option to display all columns
                        with pd.option_context('display.max_columns', None):
                            logger.info(f"Final results:\n{ner_results_df}")
    
                    elif task_type == "regression":
                        evaluation_results = evaluate_sts_regression(
                            cfg,
                            latest_checkpoint,
                            task_type,
                            hyper_param_tuning=True,
                            test_dataloader=eval_dataloader)
    
                        logger.info(f" %$%$ evaluation_results: {evaluation_results}")
    
                        # Add row to DataFrame
                        new_row = pd.DataFrame([{
                            'model_name':
                            model_name,
                            'task_name':
                            task_name,
                            'learning_rate':
                            lr,
                            'weight_decay':
                            weight_decay,
                            'epochs':
                            epochs,
                            'batch_size':
                            batch_size,
                            'mse':
                            evaluation_results['mse'],
                            'rmse':
                            evaluation_results['rmse'],
                            'mae':
                            evaluation_results['mae'],
                            'pearson_correlation':
                            evaluation_results['pearson_correlation'],
                            'spearman_correlation':
                            evaluation_results['spearman_correlation'],
                            'primary_score':
                            evaluation_results['primary_score'],
                            'test_samples':
                            evaluation_results['test_samples'],
                            'evaluation_date':
                            evaluation_results['evaluation_date'],
                        }])
                        regression_results_df = pd.concat(
                            [regression_results_df, new_row], ignore_index=True)
    
                    elif task_name in ['tquad2_qa', 'xquad_qa']:
                        evaluation_results = evaluate_question_answering(
                            cfg, latest_checkpoint, eval_dataloader, tokenizer)
    
                        # Add row to DataFrame
                        new_row = pd.DataFrame([{
                            'model_name':
                            model_name,
                            'task_name':
                            task_name,
                            'learning_rate':
                            lr,
                            'weight_decay':
                            weight_decay,
                            'epochs':
                            epochs,
                            'batch_size':
                            batch_size,
                            'exact_match':
                            evaluation_results['exact_match'],
                            'f1_score':
                            evaluation_results['f1_score'],
                            'exact_match_raw':
                            evaluation_results['exact_match_raw'],
                            'f1_score_raw':
                            evaluation_results['f1_score_raw'],
                            'predictions':
                            evaluation_results['predictions'],
                            'gold_answers':
                            evaluation_results['gold_answers'],
                            'individual_exact_matches':
                            evaluation_results['individual_exact_matches'],
                            'individual_f1_scores':
                            evaluation_results['individual_f1_scores'],
                            'test_samples':
                            evaluation_results['test_samples'],
                            'evaluation_date':
                            evaluation_results['evaluation_date'],
                        }])
    
                        qa_results_df = pd.concat([qa_results_df, new_row],
                                                ignore_index=True)
                    elif task_name in ['multinli', 'snli', 'med_nli']:
                        evaluation_results = evaluate_nli(cfg, latest_checkpoint,
                                                        task_type, eval_dataloader)
    
                        macro_avg_f1_score = evaluation_results['macro_avg_f1_score']
                        weighted_avg_f1_score = evaluation_results[
                            'weighted_avg_f1_score']
                        correct_predictions = evaluation_results['correct_predictions']
                        accuracy = evaluation_results['accuracy']
                        evaluation_date = evaluation_results['evaluation_date']
    
                        # Add row to DataFrame
                        new_row = pd.DataFrame([{
                            'model_name': model_name,
                            'task_name': task_name,
                            'learning_rate': lr,
                            'weight_decay': weight_decay,
                            'epochs': epochs,
                            'batch_size': batch_size,
                            'accuracy': accuracy,
                            'correct_predictions': correct_predictions,
                            'macro_avg_f1_score': macro_avg_f1_score,
                            'weighted_avg_f1_score': weighted_avg_f1_score,
                            'evaluation_date': evaluation_date,
                        }])
    
                        results_df = pd.concat([results_df, new_row],
                                            ignore_index=True)
                        # Temporarily set option to display all columns
                        with pd.option_context('display.max_columns', None):
                            logger.info(f"Final results:\n{results_df}")
    
                    else:
                        # Get predictions
                        evaluation_results = evaluate_text_classification(
                            cfg, latest_checkpoint, task_name, eval_dataloader)
    
                        macro_avg_f1_score = evaluation_results[
                            'classification_report']['macro avg']['f1-score']
                        weighted_avg_f1_score = evaluation_results[
                            'classification_report']['weighted avg']['f1-score']
                        correct_predictions = evaluation_results['correct_predictions']
                        accuracy = evaluation_results['accuracy']
                        evaluation_date = evaluation_results['evaluation_date']
    
                        # Add row to DataFrame
                        new_row = pd.DataFrame([{
                            'model_name': model_name,
                            'task_name': task_name,
                            'learning_rate': lr,
                            'weight_decay': weight_decay,
                            'epochs': epochs,
                            'batch_size': batch_size,
                            'accuracy': accuracy,
                            'correct_predictions': correct_predictions,
                            'macro_avg_f1_score': macro_avg_f1_score,
                            'weighted_avg_f1_score': weighted_avg_f1_score,
                            'evaluation_date': evaluation_date,
                        }])
    
                        results_df = pd.concat([results_df, new_row],
                                            ignore_index=True)
                        # Temporarily set option to display all columns
                        with pd.option_context('display.max_columns', None):
                            logger.info(f"Final results:\n{results_df}")
                    torch.cuda.empty_cache()
    
            if task_type == "retrieval":
                results_df = retrieval_results_df
                retrieval_results_df = pd.DataFrame(columns=retrieval_results_df.columns)
            elif task_type == "regression":
                results_df = regression_results_df
                regression_results_df = pd.DataFrame(
                    columns=regression_results_df.columns)
            elif task_name in [
                    "wiki_ner", "xtreme_ner", "xtreme_pos", "wiki_ann_ner",
                    "pos_ud_boun", "pos_ud_imst"
            ]:
                results_df = ner_results_df
                ner_results_df = pd.DataFrame(columns=ner_results_df.columns)
            elif task_name in ['tquad2_qa', 'xquad_qa']:
                results_df = qa_results_df
                qa_results_df = pd.DataFrame(columns=qa_results_df.columns)
            # Save DataFrame to CSV
            csv_filename = output_dir / f"{model_name_concat}_{task_name}.csv"
            results_df.to_csv(csv_filename, index=False)
            logger.info(f"Results saved to CSV: {csv_filename}")
            results_df = pd.DataFrame(columns=results_df.columns)


if __name__ == "__main__":
    hyperparameter_tuner()