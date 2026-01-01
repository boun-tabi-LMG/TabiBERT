import json
import os
from typing import Dict, List, Optional, Union

import torch
from torch.utils.data import Dataset
from transformers import PreTrainedTokenizer


# Define a custom dataset class for SNLI
class NLIDataset(Dataset):
    def __init__(self, dataset, tokenizer, max_length, is_lower=False):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.is_lower = is_lower
        
    def __len__(self):
        return len(self.dataset)
        
    def __getitem__(self, idx):
        item = self.dataset[idx]
        sentence1 = item['premise']
        sentence2 = item['hypothesis']
        label = item['label']

        if self.is_lower:
            sentence1 = sentence1.replace("I", "ı").lower()
            sentence2 = sentence2.replace("I", "ı").lower()
        
        # Tokenize the sentence pair
        encoding = self.tokenizer(
            sentence1,
            sentence2,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        
        return {
            'input_ids': encoding['input_ids'].squeeze(),
            'attention_mask': encoding['attention_mask'].squeeze(),
            'labels': torch.tensor(label, dtype=torch.long)
        }