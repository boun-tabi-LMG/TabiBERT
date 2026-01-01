import torch
import os
from typing import Union
from transformers import AutoTokenizer
from transformers import (AutoTokenizer, PreTrainedTokenizer,
                          PreTrainedTokenizerFast)

Tokenizer = Union[PreTrainedTokenizer, PreTrainedTokenizerFast]

def build_local_tokenizer(tokenizer_path: str) -> Tokenizer:
    """Build tokenizer from local files"""
    os.environ['TRANSFORMERS_NO_ADVISORY_WARNINGS'] = '1'
    os.environ['TOKENIZERS_PARALLELISM'] = 'false'

    if not os.path.exists(tokenizer_path):
        raise ValueError(f"Tokenizer path does not exist: {tokenizer_path}")
    
    required_files = ['tokenizer_config.json', 'special_tokens_map.json']
    for file in required_files:
        if not os.path.exists(os.path.join(tokenizer_path, file)):
            raise ValueError(f"Missing required tokenizer file: {file}")

    try:
        # Load the tokenizer from local files
        tokenizer = AutoTokenizer.from_pretrained(
            tokenizer_path,
            local_files_only=True
        )
        
        # Set model max length from config or default to a large value
        tokenizer.model_max_length = getattr(tokenizer, 'model_max_length', int(1e30))

        # Ensure all special tokens are set
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
            logger.info(f"Set pad_token to eos_token: {tokenizer.pad_token}")

        return tokenizer

    except Exception as e:
        raise RuntimeError(f"Failed to load tokenizer from {tokenizer_path}: {str(e)}")
