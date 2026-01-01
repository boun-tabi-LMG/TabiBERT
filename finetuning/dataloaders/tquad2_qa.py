from torch.utils.data import Dataset
import torch

class TquadQADataset(Dataset):
    def __init__(self, dataset, tokenizer, max_length, include_title=True):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.include_title = include_title

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        example = self.dataset[idx]
        context = example['context']
        question = example['question']
        title = example.get('title', '')
        answers = example['answers']
        
        # Prepare the text sequence based on whether to include title
        if self.include_title and title:
            # Format: [CLS] question [SEP] title [SEP] context [SEP]
            # This gives the model access to the title as additional context
            text_b = f"{title} {self.tokenizer.sep_token} {context}"
        else:
            text_b = context
        
        # Tokenize with return_overflowing_tokens to handle long contexts
        encoding = self.tokenizer(
            question,
            text_b,
            truncation='only_second',
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt',
            return_offsets_mapping=True,
            return_overflowing_tokens=False
        )
        
        offset_mapping = encoding['offset_mapping'].squeeze(0)
        
        # Find answer positions
        start_position = 0
        end_position = 0
        answer_found = False
        
        # Handle the answer structure - it's a list of dicts with answer_start and text
        if answers and len(answers) > 0:
            answer_start = answers[0]['answer_start']
            answer_text = answers[0]['text']
            answer_end = answer_start + len(answer_text)
            
            # Calculate offset adjustment if title is included
            title_offset = 0
            if self.include_title and title:
                # Account for "title [SEP] " prefix in text_b
                title_offset = len(title) + len(self.tokenizer.sep_token) + 1
            
            # Adjust answer positions for the title offset
            adjusted_answer_start = answer_start + title_offset
            adjusted_answer_end = answer_end + title_offset
            
            for i, (start_offset, end_offset) in enumerate(offset_mapping):
                if start_offset == 0 and end_offset == 0:
                    continue
                    
                if not answer_found and start_offset <= adjusted_answer_start < end_offset:
                    start_position = i
                    answer_found = True
                    
                if answer_found and start_offset < adjusted_answer_end <= end_offset:
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
        encoding['title'] = title  # Include title in the output for reference
        
        return encoding


class TquadQADataset2(Dataset):
    """
    Alternative implementation where title is tokenized separately
    and concatenated at the token level rather than text level
    """
    def __init__(self, dataset, tokenizer, max_length, title_max_length=64):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.title_max_length = title_max_length

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        example = self.dataset[idx]
        context = example['context']
        question = example['question']
        title = example.get('title', '')
        answers = example['answers']
        
        # Tokenize title separately if provided
        title_tokens = []
        if title:
            title_encoding = self.tokenizer(
                title,
                truncation=True,
                max_length=self.title_max_length,
                add_special_tokens=False
            )
            title_tokens = title_encoding['input_ids']
        
        # Calculate available length for question + context
        available_length = self.max_length - len(title_tokens) - 3  # Account for [CLS], [SEP], [SEP]
        
        # Tokenize question and context
        encoding = self.tokenizer(
            question,
            context,
            truncation='only_second',
            max_length=available_length,
            add_special_tokens=False,
            return_offsets_mapping=True
        )
        
        # Manually construct the final sequence: [CLS] question [SEP] title [SEP] context [SEP]
        input_ids = [self.tokenizer.cls_token_id]
        attention_mask = [1]
        token_type_ids = [0]
        
        # Add question tokens
        question_tokens = self.tokenizer(question, add_special_tokens=False)['input_ids']
        input_ids.extend(question_tokens)
        attention_mask.extend([1] * len(question_tokens))
        token_type_ids.extend([0] * len(question_tokens))
        
        # Add first SEP
        input_ids.append(self.tokenizer.sep_token_id)
        attention_mask.append(1)
        token_type_ids.append(0)
        
        # Add title tokens if present
        title_start_idx = len(input_ids)
        if title_tokens:
            input_ids.extend(title_tokens)
            attention_mask.extend([1] * len(title_tokens))
            token_type_ids.extend([1] * len(title_tokens))
            
            # Add SEP after title
            input_ids.append(self.tokenizer.sep_token_id)
            attention_mask.append(1)
            token_type_ids.append(1)
        
        # Add context tokens
        context_start_idx = len(input_ids)
        context_tokens = encoding['input_ids'][len(question_tokens)+1:]  # Skip question and first SEP
        input_ids.extend(context_tokens)
        attention_mask.extend([1] * len(context_tokens))
        token_type_ids.extend([1] * len(context_tokens))
        
        # Pad to max_length
        padding_length = self.max_length - len(input_ids)
        input_ids.extend([self.tokenizer.pad_token_id] * padding_length)
        attention_mask.extend([0] * padding_length)
        token_type_ids.extend([0] * padding_length)
        
        # Find answer positions in context
        start_position = 0
        end_position = 0
        
        if answers and len(answers) > 0:
            answer_start = answers[0]['answer_start']
            answer_text = answers[0]['text']
            answer_end = answer_start + len(answer_text)
            
            # Map to token positions (this is simplified - you might need more robust mapping)
            # For now, set to context start if answer exists
            if answer_text in context:
                start_position = context_start_idx
                end_position = context_start_idx + min(len(context_tokens) - 1, 10)  # Approximate
        
        result = {
            'input_ids': torch.tensor(input_ids, dtype=torch.long),
            'attention_mask': torch.tensor(attention_mask, dtype=torch.long),
            'token_type_ids': torch.tensor(token_type_ids, dtype=torch.long),
            'start_positions': torch.tensor(start_position, dtype=torch.long),
            'end_positions': torch.tensor(end_position, dtype=torch.long),
            'example_id': example.get('id', idx),
            'title': title
        }
        
        return result