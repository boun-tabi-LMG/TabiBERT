from dataloaders.build_dataloader import build_my_dataloader
from sequence_classification import load_model, update_batch_size_info
from sklearn.metrics import confusion_matrix
import sklearn.metrics as smt
from tabulate import tabulate
import numpy as np
import torch
from datetime import datetime
import logging
import sys
import hydra
from omegaconf import DictConfig
from hydra import compose, initialize
from pathlib import Path
from typing import Optional, cast
from omegaconf import OmegaConf as om
import json
torch.set_float32_matmul_precision('high')

def evaluate_nli(cfg, checkpoint_path, dataset_name, test_dataloader, is_bert_model: bool = False):
    """Evaluate Natural Language Inference (NLI) model on a given dataloader/checkpoint."""
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
    
    # Initialize metrics
    all_predictions = []
    all_labels = []
    total_samples = 0
    correct_predictions = 0
    
    # Run evaluation
    print("Running NLI evaluation...")

    with torch.no_grad():
        for batch in test_dataloader:
            # Move batch to device
            for k, v in batch.items():
                if isinstance(v, torch.Tensor):
                    batch[k] = v.to(device)
           
            # Filter batch to only include keys that the models expect
            if is_bert_model:
                label_str = 'labels'
            else:
                label_str = 'label'
            expected_keys = {'input_ids', 'attention_mask', label_str}
            model_inputs = {k: v for k, v in batch.items() if k in expected_keys}

            # Forward pass
            outputs = model.model(**model_inputs)  # Access the underlying model
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

    # NLI class names (standard for most NLI datasets)
    class_names = get_nli_class_names(dataset_name)

    classification_report_dict = smt.classification_report(all_labels,
                              all_predictions,
                              target_names=class_names,
                              output_dict=True,
                              zero_division=0)

    # Calculate F1 scores for compatibility with token classification format
    macro_avg_f1_score = classification_report_dict.get('macro avg', {}).get('f1-score', 0.0)
    weighted_avg_f1_score = classification_report_dict.get('weighted avg', {}).get('f1-score', 0.0)
    
    # Print results in table format
    table_data = [
        ["Test samples", "Correct predictions", "Accuracy"] + class_names,
        [f"{total_samples}", f"{correct_predictions}", f"{accuracy:.4f}"] +
        [f"{acc:.5f}" for acc in class_accuracies]
    ]

    logger.info("\nNLI Evaluation Results:")
    print("\nNLI Evaluation Results:")
    logger.info(tabulate(table_data, headers="firstrow", tablefmt="grid"))
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))

    # Print detailed classification report
    logger.info("\nDetailed Classification Report:")
    print("\nDetailed Classification Report:")
    classificationReport = smt.classification_report(all_labels,
                                                 all_predictions,
                                                 target_names=class_names,
                                                 digits=5,
                                                 zero_division=0)

    logger.info(classificationReport)
    print(classificationReport)

    # Return format compatible with both text and token classification
    evaluation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return {
        "test_samples": int(total_samples),
        "correct_predictions": int(correct_predictions),
        "accuracy": float(accuracy),
        "f1_score": float(weighted_avg_f1_score),  # Use weighted avg as main F1
        "macro_avg_f1_score": float(macro_avg_f1_score),
        "weighted_avg_f1_score": float(weighted_avg_f1_score),
        "per_class_accuracy": {
            class_names[i]: float(acc)
            for i, acc in enumerate(class_accuracies)
        },
        "confusion_matrix": cm.tolist(),
        "classification_report": classification_report_dict,
        "evaluation_date": evaluation_date
    }


def get_nli_class_names(dataset_name):
    """Get class names for NLI datasets."""
    # Standard NLI class names for most datasets (SNLI, MultiNLI, etc.)
    nli_class_mapping = {
        'snli': ['entailment', 'neutral', 'contradiction'],
        'multinli': ['entailment', 'neutral', 'contradiction'],
        'xnli': ['entailment', 'neutral', 'contradiction'],
        'rte': ['entailment', 'not_entailment'],  # RTE is binary
        'wnli': ['not_entailment', 'entailment'],  # WNLI is binary
    }
    
    # Default to standard 3-class NLI if dataset not found
    dataset_name_lower = dataset_name.lower()
    for key in nli_class_mapping:
        if key in dataset_name_lower:
            return nli_class_mapping[key]
    
    # Default case
    return ['entailment', 'neutral', 'contradiction']


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python hyperparam_nli_eval.py <model_config_name> <task_config_name> <checkpoint_path>")
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

    test_dataloader = build_my_dataloader(cfg.eval_loader, cfg.dataset_name,
                                      cfg.device_eval_microbatch_size, 'test')
    
    evaluate_nli(cfg, checkpoint_path, task_config_name, test_dataloader) 