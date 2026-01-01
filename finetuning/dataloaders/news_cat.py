from torch.utils.data import Dataset
import torch

# Define a custom dataset class
class NewsCatDataset(Dataset):
    def __init__(self, dataset, tokenizer, max_length, label2id, is_lower=False):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.label2id = label2id
        self.is_lower = is_lower
        
    def __len__(self):
        return len(self.dataset)
        
    def __getitem__(self, idx):
        item = self.dataset[idx]
        text = item['text']
        label_str = item['label']
        label = self.label2id[label_str]  # convert string label to int
        if self.is_lower:
            text = text.replace("I", "ı").lower()
            label_str = label_str.replace("I", "ı").lower()
            
        encoding = self.tokenizer(
            text=text,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        
        return {
            'input_ids': encoding['input_ids'].squeeze(),
            'attention_mask': encoding['attention_mask'].squeeze(),
            'label': torch.tensor(label, dtype=torch.long),
            'text': text 
        }