import argparse
import torch
import os
import json
from datetime import timedelta
from transformers import ModernBertConfig, ModernBertForMaskedLM
from typing import Union
from transformers import AutoTokenizer
from transformers import (AutoTokenizer, PreTrainedTokenizer,
                          PreTrainedTokenizerFast)
from utils import setup_logging
from build_local_tokenizer import build_local_tokenizer

# Set up logging
logger = setup_logging('load_model_from_checkpoint.py')

Tokenizer = Union[PreTrainedTokenizer, PreTrainedTokenizerFast]

def load_model(checkpoint_path, tokenizer, language="en", tokenizer_location: str = "hf"):
    """
    Load the pretrained ModernBERT model and tokenizer
    """
    logger.info(f"Loading model from {checkpoint_path}")
    
    try:
        # Load checkpoint with weights_only=False since we trust our checkpoint
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        checkpoint = torch.load(checkpoint_path, map_location=device, weights_only=False)
        
        # Extract model configuration from checkpoint
        config_dict = checkpoint['state']['integrations']['huggingface']['model']['config']['content']
        # logger.info(f"Model configuration found in checkpoint: {config_dict}")
        
        # Create ModernBertConfig from the saved configuration
        config = ModernBertConfig(**config_dict)
        model = ModernBertForMaskedLM(config)
        
        # Extract and load model weights
        if 'state' in checkpoint:
            state_dict = checkpoint['state']['model']
        else:
            state_dict = checkpoint
            
            
        # Create new state dict with corrected keys
        new_state_dict = {}
        for key, value in state_dict.items():
                
            # Map the keys to match ModernBERT's expected structure
            if 'bert.embeddings' in key:
                key = key.replace('bert.embeddings', 'embeddings')
            elif 'bert.encoder.layers' in key:
                key = key.replace('bert.encoder.layers', 'layers')
            elif 'bert.final_norm' in key:
                key = key.replace('bert.final_norm', 'final_norm')
            elif 'head.dense' in key:
                key = key.replace('model.', '')
            elif 'head.norm' in key:
                key = key.replace('model.', '')
            elif 'decoder' in key:
                key = key.replace('model.', '')
                    
            new_state_dict[key] = value
        
        # Load state dict into model
        missing_keys, unexpected_keys = model.load_state_dict(new_state_dict, strict=False)
       
        logger.info("Model initialized and weights loaded successfully.")
        
        if missing_keys:
            logger.warning(f"Missing keys: ({len(missing_keys)}) {missing_keys}")
        if unexpected_keys:
            logger.warning(f"Unexpected keys: ({len(unexpected_keys)}) {unexpected_keys}")
        
        # Set model to evaluation mode
        model.eval()
        
        if tokenizer_location == "hf" or (language == "en"):
            # Initialize tokenizer from the same config
            logger.info(f"Loading tokenizer from: {tokenizer}")
            tokenizer = AutoTokenizer.from_pretrained(tokenizer)
            if hasattr(config, 'vocab_size'):
                tokenizer.model_max_length = config.max_position_embeddings
        else:
            tokenizer = build_local_tokenizer(tokenizer)

        return model, tokenizer
        
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}", exc_info=True)
        raise

def main():
    # Note: This main function is deprecated. The load_model function should be accessed through mlm_inference.py
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--checkpoint_path', type=str, default="", help="Path to model checkpoint")
    parser.add_argument('-t', '--tokenizer', type=str, default="", help="Path or HuggingFace repo to tokenizer")
    
    args = parser.parse_args()
    checkpoint_path = args.checkpoint_path
    tokenizer = args.tokenizer
    
    logger.info(f"Starting model loading with checkpoint: {checkpoint_path}")
    logger.info(f"Tokenizer source: {tokenizer}")
    
    model, tokenizer = load_model(checkpoint_path, tokenizer)
    logger.info(f"Model type is: {type(model)}")
    logger.info(f"Tokenizer type is: {type(tokenizer)}")
    logger.info("Model successfully loaded")

if __name__ == "__main__":
    main()
    torch.cuda.empty_cache()
    logger.info("Script completed successfully")
    
# Example usage:
# python3 load_model_from_checkpoint.py -c "./checkpoints/modernbert-base-pretokenized-dataset-1xh100/latest-rank0.pt" -t "boun-tabilab/TabiBERT"  