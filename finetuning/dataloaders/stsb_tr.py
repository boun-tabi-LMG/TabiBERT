from torch.utils.data import Dataset as TorchDataset
import torch
import os
import pandas as pd
import re
import json
import numpy as np
from datasets import Dataset, DatasetDict

class STSDataset(TorchDataset):
    def __init__(self, dataset, tokenizer, max_length, is_lower):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.is_lower = is_lower
        
    def __len__(self):
        return len(self.dataset)
        
    def __getitem__(self, idx):
        item = self.dataset[idx]
        sentence1 = item['sentence1']
        sentence2 = item['sentence2']
        score = item['score']

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
            'labels': torch.tensor(score, dtype=torch.float),  # Changed to float for regression
        }


# STS-B dataset reader - TSV format with HF Dataset objects
class STSBReader():
    def __init__(self, filepath):
        self.filepath = filepath
        self.filename = {}
        self.filename['train'] = 'stsb_tr_train.tsv'
        self.filename['dev'] = 'stsb_tr_dev.tsv'
        self.filename['test'] = 'stsb_tr_test.tsv'
    
    def get_data(self, data_split):
        """Read data from TSV file for a specific split"""
        filepath = os.path.join(self.filepath, self.filename[data_split])
        
        # Read TSV file with error handling for malformed rows
        try:
            # First, try to read normally
            df = pd.read_csv(filepath, sep='\t', header=None)
        except pd.errors.ParserError:
            # If that fails, read with error handling
            print(f"Warning: Found malformed rows in {data_split} split, attempting to fix...")
            
            # Read line by line to handle problematic rows
            valid_rows = []
            with open(filepath, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    try:
                        # Split by tab and check if we have reasonable number of columns
                        columns = line.strip().split('\t')
                        
                        # Skip empty lines
                        if not line.strip():
                            continue
                            
                        # Handle different expected formats
                        if len(columns) >= 3:  # Minimum: sentence1, sentence2, score
                            valid_rows.append(columns)
                        else:
                            print(f"Skipping malformed line {line_num}: insufficient columns ({len(columns)})")
                            
                    except Exception as e:
                        print(f"Skipping problematic line {line_num}: {str(e)}")
                        continue
            
            if not valid_rows:
                raise ValueError(f"No valid rows found in {filepath}")
            
            # Create DataFrame from valid rows
            df = pd.DataFrame(valid_rows)
            print(f"Successfully processed {len(df)} valid rows from {data_split} split")
        
        # Extract columns based on STS-B format
        # STS-B format: [genre, filename, year, id, score, sentence1, sentence2]
        # [genre, dataset, year, sid, score, sentence1, sentence2]
        if len(df.columns) >= 7:
            # Full format with metadata
            genre = df.iloc[:, 0].tolist()[1:]
            dataset = df.iloc[:, 1].tolist()[1:]
            year = df.iloc[:, 2].tolist()[1:]
            sid = df.iloc[:, 3].tolist()[1:]
            scores = df.iloc[:, 4].tolist()[1:]
            sentence1 = df.iloc[:, 5].tolist()[1:]
            sentence2 = df.iloc[:, 6].tolist()[1:]
            
        # Convert scores to float and handle missing values
        scores = [float(score) if pd.notna(score) else 0.0 for score in scores]
        return sid, sentence1, sentence2, scores, year
    
    def get_all_splits(self):
        """Get all dataset splits at once as raw data"""
        splits_data = {}
        
        for split in ['train', 'dev', 'test']:
            try:
                id, sentence1, sentence2, scores, year = self.get_data(split)
                splits_data[split] = {
                    'id': id,
                    'sentence1': sentence1,
                    'sentence2': sentence2,
                    'scores': scores,
                    'year': year
                }
            except FileNotFoundError:
                print(f"Warning: {self.filename[split]} not found, skipping {split} split")
                continue
        
        return splits_data
    
    def get_datasets(self):
        """Get all splits as Hugging Face Dataset objects"""
        dataset_dict = {}
        
        for split in ['train', 'dev', 'test']:
            try:
                id, sentence1, sentence2, scores, year = self.get_data(split)
                
                # Create dataset from dictionary
                dataset = Dataset.from_dict({
                    'id': id,
                    'sentence1': sentence1,
                    'sentence2': sentence2,
                    'score': scores,
                    'year': year
                })
                
                dataset_dict[split] = dataset
                
            except FileNotFoundError:
                print(f"Warning: {self.filename[split]} not found, skipping {split} split")
                continue
        
        # Return as DatasetDict for easy access
        return DatasetDict(dataset_dict)
    
    def get_single_dataset(self, split):
        """Get a single split as Dataset object"""
        id, sentence1, sentence2, scores, year = self.get_data(split)
        
        return Dataset.from_dict({
            'id': id,
            'sentence1': sentence1,
            'sentence2': sentence2,
            'score': scores,
            'year': year
        })



# SICK-dataset reader - Modified to get all splits
class SICKReader():  
    def __init__(self, filepath):
        self.filepath = filepath
        self.filename = {}
        self.filename['train'] = 'SICK_train_tr.txt'
        self.filename['test']  = 'SICK_test_tr.txt'
        self.filename['trial'] = 'SICK_trial_tr.txt'
        self.label2index = {'CONTRADICTION': 0 , 'NEUTRAL': 1 ,  'ENTAILMENT': 2}

    def get_data(self, data_split):
        id, x1, x2, annotator_labels, scores, labels, all_data = [], [], [], [], [], [], []
        
        with open(os.path.join(self.filepath, self.filename[data_split]), 'r') as f:
            next(f)  # Skip header
            for line in f:
                line = line.rstrip().split("\t")
                id.append(line[0])
                x1.append(line[1])
                x2.append(line[2])
                labels.append(self.label2index[line[4]])
                scores.append(float(line[3]))
                annotator_labels.append(line[4])

            [all_data.append([id[i], x1[i], x2[i], labels[i], scores[i], annotator_labels[i]]) for i in range(len(id))]

        return id, x1, x2, labels, scores, annotator_labels, all_data

    def get_all_splits(self):
        """Get all dataset splits at once"""
        splits_data = {}
        
        for split in ['train', 'test', 'trial']:
            id, x1, x2, labels, scores, annotator_labels, all_data = self.get_data(split)
            splits_data[split] = {
                'id': id,
                'sentence_1': x1,
                'sentence_2': x2,
                'labels': labels,
                'scores': scores,
                'annotator_labels': annotator_labels,
                'all_data': all_data
            }
        
        return splits_data

    def get_datasets(self):
        """Get all splits as Hugging Face Dataset objects"""
        dataset_dict = {}
        
        for split in ['train', 'test', 'trial']:
            id, x1, x2, labels, scores, annotator_labels, all_data = self.get_data(split)
            
            # Create dataset from dictionary
            dataset = Dataset.from_dict({
                'id': id,
                'sentence1': x1,
                'sentence2': x2,
                'label': labels,
                'score': scores,
                'entailment_label': annotator_labels
            })
            
            dataset_dict[split] = dataset
        
        # Return as DatasetDict for easy access
        return DatasetDict(dataset_dict)
    
    def get_single_dataset(self, split):
        """Get a single split as Dataset object"""
        id, x1, x2, labels, scores, annotator_labels, all_data = self.get_data(split)
        
        return Dataset.from_dict({
            'id': id,
            'sentence1': x1,
            'sentence2': x2,
            'label': labels,
            'score': scores,
            'entailment_label': annotator_labels
        })

    def get_label2index(self):
        return self.label2index 