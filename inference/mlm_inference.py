import torch
import argparse
import json
from datetime import timedelta
from typing import List, Dict, Any
from datetime import datetime
import os
from load_model_from_checkpoint import load_model
from read_dataset import read_json_dataset
from utils import setup_logging

# Set up logging
logger = setup_logging('mlm_inference.py')

# Add timedelta to safe globals
# torch.serialization.add_safe_globals([timedelta])

# TODO: Modiy the following function for clean MLM output.

def predict_masked_tokens(model, tokenizer, text_dict: Dict[str, str], top_k: int = 5, device=None):
    """
    Predict masked tokens in the input text from a dictionary.
    
    Args:
        model: The loaded model
        tokenizer: The tokenizer
        text_dict: Dictionary containing text and metadata
            {
                "id": string,
                "domain": string,
                "language": "en" | "tr",
                "length": "short" | "mid" | "long",
                "text": string
            }
        top_k: Number of top predictions to return for each mask (default: 5)
        device: Device to run inference on
    
    Returns:
        List[List[Tuple[str, float]]]: List of predictions for each mask token
    """
    if device is None:
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
    # Log metadata
    logger.info(f"Processing text with ID: {text_dict['id']}")
    logger.info(f"Domain: {text_dict['domain']}")
    logger.info(f"Language: {text_dict['language']}")
    logger.info(f"Length: {text_dict['length']}")
    
    # Extract text
    text = text_dict['masked_text']
    # logger.info(f"Original text:\n{text}")
    
    # Prepare input text
    inputs = tokenizer(text, return_tensors="pt")
    inputs = {k: v.to(device) for k, v in inputs.items()}
    
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = outputs.logits
        
    # Get the predicted token
    mask_token_index = torch.where(inputs["input_ids"] == tokenizer.mask_token_id)[1]
    mask_token_logits = predictions[0, mask_token_index, :]
    top_k_tokens = torch.topk(mask_token_logits, k=top_k, dim=1)
    
    # Store predictions for each mask
    all_predictions = []
    
    # Process each mask token
    for i, mask_index in enumerate(mask_token_index):
        mask_predictions = []
        # logger.info(f"Predictions for mask token {i+1}:")
        predictions_str = f"\nPredictions for mask token {i+1}\n"
        # Get top-k predictions for this mask
        for score, token_id in zip(top_k_tokens.values[i], top_k_tokens.indices[i]):
            token = tokenizer.decode([token_id]).strip()
            probability = torch.softmax(mask_token_logits[i], dim=0)[token_id].item()
            mask_predictions.append((token, probability))
            # logger.info(f"  - {token}: {probability:.4f}")
            predictions_str += f"  - {token}: {probability:.4f}\n"
        logger.info(predictions_str)
        all_predictions.append(mask_predictions)
    
    # Create filled text with best predictions
    filled_text = text
    for i, predictions in enumerate(all_predictions):
        best_token = predictions[0][0]  # Get the token with highest probability
        best_token = predictions[1][0] if best_token == tokenizer.mask_token else best_token
        filled_text = filled_text.replace(tokenizer.mask_token, f"[{best_token}]", 1)
    
    logger.info(f"Text with masks:\n{text}")
    logger.info(f"Text with predictions:\n{filled_text}")
    
    return all_predictions, filled_text

def inference(model, tokenizer, text_path, top_k=5):
    """
    Perform masked language model inference on a given text file.
    
    Args:
        model: The loaded model
        tokenizer: The tokenizer
        text_path: The path to the text file
        top_k: Number of top predictions to return for each mask (default: 5)

    Returns:
        List[Dict[str, Any]]: List of dictionaries containing text samples and their metadata
    """
    if text_path:
        try:
            samples = read_json_dataset(text_path)
            logger.info(f"Loaded {len(samples)} samples from {text_path}")
            
            all_results = []
            for sample in samples:
                logger.info(f"\n{'='*50}")
                logger.info(f"Processing sample {sample['id']}")
                predictions = predict_masked_tokens(model, tokenizer, sample, top_k=top_k)
                all_results.append({
                    'id': sample['id'],
                    'predictions': predictions
                })
                
            return all_results
            
        except Exception as e:
            logger.error(f"Error processing text file: {str(e)}")
            raise
    else:
        logger.error("No text file provided")
        raise ValueError("No text file provided")

def main():
    # Set up device and model
    # device = 'cpu'
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    logger.info(f"Using device: {device}")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--checkpoint_path', type=str, default="", help="Path to model checkpoint")
    parser.add_argument('-t', '--tokenizer', type=str, default="", help="Path or HuggingFace repo to tokenizer")
    parser.add_argument('-p', '--text_path', type=str, default="", help="Path to the JSON file containing text samples")
    parser.add_argument('-k', '--top_k', type=int, default=5, help="Number of top predictions to return for each mask")
    
    args = parser.parse_args()
    checkpoint_path = args.checkpoint_path
    tokenizer = args.tokenizer
    text_path = args.text_path
    top_k = args.top_k
    
    model, tokenizer = load_model(checkpoint_path, tokenizer)
    model.to(device)

    # logger.info(f"Model type is: {type(model)}")
    # logger.info(f"Tokenizer type is: {type(tokenizer)}")
    logger.info("Model successfully loaded and moved to device")
    
    if text_path:
        results = inference(model, tokenizer, text_path, top_k=top_k)
        logger.info(f"Completed processing {len(results)} samples")

if __name__ == "__main__":
    main()
    torch.cuda.empty_cache()
    logger.info("Script completed successfully")
    
# Example usage:
# python3 inference/mlm_inference.py -c "/workspace/TabiBERT/checkpoints/latest-rank0.pt" -t "boun-tabilab/TabiBERT" -p "inference/inference_dataset/mid_masked.json" -k 3 > MID.txt
# python3 inference/mlm_inference.py -c "/workspace/TabiBERT/checkpoints/latest-rank0.pt" -t "boun-tabilab/TabiBERT" -p "inference/inference_dataset/short_masked.json" -k 3
# python3 inference/mlm_inference.py -c "/workspace/TabiBERT/checkpoints/latest-rank0.pt" -t "boun-tabilab/TabiBERT" -p "inference/inference_dataset/long_masked.json" -k 3 > LONG.txt