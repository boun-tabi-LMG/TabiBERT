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


from sklearn.metrics import classification_report as sk_classification_report, accuracy_score, f1_score
from seqeval.metrics import classification_report as seqeval_classification_report, f1_score as seqeval_f1_score

def get_tag_mappings(cfg):
    # For wiki_ner: cfg.tag2id, for xtreme_ner: cfg.tag_names
    if cfg.dataset_name == "wiki_ann_ner":
        id2tag = {i : i for i in range(7)}
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


def evaluate_token_classification(cfg, checkpoint_path, task_name, task_type, test_dataloader, is_bert_model: bool = False):
    """Evaluate token classification (NER or POS) model on a given dataloader/checkpoint."""
    from sequence_classification import load_model, update_batch_size_info
    import numpy as np
    import torch
    from datetime import datetime

    # Get batch size info
    cfg = update_batch_size_info(cfg)
    model = load_model(cfg)

    # Load checkpoint
    checkpoint = torch.load(checkpoint_path, weights_only=False)
    if 'state' in checkpoint:
        state_dict = checkpoint['state']['model']
    else:
        state_dict = checkpoint
    model.load_state_dict(state_dict, strict=False)

    model.eval()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)

    if task_type == "ner":
        if task_name == "wiki_ann_ner":
            id2tag = {
                0: "O",
                1: "B-PER", 2: "I-PER",
                3: "B-LOC", 4: "I-LOC", 
                5: "B-ORG", 6: "I-ORG"
            }
        else:
            id2tag = get_tag_mappings(cfg)
    elif task_type == "pos":
        id2tag = get_tag_mappings(cfg)
    else:
        raise ValueError(f"Unknown task_type: {task_type}")

    all_predictions, all_labels = [], []
    total_samples = 0

    print("Running token classification evaluation...")
    with torch.no_grad():
        for batch in test_dataloader:
            batch = {k: (v.to(device) if isinstance(v, torch.Tensor) else v) for k, v in batch.items()}
            outputs = model.model(input_ids=batch['input_ids'], attention_mask=batch['attention_mask'])
            predictions = torch.argmax(outputs.logits, dim=-1)
            labels = batch['labels']
            word_ids_batch = batch['word_ids']
            for i in range(predictions.shape[0]):
                pred_ids = predictions[i].cpu().numpy()
                label_ids = labels[i].cpu().numpy()
                word_ids = word_ids_batch[i].cpu().numpy() if torch.is_tensor(word_ids_batch[i]) else word_ids_batch[i]
                pred_tags, true_tags = [], []
                prev_word_idx = None
                for idx, word_idx in enumerate(word_ids):
                    if word_idx == -1 or word_idx == prev_word_idx or label_ids[idx] == -100:
                        continue
                    pred_tag = id2tag[pred_ids[idx]]
                    true_tag = id2tag[label_ids[idx]]
                    pred_tags.append(pred_tag)
                    true_tags.append(true_tag)
                    prev_word_idx = word_idx
                all_predictions.append(pred_tags)
                all_labels.append(true_tags)
                total_samples += 1

    # ---- Metric Computation ----
    if task_type == "ner":
        # Use seqeval (sequence-level)
        report = seqeval_classification_report(all_labels, all_predictions, output_dict=True)
        f1 = seqeval_f1_score(all_labels, all_predictions)
        macro_f1 = report.get("macro avg", {}).get("f1-score", f1)
        weighted_f1 = report.get("weighted avg", {}).get("f1-score", f1)
        acc = None
        correct_predictions = None
    elif task_type == "pos":
        # Flatten for token-level
        y_true = [tag for seq in all_labels for tag in seq]
        y_pred = [tag for seq in all_predictions for tag in seq]
        report = sk_classification_report(y_true, y_pred, output_dict=True, zero_division=0)
        acc = accuracy_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred, average="macro")
        macro_f1 = f1
        weighted_f1 = f1_score(y_true, y_pred, average="weighted")
        correct_predictions = int(sum(t == p for t, p in zip(y_true, y_pred)))

    evaluation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    results = {
        "test_samples": int(total_samples),
        "accuracy": acc,
        "f1_score": float(f1),
        "macro_avg_f1_score": float(macro_f1),
        "weighted_avg_f1_score": float(weighted_f1),
        "correct_predictions": correct_predictions,
        "classification_report": report,
        "evaluation_date": evaluation_date
    }

    # Save results to JSON
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

   
    if task_type == "ner":    
         # Print detailed classification report
        print("\nDetailed Classification Report:")
        print(seqeval_mt.classification_report(all_labels, all_predictions, digits=4))
    elif task_type == "pos":
        from sklearn.metrics import classification_report
        print("\nDetailed Classification Report:")
        print(classification_report(y_true, y_pred, digits=4, zero_division=0))

    return results

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
    
    evaluate_token_classification(cfg, checkpoint_path, is_finetuned) 
