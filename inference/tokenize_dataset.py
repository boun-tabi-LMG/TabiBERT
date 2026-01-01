"""
This script tokenizes and adds mask tokens to sample texts.
It reads a dataset from a JSON file, tokenizes the texts, and adds mask tokens, [MASK] to the texts, with provided probability.
It then writes the masked texts to a new JSON file.

Example usage:
python tokenize_dataset.py -t "boun-tabilab/TabiBERT" -d "inference_dataset/short.json" -o "inference_dataset/short_masked.json" -l 1024 -m 0.15
python tokenize_dataset.py -t "boun-tabilab/TabiBERT" -d "inference_dataset/mid.json" -o "inference_dataset/mid_masked.json" -l 1024 -m 0.15
python tokenize_dataset.py -t "boun-tabilab/TabiBERT" -d "inference_dataset/long.json" -o "inference_dataset/long_masked.json" -l 1024 -m 0.15
"""

import argparse
from utils import setup_logging
from transformers import AutoTokenizer, DataCollatorForLanguageModeling
from datasets import Dataset
from torch.utils.data import DataLoader
from typing import List, Dict, Any
import json

from read_dataset import read_json_dataset


logger = setup_logging('tokenize_dataset.py')

def main():

    parser = argparse.ArgumentParser(description="This script tokenizes and adds mask tokens to sample texts")
    parser.add_argument("--tokenizer", "-t", type=str, required=True, help="Path to the tokenizer")
    parser.add_argument("--dataset", "-d", type=str, required=True, help="Path to the dataset")
    parser.add_argument("--output", "-o", type=str, required=True, help="Path to the output dataset")
    parser.add_argument("--max_seq_len", "-l", type=int, default=512, help="Maximum sequence length")
    parser.add_argument("--mask_probability", "-m", type=float, default=0.15, help="Probability of masking each token. Used 15%, 30%, and 45%")

    args = parser.parse_args()

    tokenizer = AutoTokenizer.from_pretrained(args.tokenizer)

    mask_probability = args.mask_probability

    # if tokenizer.pad_token is None:
    #     tokenizer.pad_token = tokenizer.eos_token
    #     logger.info(f"Set pad_token to eos_token: {tokenizer.pad_token}")

    samples = read_json_dataset(args.dataset)

    dataset_dict = {}

    dataset_dict_masked = {}

    for sample in samples:
        dataset_dict[sample['id']] = sample['text']
        masked_sample = sample.copy()
        masked_sample['mask_probability'] = mask_probability
        dataset_dict_masked[sample['id']] = masked_sample
    # Convert to list of dicts (each element is one row of the dataset)
    data_list = [{"id": k, "text": v} for k, v in dataset_dict.items()]
    dataset = Dataset.from_list(data_list)

    def tokenize_fn(examples):
        # Process each text individually to maintain correct dimensions
        tokenized = tokenizer(
            examples["text"],
            truncation=True,
            max_length=args.max_seq_len,
            return_tensors=None,
            padding=False  # Explicitly set padding to False
        )
        return tokenized

    tokenized_dataset = dataset.map(
        tokenize_fn,
        batched=True,
        remove_columns=dataset.column_names  # Remove original columns after tokenization
    )

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=True,
        mlm_probability=mask_probability,
        random_replace_prob=0.0
    )

    train_dataloader = DataLoader(
        tokenized_dataset,
        shuffle=False,  # Don't shuffle to maintain order
        batch_size=8,
        collate_fn=data_collator,
    )

    batch = next(iter(train_dataloader))
    input_ids = batch['input_ids']
    labels = batch['labels']

    masked_texts = []
    
    # Create a mapping of original indices to their positions in the batch
    original_indices = list(dataset_dict.keys())
    
    for idx, sample_id in enumerate(original_indices):
        if idx < len(input_ids):  # Make sure we don't go out of bounds
            sample = dataset_dict_masked[sample_id]
            decoded_text = tokenizer.decode(input_ids[idx])
            sep_idx = decoded_text.find('[PAD]')
            # Remove the trailing [PAD] tokens:
            sample['masked_text'] = decoded_text[:sep_idx] if sep_idx != -1 else decoded_text
            masked_texts.append(sample)

    # Now: Write the masked_texts to the output json file:
    with open(args.output, "a", encoding='utf-8') as f:
        json.dump(masked_texts, f, indent=4, ensure_ascii=False)



if __name__ == "__main__":
    main()
    logger.info("Script completed successfully")
