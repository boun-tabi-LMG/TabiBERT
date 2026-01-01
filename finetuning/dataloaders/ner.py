from torch.utils.data import Dataset
import torch

# Define a custom dataset class
class NERDataset(Dataset):
    def __init__(self, dataset, tokenizer, tag2id, max_length, is_lower=False):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.tag2id = tag2id
        self.max_length = max_length
        self.is_lower = is_lower

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        tokens = self.dataset[idx]['tokens']
        tags = self.dataset[idx]['tags']

        if self.is_lower:
            for i in range(len(tokens)):
                tokens[i] = tokens[i].replace("I", "ı").lower()

        encoding = self.tokenizer(
            tokens,
            is_split_into_words=True,
            truncation=True,
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt'
        )
        word_ids = encoding.word_ids(batch_index=0)
        labels = []
        previous_word_idx = None
    
        for word_idx in word_ids:
            if word_idx is None:
                # Padding or special tokens
                labels.append(-100)
            elif word_idx != previous_word_idx:
                # First subtoken of the word → assign label
                labels.append(self.tag2id[tags[word_idx]])
            else:
                # Subsequent subtoken of the same word → ignore
                labels.append(-100)
            previous_word_idx = word_idx

        # Convert everything to the right format
        encoding = {k: v.squeeze(0) for k, v in encoding.items()}
        encoding['labels'] = torch.tensor(labels)
        encoding['word_ids'] = torch.tensor(
            [-1 if w is None else w for w in word_ids]
        )  # -1 for special tokens, else word index

        return encoding
        
        
        
