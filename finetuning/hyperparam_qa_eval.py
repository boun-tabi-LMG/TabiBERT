from dataloaders.qa import evaluate_question_answering as eval_function
from dataloaders.build_dataloader import build_my_dataloader
from transformers import AutoTokenizer
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

def evaluate_question_answering(cfg, checkpoint_path, test_dataloader, tokenizer):
    """Evaluate question answering model on a given dataloader/checkpoint."""
    from sequence_classification import load_model, update_batch_size_info
    import numpy as np
    import torch
    from datetime import datetime
    import string
    import re
    from collections import Counter

    def normalize_answer(s):
        """Lower text and remove punctuation, articles and extra whitespace."""
        def remove_articles(text):
            regex = re.compile(r'\b(a|an|the)\b', re.IGNORECASE)
            return re.sub(regex, ' ', text)
        
        def white_space_fix(text):
            return ' '.join(text.split())
        
        def remove_punc(text):
            exclude = set(string.punctuation)
            return ''.join(ch for ch in text if ch not in exclude)
        
        def lower(text):
            return text.lower()
        
        return white_space_fix(remove_articles(remove_punc(lower(s))))

    def get_tokens(s):
        """Get tokens from normalized answer."""
        if not s:
            return []
        return normalize_answer(s).split()

    def compute_exact_match(a_gold, a_pred):
        """Compute exact match score."""
        return int(normalize_answer(a_gold) == normalize_answer(a_pred))

    def compute_f1(a_gold, a_pred):
        """Compute F1 score between gold and predicted answers."""
        gold_toks = get_tokens(a_gold)
        pred_toks = get_tokens(a_pred)
        
        if not gold_toks and not pred_toks:
            return 1.0
        if not gold_toks or not pred_toks:
            return 0.0
        
        common = Counter(gold_toks) & Counter(pred_toks)
        num_same = sum(common.values())
        
        if len(gold_toks) == 0 or len(pred_toks) == 0:
            return int(gold_toks == pred_toks)
        
        if num_same == 0:
            return 0.0
        
        precision = 1.0 * num_same / len(pred_toks)
        recall = 1.0 * num_same / len(gold_toks)
        f1 = (2 * precision * recall) / (precision + recall)
        
        return f1

    def extract_answer_from_tokens(input_ids, start_pos, end_pos, tokenizer):
        """Extract answer text from token positions."""
        if start_pos >= len(input_ids) or end_pos >= len(input_ids) or start_pos > end_pos:
            return ""
        
        # Extract tokens between start and end positions (inclusive)
        answer_tokens = input_ids[start_pos:end_pos + 1]
        
        # Decode tokens to text
        answer_text = tokenizer.decode(answer_tokens, skip_special_tokens=True)
        
        return answer_text.strip()

    # Get batch size info
    cfg = update_batch_size_info(cfg)
    
    # Build Model
    model = load_model(cfg)

    # Get model state before loading
    original_state = {name: param.clone() for name, param in model.named_parameters()}

    # Load checkpoint
    checkpoint = torch.load(checkpoint_path, weights_only=False)
    if 'state' in checkpoint:
        state_dict = checkpoint['state']['model']
    else:
        state_dict = checkpoint
    
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

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    results = eval_function(
        model=model,
        test_dataloader=test_dataloader,
        tokenizer=tokenizer,
        device=device,
        verbose=True
    )
    
    print(f"Exact Match: {results['exact_match']:.2f}%")
    print(f"F1 Score: {results['f1_score']:.2f}%")

    return results


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python hyperparam_qa_eval.py <model_config_name> <task_config_name> <checkpoint_path> <finetuned_boolean>")
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
    
    test_dataloader = build_my_dataloader(cfg.eval_loader, cfg.dataset_name,
                                      cfg.device_eval_microbatch_size, 'test')
    tokenizer = AutoTokenizer.from_pretrained(cfg.tokenizer_name)

    evaluate_question_answering(cfg, checkpoint_path, test_dataloader, tokenizer)
    
