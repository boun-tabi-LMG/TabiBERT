"""
This script reads a JSON file containing text samples with metadata.
It validates the format of the JSON file and returns a list of dictionaries containing text samples and their metadata.

Example usage if you want to print the texts from the json dataset to a markdown file:
python read_dataset.py -p "inference_dataset/short_masked.json" > short_masked_check.md
"""

import torch
import json
import argparse
from datetime import timedelta
from typing import List, Dict, Any
from utils import setup_logging

# Set up logging
logger = setup_logging('read_dataset.py')

def read_json_dataset(file_path: str) -> List[Dict[str, Any]]:
    """
    Read a JSON file containing text samples with metadata.
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        List[Dict[str, Any]]: List of dictionaries containing text samples and their metadata
        
    Example format:
    [
        {
            "id": "0000",
            "domain": "web",
            "language": "tr",
            "length": "short",
            "mask_probability": 0,
            "text": "Sample text here..."
        },
        ...
    ]
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if not isinstance(data, list):
            raise ValueError("JSON file must contain a list of samples")
            
        # Validate each sample has required fields
        required_fields = ['id', 'domain', 'language', 'length', 'mask_probability', 'text']  # 'masked_text'
        for i, sample in enumerate(data):
            missing_fields = [field for field in required_fields if field not in sample]
            if missing_fields:
                raise ValueError(f"Sample {i} is missing required fields: {missing_fields}")
                
        logger.info(f"Successfully loaded {len(data)} samples from {file_path}")
        return data
        
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON file: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {str(e)}")
        raise


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--text_path', type=str, default="", help="Path to the JSON file containing text samples")
    
    args = parser.parse_args()

    data = read_json_dataset(args.text_path)


    for sample in data:
        print(f"## ID: {sample['id']} & domain: {sample['domain']} & language: {sample['language']} & mlm_probability: {sample['mask_probability']} :\n\n{sample['masked_text']}\n\n")

if __name__ == "__main__":
    main()
