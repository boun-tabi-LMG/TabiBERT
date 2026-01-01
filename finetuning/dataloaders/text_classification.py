from torch.utils.data import Dataset
import torch

# Define a custom dataset class
class TextClassificationDataset(Dataset):
    def __init__(self, dataset, tokenizer, max_length, is_lower=False):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.is_lower = is_lower
        
    def __len__(self):
        return len(self.dataset)
        
    def __getitem__(self, idx):
        item = self.dataset[idx]
        text = item['text']
        label = item['label']
        if self.is_lower:
            text = text.replace("I", "ı").lower()
            
        # Tokenize the text
        encoding = self.tokenizer(
            text,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        
        return {
            'input_ids': encoding['input_ids'].squeeze(),
            'attention_mask': encoding['attention_mask'].squeeze(),
            'text': text,
            'label': torch.tensor(label, dtype=torch.long),
            'labels': int(label),  # for analysis
        }