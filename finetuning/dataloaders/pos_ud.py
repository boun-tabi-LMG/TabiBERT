from torch.utils.data import Dataset
import torch

class POSUDDataset(Dataset):
    def __init__(self, dataset, tokenizer, max_length, is_lower=False):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.is_lower = is_lower
        
        # Create label mappings
        self.label_to_id = self._create_label_mapping()
        self.id_to_label = {v: k for k, v in self.label_to_id.items()}
        self.num_labels = len(self.label_to_id)
        
    def _create_label_mapping(self):
        """Create mapping from string labels to integers"""
        unique_labels = set()
        for example in self.dataset:
            unique_labels.update(example['pos_tags'])
        
        # Sort for consistency and add special tokens
        sorted_labels = sorted(list(unique_labels))
        label_to_id = {label: idx for idx, label in enumerate(sorted_labels)}
        
        return label_to_id

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        tokens = self.dataset[idx]['tokens']
        pos_tags = self.dataset[idx]['pos_tags']
        
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
                labels.append(-100)
            elif word_idx != previous_word_idx:
                labels.append(self.label_to_id[pos_tags[word_idx]])
            else:
                # mark non-first subtokens
                labels.append(-100)
            previous_word_idx = word_idx

        # Remove batch dimension and add labels
        encoding = {k: v.squeeze(0) for k, v in encoding.items()}
        encoding['labels'] = torch.tensor(labels, dtype=torch.long)
        encoding['word_ids'] = torch.tensor([-1 if w is None else w for w in word_ids])
        
        return encoding