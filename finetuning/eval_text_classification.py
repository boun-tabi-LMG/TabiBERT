#!/usr/bin/env python3
"""
Evaluation script for finetuned models.
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
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import json
from tabulate import tabulate
from datetime import datetime
from finetuning.dataloaders.build_dataloader import build_my_dataloader
from transformers import AutoTokenizer

torch.set_float32_matmul_precision('high')

def get_class_names(dataset_name):
    """Get class names for a given dataset."""
    if dataset_name == "snli_tr_1.0":
        return ['Entailment', 'Neutral', 'Contradiction']
    elif dataset_name == "ttc4900":
        return ['siyaset', 'dunya', 'ekonomi', 'kultur', 'saglik', 'spor', 'teknoloji']
    elif dataset_name == "prod_review":
        return ['Negative', 'Positive']
    elif dataset_name == "news_cat":
        return ['economy', 'health', 'magazine', 'politics', 'sport']
    elif dataset_name == "interpress_news":
        return [str(i) for i in range(17)]
    elif dataset_name == "bil_tweet_news":
        return [str(i) for i in range(5)]
    elif dataset_name == "gender_hate_speech":
        return [str(i) for i in range(3)]
    elif dataset_name == "pubmed_RCT":
        return ['results', 'methods', 'conclusions', 'background', 'objective']
    elif dataset_name == "sci_cite_TR":
        return ['results', 'methods', 'background']
    elif dataset_name == "thesis_abstract":
        return [str(i) for i in range(187)]
    else:
        raise ValueError(f"Unknown dataset!: {dataset_name}.")

def evaluate(
    cfg: DictConfig, 
    checkpoint_path: str, 
    is_finetuned: bool,
    is_bert_model: bool = False,
    eval_dataloader = None):
    """Evaluate a finetuned model on the test set."""

    # Get batch size info
    cfg = update_batch_size_info(cfg)

    # Build Model
    print("Initializing model...")
    model = load_model(cfg)

    if is_finetuned:
        # Get model state before loading
        original_state = {
            name: param.clone()
            for name, param in model.named_parameters()
        }

        # Load checkpoint
        checkpoint = torch.load(checkpoint_path, weights_only = False)

        # Handle different checkpoint structures
        if 'state' in checkpoint:
            state_dict = checkpoint['state']['model']
        else:
            state_dict = checkpoint

        if 'model.classifier.weight' in state_dict:
            print(f" %%%% {state_dict['model.classifier.weight']}")
        elif 'model.classifier.dense.weight' in state_dict:
            print(f" %%%% {state_dict['model.classifier.dense.weight']}")
        if 'model.classifier.bias' in state_dict:
            print(f" %%%% {state_dict['model.classifier.bias']}")
        elif 'model.classifier.dense.bias' in state_dict:
            print(f" %%%% {state_dict['model.classifier.dense.bias']}")

        # Load state dict with strict=False to handle potential mismatches
        missing_keys, unexpected_keys = model.load_state_dict(state_dict,
                                                              strict=False)
        if missing_keys:
            print(f"Warning: Missing keys: {missing_keys[:5]}..."
                  )  # Show first 5
        if unexpected_keys:
            print(f"Warning: Unexpected keys: {unexpected_keys[:5]}..."
                  )  # Show first 5

        # Check if weights actually changed
        weights_changed = False
        for name, param in model.named_parameters():
            if name in original_state:
                if not torch.equal(original_state[name], param):
                    weights_changed = True
                    break

        for name, module in model.named_modules():
            if name.endswith('classifier') and isinstance(
                    module, torch.nn.Linear):
                classifier = module

    model.eval()

    # Move model to GPU if available
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)

     # Load tokenizer for decoding input_ids when text field is not available
    tokenizer = None
    if hasattr(cfg, 'tokenizer_name'):
        tokenizer = AutoTokenizer.from_pretrained(cfg.tokenizer_name)
        print(f"Loaded tokenizer: {cfg.tokenizer_name}")

    # Create test dataloader
    test_loader = build_my_dataloader(cfg.eval_loader, cfg.dataset_name,
                                      cfg.device_eval_microbatch_size, 'test')

    # Initialize metrics
    all_predictions = []
    all_labels = []
    all_examples = []
    total_samples = 0
    correct_predictions = 0

    # Run evaluation
    print("Running evaluation...")
    with torch.no_grad():
        for batch in test_loader:
            if 'text' in batch.keys():
                print(f"Example text is: {batch['text']}")
                all_examples.extend(batch['text'])
            else:
                # Decode input_ids to get text
                if tokenizer is not None and 'input_ids' in batch.keys():
                    batch_input_ids = batch['input_ids'].cpu().numpy()
                    batch_attention_mask = batch.get('attention_mask', None)
                    if batch_attention_mask is not None:
                        batch_attention_mask = batch_attention_mask.cpu().numpy()
                    
                    # Decode each sequence in the batch
                    batch_texts = []
                    for idx, input_ids in enumerate(batch_input_ids):
                        # Use attention_mask to filter out padding tokens if available
                        if batch_attention_mask is not None:
                            # Get the actual length from attention_mask
                            actual_length = batch_attention_mask[idx].sum()
                            input_ids = input_ids[:actual_length]
                        else:
                            # Fallback: filter out padding tokens manually
                            pad_token_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else 0
                            # Find where padding starts (assuming padding is at the end)
                            non_padding_mask = input_ids != pad_token_id
                            if non_padding_mask.any():
                                last_non_padding = np.where(non_padding_mask)[0][-1] + 1
                                input_ids = input_ids[:last_non_padding]
                        
                        decoded_text = tokenizer.decode(input_ids, skip_special_tokens=True)
                        batch_texts.append(decoded_text)
                    all_examples.extend(batch_texts)
                else:
                    print("TEXT FIELD COULD NOT FOUND and cannot decode from input_ids (tokenizer not available)....")
                    # Add placeholder if we can't decode
                    batch_size = batch['input_ids'].size(0) if 'input_ids' in batch.keys() else 1
                    all_examples.extend(["[Unable to decode text]"] * batch_size)
                
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
    all_examples = np.array(all_examples)

    print(f"All_labels are: {all_labels}")
    print(f"all_predictions are: {all_predictions}")

    # Calculate accuracy
    accuracy = correct_predictions / total_samples

    # Calculate confusion matrix and per-class accuracy
    cm = confusion_matrix(all_labels, all_predictions)

    with np.errstate(divide='ignore', invalid='ignore'):
        class_accuracies = np.divide(cm.diagonal(), cm.sum(axis=1))
        class_accuracies = np.nan_to_num(class_accuracies, nan=0.0)

    class_names = get_class_names(cfg.dataset_name)

    # Find examples where label and prediction are different (incorrect predictions)
    incorrect_indices = np.where(all_labels != all_predictions)[0]
    num_incorrect = len(incorrect_indices)
    
    # Print incorrect predictions with labels and example details
    num_samples_to_show = min(20, num_incorrect) 
    print(f"Incorrect Predictions (showing {num_samples_to_show} out of {num_incorrect} incorrect predictions):")
    if num_incorrect == 0:
        print("No incorrect predictions found! All predictions are correct.")
    else:
        for sample_idx, i in enumerate(incorrect_indices[:num_samples_to_show]):
            true_label_idx = int(all_labels[i])
            pred_label_idx = int(all_predictions[i])
            true_label_name = class_names[true_label_idx] if true_label_idx < len(class_names) else str(true_label_idx)
            pred_label_name = class_names[pred_label_idx] if pred_label_idx < len(class_names) else str(pred_label_idx)
            
            example_text = all_examples[i] if i < len(all_examples) else "N/A"
            # Truncate long examples for readability
            if len(example_text) > 200:
                example_text = example_text[:200] + "..."
            
            print(f"Incorrect Sample {sample_idx + 1} (Index {i}):")
            print(f"  Example: {example_text}")
            print(f"  True Label: {true_label_name} (idx: {true_label_idx})")
            print(f"  Predicted Label: {pred_label_name} (idx: {pred_label_idx})")
            print(f"  Status: ✗ INCORRECT")
            print("-" * 100)

    # Print sample predictions with labels and example details
    num_samples = min(20, len(all_labels))  # Print up to 20 samples
    print(f"\n{'='*100}")
    print(f"Sample Predictions (showing {num_samples} out of {len(all_labels)} examples):")
    print(f"{'='*100}\n")
    
    for i in range(num_samples):
        true_label_idx = int(all_labels[i])
        pred_label_idx = int(all_predictions[i])
        true_label_name = class_names[true_label_idx] if true_label_idx < len(class_names) else str(true_label_idx)
        pred_label_name = class_names[pred_label_idx] if pred_label_idx < len(class_names) else str(pred_label_idx)
        is_correct = "✓" if true_label_idx == pred_label_idx else "✗"
        
        example_text = all_examples[i] if i < len(all_examples) else "N/A"
        # Truncate long examples for readability
        if len(example_text) > 200:
            example_text = example_text[:200] + "..."
        
        print(f"Sample {i+1}:")
        print(f"  Example: {example_text}")
        print(f"  True Label: {true_label_name} (idx: {true_label_idx})")
        print(f"  Predicted Label: {pred_label_name} (idx: {pred_label_idx})")
        print(f"  Correct: {is_correct}")
        print("-" * 100)
    
    print(f"{'='*100}\n")

    classification_report_dict = classification_report(all_labels,
                              all_predictions,
                              target_names=class_names,
                              output_dict=True,
                              zero_division=0)

    # Create results dictionary
    results = {
        "test_samples":
        int(total_samples),
        "correct_predictions":
        int(correct_predictions),
        "accuracy":
        float(accuracy),
        "per_class_accuracy": {
            class_names[i]: float(acc)
            for i, acc in enumerate(class_accuracies)
        },
        "confusion_matrix":
        cm.tolist(),
        "classification_report":
        classification_report_dict,
        "model_name":
        cfg.model_path,
        "checkpoint_path":
        checkpoint_path,
        "task_type":
        cfg.task_type,
        "evaluation_date":
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Save results to JSON
    output_dir = Path("evaluation_results")
    output_dir.mkdir(exist_ok=True)

    # Create filename based on model name and timestamp
    model_name = cfg.hf_model_name.replace("/", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"eval_results_{model_name}_{timestamp}.json"

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to: {output_file}")

    # Print results in table format
    table_data = [
        ["Test samples", "Correct predictions", "Accuracy"] + class_names,
        [f"{total_samples}", f"{correct_predictions}", f"{accuracy:.4f}"] +
        [f"{acc:.5f}" for acc in class_accuracies]
    ]

    print("\nEvaluation Results:")
    print(tabulate(table_data, headers="firstrow", tablefmt="grid"))

    # Print detailed classification report
    print("\nDetailed Classification Report:")
    classificationReport = classification_report(all_labels,
                                                 all_predictions,
                                                 target_names=class_names,
                                                 digits=5,
                                                 zero_division=0)

    print(classificationReport)

    print('#' * 100)
    print()

    return classification_report_dict, all_labels, all_predictions, all_examples

def compare_two_models(labels, predictions_1, predictions_2, examples=None):
    """
    Compare predictions from two models and print examples where:
    - Model 1 is correct and Model 2 is wrong
    - Model 2 is correct and Model 1 is wrong
    """
    labels = np.array(labels)
    predictions_1 = np.array(predictions_1)
    predictions_2 = np.array(predictions_2)

    model1_correct = predictions_1 == labels
    model2_correct = predictions_2 == labels

    # Model 1 correct, Model 2 wrong
    model1_only = np.where((model1_correct) & (~model2_correct))[0]
    # Model 2 correct, Model 1 wrong
    model2_only = np.where((model2_correct) & (~model1_correct))[0]

    print(f"\nExamples where Model 1 is correct and Model 2 is wrong (total: {len(model1_only)}):")
    for idx in model1_only:
        example_str = f" Example: {examples[idx]}" if examples is not None else ""
        print(f"Index: {idx}, Label: {labels[idx]}, Model 1 Prediction: {predictions_1[idx]}, Model 2 Prediction: {predictions_2[idx]}{example_str}")

    print(f"\nExamples where Model 2 is correct and Model 1 is wrong (total: {len(model2_only)}):")
    for idx in model2_only:
        example_str = f" Example: {examples[idx]}" if examples is not None else ""
        print(f"Index: {idx}, Label: {labels[idx]}, Model 1 Prediction: {predictions_1[idx]}, Model 2 Prediction: {predictions_2[idx]}{example_str}")

    print(f"\nSummary:")
    print(f"Total examples: {len(labels)}")
    print(f"Model 1 correct only: {len(model1_only)}")
    print(f"Model 2 correct only: {len(model2_only)}")
    print(f"Both correct: {np.sum(model1_correct & model2_correct)}")
    print(f"Both wrong: {np.sum(~model1_correct & ~model2_correct)}")


if __name__ == "__main__":
    if len(sys.argv) == 5:
        # Evaluate one model:
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
        
    elif len(sys.argv) == 6:
        # Compare two models:
        task_config_name, model_1_config_name, model_1_checkpoint_path, model_2_config_name, model_2_checkpoint_path = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5] 
        
        # Initialize Hydra and load task config with defaults
        with initialize(config_path="yamls", version_base=None):
            task_cfg = compose(config_name=task_config_name)
        om.set_struct(task_cfg, False)
        
        # Load model configs:
        with open(model_1_config_name) as f:
            model_1_cfg = om.load(f)
        
        with open(model_2_config_name) as f:
            model_2_cfg = om.load(f)
        om.set_struct(model_1_cfg, False)
        om.set_struct(model_2_cfg, False)
        cfg_1 = om.merge(task_cfg, model_1_cfg)
        cfg_1 = cast(DictConfig, cfg_1)

        cfg_2 = om.merge(task_cfg, model_2_cfg)
        cfg_2 = cast(DictConfig, cfg_2)

        classification_report_dict, labels, predictions_1, examples = evaluate(cfg_1, model_1_checkpoint_path, 1)
        classification_report_dict, _, predictions_2, _ = evaluate(cfg_2, model_2_checkpoint_path, 1, is_bert_model=True)

        print(f"Model 1 checkpoint is: {model_1_checkpoint_path} ")
        print(f"Model 2 checkpoint is: {model_2_checkpoint_path} ")
        
        compare_two_models(labels, predictions_1, predictions_2, examples=examples)

    else:
        print("Usage for one model: python eval_text_classification.py <model_config_name> <task_config_name> <checkpoint_path> <finetuned_boolean>")
        print("Usage for two models: python eval_text_classification.py <task_config_name> <model_1_config_name> <model_1_checkpoint_path> <model_2_config_name> <model_2_checkpoint_path>")
        sys.exit(1)