from dataloaders.build_dataloader import build_my_dataloader
import sys
import hydra
from omegaconf import DictConfig
from hydra import compose, initialize
from pathlib import Path
from typing import Optional, cast
import torch
from omegaconf import OmegaConf as om
import numpy as np
import json

from sequence_classification import load_model, update_batch_size_info
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import mean_squared_error, mean_absolute_error
from tabulate import tabulate
from datetime import datetime
import logging

torch.set_float32_matmul_precision('high')

def evaluate_sts_regression(cfg, checkpoint_path, dataset_name, hyper_param_tuning: bool = True, test_dataloader=None, is_bert_model: bool = False):
    """Evaluate Semantic Textual Similarity (STS) regression model on a given dataloader/checkpoint."""


    logger = logging.getLogger(__name__)

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
    missing_keys, unexpected_keys = model.load_state_dict(state_dict, strict=False)
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

    if not hyper_param_tuning:
        test_dataloader = build_my_dataloader(cfg.eval_loader, cfg.dataset_name, cfg.device_eval_microbatch_size, 'test')
    # Initialize containers for predictions and labels
    all_predictions = []
    all_labels = []
    total_samples = 0
    
    # Run evaluation
    print("Running STS regression evaluation...")

    with torch.no_grad():
        for batch in test_dataloader:
            # Move batch to device
            for k, v in batch.items():
                if isinstance(v, torch.Tensor):
                    batch[k] = v.to(device)
           
            expected_keys = {'input_ids', 'attention_mask', 'labels'}
            model_inputs = {k: v for k, v in batch.items() if k in expected_keys}

            # Forward pass
            outputs = model.model(**model_inputs)  # Access the underlying model
            
            # For regression, we typically take the raw logits (single output)
            # Squeeze to remove extra dimensions if needed
            predictions = outputs.logits.squeeze(-1) if outputs.logits.dim() > 1 else outputs.logits

            # Store predictions and labels
            all_predictions.extend(predictions.cpu().numpy())
            all_labels.extend(batch['labels'].cpu().numpy())

            # Update sample count
            total_samples += batch['labels'].size(0)

    # Convert to numpy arrays
    min_score, max_score = get_sts_score_range(dataset_name)
    all_predictions = np.clip(all_predictions, min_score, max_score)
    all_labels = np.array(all_labels)

    # Calculate regression metrics
    mse = mean_squared_error(all_labels, all_predictions)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(all_labels, all_predictions)
    
    # Calculate correlation coefficients
    pearson_corr, pearson_p = pearsonr(all_labels, all_predictions)
    spearman_corr, spearman_p = spearmanr(all_labels, all_predictions)
    
    # Handle NaN values that might occur with constant predictions
    pearson_corr = 0.0 if np.isnan(pearson_corr) else pearson_corr
    spearman_corr = 0.0 if np.isnan(spearman_corr) else spearman_corr
    pearson_p = 1.0 if np.isnan(pearson_p) else pearson_p
    spearman_p = 1.0 if np.isnan(spearman_p) else spearman_p
    
    # Calculate additional STS-specific metrics
    # For STS, scores are typically in range [0, 5], so we can calculate score distribution stats
    label_mean = np.mean(all_labels)
    label_std = np.std(all_labels)
    pred_mean = np.mean(all_predictions)
    pred_std = np.std(all_predictions)
    
    # Calculate score range metrics
    label_min, label_max = np.min(all_labels), np.max(all_labels)
    pred_min, pred_max = np.min(all_predictions), np.max(all_predictions)

    # Print results in table format
    table_data = [
        ["Metric", "Value"],
        ["Test samples", f"{total_samples}"],
        ["MSE", f"{mse:.6f}"],
        ["RMSE", f"{rmse:.6f}"],
        ["MAE", f"{mae:.6f}"],
        ["Pearson correlation", f"{pearson_corr:.6f}"],
        ["Spearman correlation", f"{spearman_corr:.6f}"],
        ["Label mean ± std", f"{label_mean:.3f} ± {label_std:.3f}"],
        ["Prediction mean ± std", f"{pred_mean:.3f} ± {pred_std:.3f}"],
        ["Label range", f"[{label_min:.3f}, {label_max:.3f}]"],
        ["Prediction range", f"[{pred_min:.3f}, {pred_max:.3f}]"]
    ]

    logger.info("\nSTS Regression Evaluation Results:")
    logger.info(tabulate(table_data, headers="firstrow", tablefmt="grid"))
    print("\nSTS Regression Evaluation Results:")
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))

    # Print additional statistics
    logger.info(f"\nCorrelation Statistics:")
    logger.info(f"Pearson r = {pearson_corr:.6f} (p-value = {pearson_p:.6f})")
    logger.info(f"Spearman ρ = {spearman_corr:.6f} (p-value = {spearman_p:.6f})")

    # For STS datasets, Pearson correlation is typically the main metric
    primary_score = pearson_corr
    
    evaluation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Return for regression tasks
    return {
        "test_samples": int(total_samples),
        "mse": float(mse),
        "rmse": float(rmse),
        "mae": float(mae),
        "pearson_correlation": float(pearson_corr),
        "spearman_correlation": float(spearman_corr),
        "pearson_p_value": float(pearson_p),
        "spearman_p_value": float(spearman_p),
        "primary_score": float(primary_score),  # Main metric for STS
        "label_statistics": {
            "mean": float(label_mean),
            "std": float(label_std),
            "min": float(label_min),
            "max": float(label_max)
        },
        "prediction_statistics": {
            "mean": float(pred_mean),
            "std": float(pred_std),
            "min": float(pred_min),
            "max": float(pred_max)
        },
        "evaluation_date": evaluation_date
    }


def get_sts_score_range(dataset_name):
    """Get expected score range for different STS datasets."""
    sts_ranges = {
        'sts': (0, 5),      # STS Benchmark: 0-5 scale
        'sts12': (0, 5),     # SemEval STS 2012: 0-5 scale  
        'sts13': (0, 5),     # SemEval STS 2013: 0-5 scale
        'sts14': (0, 5),     # SemEval STS 2014: 0-5 scale
        'sts15': (0, 5),     # SemEval STS 2015: 0-5 scale
        'sts16': (0, 5),     # SemEval STS 2016: 0-5 scale
        'sick_tr': (1, 5),   # SICK dataset: 1-5 scale
    }
    
    dataset_name_lower = dataset_name.lower()
    for key in sts_ranges:
        if key in dataset_name_lower:
            return sts_ranges[key]
    
    # Default to STS Benchmark range
    return (0, 5)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python hyperparam_sts_eval.py <model_config_name> <task_config_name> <checkpoint_path>")
        sys.exit(1)

    model_config_name, task_config_name, checkpoint_path = sys.argv[1], sys.argv[2], sys.argv[3]

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
    
    evaluate_sts_regression(cfg, checkpoint_path, task_config_name, hyper_param_tuning=False) 