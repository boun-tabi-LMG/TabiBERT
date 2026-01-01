from torch.utils.data import Dataset
import torch
import numpy as np
import string
import re
from collections import Counter
from typing import List, Dict, Any
from datetime import datetime

class DataCollatorForQuestionAnswering:
    """
    Data collator for question answering that handles metadata properly.
    """
    
    def __call__(self, features: List[Dict[str, Any]]) -> Dict[str, Any]:
        # Separate main features from metadata
        batch = {}
        metadata = []
        
        # Get the main tensor fields
        tensor_keys = ['input_ids', 'attention_mask', 'start_positions', 'end_positions']
        
        for key in tensor_keys:
            if key in features[0]:
                batch[key] = torch.stack([f[key] for f in features])
        
        # Handle metadata separately
        for f in features:
            if '_metadata' in f:
                metadata.append(f['_metadata'])
            else:
                # Collect from individual keys
                meta_dict = {}
                for key in metadata_keys:
                    if key in f:
                        meta_dict[key] = f[key]
                metadata.append(meta_dict)
        
        # Add metadata to batch (these won't go through tensor operations)
        batch['_metadata'] = metadata
        
        return batch


class QADataset(Dataset):
    def __init__(self, dataset, tokenizer, max_length, is_lower: bool = False):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.is_lower = is_lower

    def __len__(self):
        return len(self.dataset)

    def to_lower_tr(self, obj):
        if isinstance(obj, str):
            return obj.replace("I", "ı").lower()
        elif isinstance(obj, list):
            return [self.to_lower_tr(x) for x in obj]
        elif isinstance(obj, dict):
            return {k: self.to_lower_tr(v) for k, v in obj.items()}
        else:
            return obj

    def __getitem__(self, idx):
        example = self.dataset[idx]
        context = example['context']
        question = example['question']
        answers = example['answers']

        if self.is_lower:
            context = self.to_lower_tr(context)
            question = self.to_lower_tr(question)
            answers = self.to_lower_tr(answers)
            
        # Normalize answer format - handle both formats from QA tasks
        if isinstance(answers, dict): # for Xquad
            # Format 1: {'text': ['136'], 'answer_start': [480]}
            if 'text' in answers and 'answer_start' in answers:
                answer_texts = answers['text']
                answer_starts = answers['answer_start']
            else:
                answer_texts = []
                answer_starts = []
        elif isinstance(answers, list):  # for Tquad
            # Format 2: [{'answer_start': 400, 'text': 'William Iron Arm'}]
            answer_texts = [ans['text'] for ans in answers if 'text' in ans]
            answer_starts = [ans['answer_start'] for ans in answers if 'answer_start' in ans]
        else:
            answer_texts = []
            answer_starts = []
        
        # Tokenize question and context
        encoding = self.tokenizer(
            question,
            context,
            truncation='only_second',  # Only truncate context, not question
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt',
            return_offsets_mapping=True,
            return_overflowing_tokens=False
        )
        
        # Extract offset mapping and remove batch dimension
        offset_mapping = encoding['offset_mapping'].squeeze(0)
        sequence_ids = encoding.sequence_ids(0)  # 0 for first example in batch
        
        # Initialize positions
        start_position = 0  # Default to CLS token
        end_position = 0
        
        # Find answer positions if we have answers
        if answer_texts and answer_starts:
            answer_start_char = answer_starts[0]
            answer_text = answer_texts[0]
            answer_end_char = answer_start_char + len(answer_text)
            
            # Find token positions that correspond to character positions
            token_start_position = 0
            token_end_position = 0
            
            for i, (start_offset, end_offset) in enumerate(offset_mapping):
                # Skip tokens that don't belong to context (sequence_id != 1)
                if sequence_ids[i] != 1:  # 1 = context, 0 = question, None = special tokens
                    continue
                
                # Check if this token contains the start of the answer
                if start_offset <= answer_start_char < end_offset:
                    token_start_position = i
                
                # Check if this token contains the end of the answer
                if start_offset < answer_end_char <= end_offset:
                    token_end_position = i
                    break
                
                # If we're past the answer, stop
                if start_offset >= answer_end_char:
                    break
            
            # Validate positions
            if token_start_position > 0 and token_end_position >= token_start_position:
                start_position = token_start_position
                end_position = token_end_position
            else:
                # Answer not found in truncated context
                start_position = 0
                end_position = 0
        
        # Prepare return dictionary
        result = {
            'input_ids': encoding['input_ids'].squeeze(0),
            'attention_mask': encoding['attention_mask'].squeeze(0),
            'start_positions': torch.tensor(start_position, dtype=torch.long),
            'end_positions': torch.tensor(end_position, dtype=torch.long),
            '_metadata': {
                'offset_mapping': offset_mapping,
                'example_id': example.get('id', idx),
                'context': context,
                'question': question,
                'gold_answers': answer_texts,
                'sequence_ids': encoding.sequence_ids(0),
            }
        }
        return result


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


def extract_answer_from_offsets(context, offset_mapping, start_pos, end_pos, sequence_ids=None):
    """Extract answer using offset mapping (more accurate)."""
    try:
        # Check for invalid positions
        if (start_pos >= len(offset_mapping) or 
            end_pos >= len(offset_mapping) or 
            start_pos > end_pos):
            return ""
        
        # Check if positions are special tokens or question tokens
        if sequence_ids is not None:
            # Only accept positions in context (sequence_id == 1)
            if sequence_ids[start_pos] != 1 or sequence_ids[end_pos] != 1:
                return ""
        
        # Check if offsets are valid (not special tokens)
        if offset_mapping[start_pos] == (0, 0) or offset_mapping[end_pos] == (0, 0):
            return ""
        
        start_char = offset_mapping[start_pos][0]
        end_char = offset_mapping[end_pos][1]
        
        if start_char >= len(context) or end_char > len(context) or start_char >= end_char:
            return ""
        
        return context[start_char:end_char].strip()
    except Exception as e:
        print(f"Error extracting answer: {e}")
        return ""


def evaluate_question_answering(model, test_dataloader, tokenizer, device=None, verbose=True):
    """
    Evaluate question answering model on a given dataloader.
    
    Args:
        model: The QA model to evaluate
        test_dataloader: DataLoader with test data
        tokenizer: Tokenizer used for the model
        device: Device to run evaluation on
        verbose: Whether to print detailed results
    
    Returns:
        Dictionary with evaluation metrics
    """
    if device is None:
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    model.eval()
    model = model.to(device)

    # Initialize metrics
    all_exact_matches = []
    all_f1_scores = []
    all_predictions = []
    all_gold_answers = []
    all_contexts = []
    all_questions = []
    total_samples = 0
    
    if verbose:
        print("Running question answering evaluation...")

    with torch.no_grad():
        for batch_idx, batch in enumerate(test_dataloader):
            # Move tensors to device
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            offset_mapping = [m['offset_mapping'] for m in batch['_metadata']]
            outputs = model({
                'input_ids': input_ids,
                'attention_mask': attention_mask
            })
            
            # Get predictions
            start_logits = outputs.start_logits
            end_logits = outputs.end_logits
            
            # Find best start and end positions
            start_predictions = torch.argmax(start_logits, dim=-1)
            end_predictions = torch.argmax(end_logits, dim=-1)
            
            # Process each sample in the batch
            batch_size = start_predictions.size(0)
            for i in range(batch_size):
                start_pos = start_predictions[i].item()
                end_pos = end_predictions[i].item()
                metadata = batch['_metadata'][i]
                context = metadata['context']
                gold_answers = metadata['gold_answers']
                question = metadata['question']
                sequence_ids = metadata['sequence_ids']
                offset_map = metadata['offset_mapping']

                # DEBUG: Print first few examples
                if total_samples < 5:
                    print(f"\n=== Sample {total_samples} ===")
                    print(f"Start pos: {start_pos}, End pos: {end_pos}")
                    print(f"Sequence IDs at positions: start={sequence_ids[start_pos] if start_pos < len(sequence_ids) else 'OOB'}, end={sequence_ids[end_pos] if end_pos < len(sequence_ids) else 'OOB'}")
                    print(f"Offset at start: {offset_map[start_pos] if start_pos < len(offset_map) else 'OOB'}")
                    print(f"Offset at end: {offset_map[end_pos] if end_pos < len(offset_map) else 'OOB'}")
                
                
                if end_pos < start_pos:
                    predicted_answer = ""
                else:
                    # Extract predicted answer using offset mapping with sequence_ids
                    predicted_answer = extract_answer_from_offsets(
                        context, offset_map, start_pos, end_pos, sequence_ids
                    )
                
                    # Fallback to token-based extraction if offset method fails, and only if positions are in context (check sequence_ids)
                    if not predicted_answer and start_pos > 0:
                        if (start_pos < len(sequence_ids) and 
                            end_pos < len(sequence_ids) and
                            sequence_ids[start_pos] == 1 and 
                            sequence_ids[end_pos] == 1):
                            input_ids_sample = input_ids[i].cpu().numpy()
                            predicted_answer = extract_answer_from_tokens(
                                input_ids_sample, start_pos, end_pos, tokenizer
                            )
                
                if not gold_answers:
                    gold_answers = [""]
                
                # For multiple gold answers, compute metrics against all and take max
                best_exact_match = 0
                best_f1 = 0.0
                
                for gold_answer in gold_answers:
                    exact_match = compute_exact_match(gold_answer, predicted_answer)
                    f1_score = compute_f1(gold_answer, predicted_answer)
                    
                    best_exact_match = max(best_exact_match, exact_match)
                    best_f1 = max(best_f1, f1_score)
             
                # Store results
                all_exact_matches.append(best_exact_match)
                all_f1_scores.append(best_f1)
                all_predictions.append(predicted_answer)
                all_gold_answers.append(gold_answers)
                all_contexts.append(context)
                all_questions.append(question)
                total_samples += 1
            
            if verbose and (batch_idx + 1) % 50 == 0:
                print(f"Processed {batch_idx + 1} batches ({total_samples} samples)...")

    # Calculate overall metrics
    exact_match_score = np.mean(all_exact_matches) * 100  # Convert to percentage
    f1_score = np.mean(all_f1_scores) * 100  # Convert to percentage
    
    # Create detailed results
    evaluation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("all_exact_matches[:10]:", all_exact_matches[:10])
    print("all_f1_scores[:10]:", all_f1_scores[:10])
    print("type(all_exact_matches[0]):", type(all_exact_matches[0]))
    
    if verbose:
        # Show some examples
        print(f"\nSample predictions (first 20):")
        for i in range(min(20, len(all_predictions))):
            print(f"Question: {all_questions[i]}")
            print(f"Context: {all_contexts[i][:100]}...")
            print(f"Gold: {all_gold_answers[i]}")
            print(f"Pred: '{all_predictions[i]}'")
            print(f"EM: {all_exact_matches[i]}, F1: {all_f1_scores[i]:.3f}")
            print("-" * 80)
        
        print("=" * 120)


        # Print results
        print(f"\nQuestion Answering Evaluation Results:")
        print(f"Total samples: {total_samples}")
        print(f"Exact Match: {exact_match_score:.2f}%")
        print(f"F1 Score: {f1_score:.2f}%")

    return {
        "test_samples": int(total_samples),
        "exact_match": float(exact_match_score),
        "f1_score": float(f1_score),
        "exact_match_raw": float(np.mean(all_exact_matches)),
        "f1_score_raw": float(np.mean(all_f1_scores)),
        "predictions": all_predictions,
        "gold_answers": all_gold_answers,
        "individual_exact_matches": all_exact_matches,
        "individual_f1_scores": all_f1_scores,
        "contexts": all_contexts,
        "questions": all_questions,
        "evaluation_date": evaluation_date
    }



"""
Usage example for the DataCollator, in build_dataloader.py, for both Training and Evaluation Dataloader (avoids collator issues):

dataloader = DataLoader(
    dataset,
    collate_fn=DataCollatorForQuestionAnswering(),
    batch_size=device_batch_size,
    sampler=dist.get_sampler(dataset,
                             drop_last=cfg.drop_last,
                             shuffle=cfg.shuffle),
)
    
For Evaluation, in the ../hyperparam_qa_eval.py:
===============
results = evaluate_question_answering(
    model=your_model,
    test_dataloader=eval_dataloader,
    tokenizer=tokenizer,
    device=torch.device('cuda')
)

print(f"Exact Match: {results['exact_match']:.2f}%")
print(f"F1 Score: {results['f1_score']:.2f}%")
"""