from torch.utils.data import Dataset
import torch

class XtremeQADataset(Dataset):
    def __init__(self, dataset, tokenizer, max_length):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        example = self.dataset[idx]
        context = example['context']
        question = example['question']
        answers = example['answers']
        
        # Tokenize with return_overflowing_tokens to handle long contexts
        encoding = self.tokenizer(
            question,
            context,
            truncation='only_second',
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt',
            return_offsets_mapping=True,
            return_overflowing_tokens=False  # Set to True if you want to handle overflow
        )
        
        offset_mapping = encoding['offset_mapping'].squeeze(0)
        
        # Find answer positions
        start_position = 0
        end_position = 0
        answer_found = False
        
        if answers['answer_start'] and answers['text']:
            answer_start = answers['answer_start'][0]
            answer_text = answers['text'][0]
            answer_end = answer_start + len(answer_text)
            
            for i, (start_offset, end_offset) in enumerate(offset_mapping):
                if start_offset == 0 and end_offset == 0:
                    continue
                    
                if not answer_found and start_offset <= answer_start < end_offset:
                    start_position = i
                    answer_found = True
                    
                if answer_found and start_offset < answer_end <= end_offset:
                    end_position = i
                    break
            
            # If answer wasn't found in truncated context, set to CLS token (position 0)
            if not answer_found:
                start_position = 0
                end_position = 0
        
        # Clean up encoding
        encoding = {k: v.squeeze(0) for k, v in encoding.items() if k != 'offset_mapping'}
        
        encoding['start_positions'] = torch.tensor(start_position, dtype=torch.long)
        encoding['end_positions'] = torch.tensor(end_position, dtype=torch.long)
        encoding['example_id'] = example.get('id', idx)
        
        return encoding