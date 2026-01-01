"""
Turkish BERT Masking Benchmark Recreation - FIXED VERSION

Required installations:
pip install torch transformers datasets tqdm numpy

Usage:
python inference_across_models.py
"""

import torch
import json
from datetime import timedelta
from typing import List, Dict, Any
from transformers import AutoTokenizer, AutoModelForMaskedLM
from datasets import load_dataset
from utils import setup_logging
from torch.utils.data import Dataset, DataLoader
import random
import numpy as np
from tqdm import tqdm
from load_model_from_checkpoint import load_model

# Enable TF32 for better performance on Ampere GPUs
torch.set_float32_matmul_precision('high')

# Set up logging
logger = setup_logging('inference_across_models.py')

# Add timedelta to safe globals
torch.serialization.add_safe_globals([timedelta])

SAMPLE_SIZE = 2500


class MaskingDataset(Dataset):

    def __init__(self, texts: List[str], tokenizer, mask_probability: float, uncased: bool = True):
        self.texts = texts
        self.tokenizer = tokenizer
        self.mask_probability = mask_probability
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.uncased = uncased

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        
        # Consistent preprocessing for Turkish uncased models
        if self.uncased:
            text = text.replace("I", "ı").lower()

        # Tokenize the text
        encoding = self.tokenizer(
            text,
            truncation=True,
            max_length=512,
            padding='max_length',
            return_tensors="pt"
        )
        
        input_ids = encoding["input_ids"][0].to(self.device)
        attention_mask = encoding["attention_mask"][0].to(self.device)

        # Create labels (copy of input_ids)
        labels = input_ids.clone()

        # Create probability matrix for masking based on self.mask_probability (5%, 10%, or 15%)
        probability_matrix = torch.full(labels.shape, self.mask_probability, device=self.device)

        # Create special tokens mask
        special_tokens_mask = torch.zeros_like(labels, dtype=torch.bool, device=self.device)
        
        # Mark special tokens
        special_token_ids = {
            self.tokenizer.cls_token_id,
            self.tokenizer.sep_token_id, 
            self.tokenizer.pad_token_id,
            self.tokenizer.unk_token_id
        }
        
        for i, token_id in enumerate(labels):
            if token_id.item() in special_token_ids:
                special_tokens_mask[i] = True

        # Don't mask special tokens or padding
        probability_matrix.masked_fill_(special_tokens_mask, value=0.0)
        probability_matrix.masked_fill_(attention_mask == 0, value=0.0)

        # Get indices to mask based on the experiment's mask probability
        masked_indices = torch.bernoulli(probability_matrix).bool()
        
        # Ensure at least one token is masked if possible
        if masked_indices.sum() == 0:
            valid_positions = (attention_mask == 1) & (~special_tokens_mask)
            if valid_positions.sum() > 0:
                valid_indices = torch.where(valid_positions)[0]
                random_idx = torch.randint(0, len(valid_indices), (1,), device=self.device)
                masked_indices[valid_indices[random_idx]] = True

        # Set labels to -100 for non-masked tokens
        labels[~masked_indices] = -100

        # Option 1: Replace all masked tokens with [MASK] token
        input_ids[masked_indices] = self.tokenizer.mask_token_id

        # # Option 2: Replace 80% of the masked tokens with [MASK] token
        # indices_replaced = torch.bernoulli(
        #     torch.full(labels.shape, 0.8, device=self.device)
        # ).bool() & masked_indices
        # input_ids[indices_replaced] = self.tokenizer.mask_token_id

        # Remaining 20%: keep original token (no action needed)

        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "labels": labels
        }


def calculate_masking_accuracy(model, dataloader, device):
    model.eval()
    correct_predictions = 0
    total_predictions = 0

    with torch.no_grad():
        for batch in tqdm(dataloader, desc="Evaluating"):
            # Move batch to device
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["labels"].to(device)

            # Get model predictions
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            logits = outputs.logits

            # Get predictions for masked tokens
            masked_indices = (labels != -100)
            
            if masked_indices.sum() == 0:
                continue
                
            masked_logits = logits[masked_indices]
            masked_labels = labels[masked_indices]

            # Get top predictions
            top_predictions = torch.argmax(masked_logits, dim=-1)

            # Calculate accuracy
            correct_predictions += (top_predictions == masked_labels).sum().item()
            total_predictions += masked_labels.numel()

    return (correct_predictions / total_predictions) * 100 if total_predictions > 0 else 0


def load_datasets_from_hf(datasets: Dict[str, str]):
    """
    Load Turkish datasets from Hugging Face Hub
    Based on the exact datasets mentioned in the benchmark
    """
    loaded_datasets = {}

    for dataset_name, dataset_path in datasets.items():
        logger.info(f"Loading {dataset_name} dataset...")
        try:
            # Load dataset with error handling
            dataset = load_dataset(dataset_path, split=f"train[:{SAMPLE_SIZE}]")
            texts = []
            
            for item in dataset:
                text_content = None
                
                # Try different field names
                if 'instruction' in item and 'output' in item:
                    text_content = item['instruction'] + " " + item['output']
                elif 'text' in item:
                    text_content = item['text']
                elif 'sentence' in item:
                    text_content = item['sentence']
                elif 'review' in item:
                    text_content = item['review']
                elif 'content' in item:
                    text_content = item['content']
                elif 'question' in item and 'answer' in item:
                    text_content = item['question'] + " " + item['answer']
                
                # Add text if it's valid and not too short
                if text_content and len(text_content.strip()) > 10:
                    texts.append(text_content.strip())
                    
            logger.info(f"✅ Loaded {len(texts)} examples")
            loaded_datasets[dataset_name] = texts
            
        except Exception as e:
            logger.error(f"  Could not load {dataset_name}: {e}")
            loaded_datasets[dataset_name] = []

    return loaded_datasets


def run_checkpoint_benchmark(
    checkpoint_model_instance,
    checkpoint_tokenizer,
    loaded_datasets,
    mlm_probabilities,
    device,
    model_name,
    uncased: bool = True
):
    mode = "uncased" if uncased else "cased"
    logger.info(f"\nTesting checkpoint model: {model_name} ({mode})")
    checkpoint_results = {}
    result_key = f"{model_name}-{mode}"
    checkpoint_results[result_key] = {}

    for dataset_name, texts in loaded_datasets.items():
        if not texts:
            logger.info(f"   Dataset {dataset_name} is skipped (empty)!")
            continue

        logger.info(f"  Dataset: {dataset_name} ({len(texts)} examples)")
        checkpoint_results[result_key][dataset_name] = {}

        for mask_pct in mlm_probabilities:
            logger.info(f"    Mask percentage: {mask_pct*100}%")
            try:
                dataset = MaskingDataset(texts, checkpoint_tokenizer, mask_pct, uncased=uncased)
                dataloader = DataLoader(dataset, batch_size=8, shuffle=False)
                accuracy = calculate_masking_accuracy(checkpoint_model_instance, dataloader, device)
                checkpoint_results[result_key][dataset_name][f"{int(mask_pct*100)}%"] = accuracy
                logger.info(f"      Accuracy: {accuracy:.2f}%")
            except Exception as e:
                logger.error(f"      Error with {mask_pct*100}% masking: {e}")
                checkpoint_results[result_key][dataset_name][f"{int(mask_pct*100)}%"] = 0.0
    return checkpoint_results


def run_inference_benchmark(models: Dict[str, str],
                            datasets: Dict,
                            mlm_probabilities: List = [0.05, 0.10, 0.15]):
    results = {}
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    logger.info(f"Using device: {device}")

    for model_name, model_path in models.items():
        logger.info(f"\nTesting model: {model_path}")
        try:
            # Load model and tokenizer
            model = AutoModelForMaskedLM.from_pretrained(model_path)
            tokenizer = AutoTokenizer.from_pretrained(model_path)
            
            # Ensure we have a mask token
            if tokenizer.mask_token is None:
                logger.error(f"Model {model_path} tokenizer has no mask token!")
                continue
                
            model.to(device)
            results[model_name] = {}

            for dataset_name, texts in datasets.items():
                if not texts:  # Skip empty datasets
                    logger.info(f"   Dataset {dataset_name} is skipped (empty)!")
                    continue

                logger.info(f"  Dataset: {dataset_name} ({len(texts)} examples)")
                results[model_name][dataset_name] = {}

                for mask_pct in mlm_probabilities:
                    logger.info(f"    Mask percentage: {mask_pct*100}%")

                    try:
                        # Create dataset and dataloader
                        dataset = MaskingDataset(texts, tokenizer, mask_pct)
                        dataloader = DataLoader(dataset,
                                              batch_size=8,  # Reduced batch size
                                              shuffle=False)

                        # Calculate accuracy
                        accuracy = calculate_masking_accuracy(model, dataloader, device)
                        results[model_name][dataset_name][f"{int(mask_pct*100)}%"] = accuracy

                        logger.info(f"      Accuracy: {accuracy:.2f}%")
                        
                    except Exception as e:
                        logger.error(f"      Error with {mask_pct*100}% masking: {e}")
                        results[model_name][dataset_name][f"{int(mask_pct*100)}%"] = 0.0
                        
        except Exception as e:
            logger.error(f"Error processing model {model_name}: {e}")
            continue

    return results


def print_results_table(results):
    print("\n" + "="*110)
    print("BENCHMARK RESULTS")
    print("="*110)

    if not results:
        print("No results to display!")
        return

    # Get all datasets and models
    all_datasets = set()
    all_models = list(results.keys())
    for model_results in results.values():
        all_datasets.update(model_results.keys())
    all_datasets = sorted(list(all_datasets))
    mask_levels = ['5%', '10%', '15%']

    # Shorten model names for header
    model_headers = [model.split('/')[-1] for model in all_models]

    # Print header
    header = f"{'Dataset':<20} {'Mask':<5} | " + " | ".join([f"{m:<22}" for m in model_headers])
    print(header)
    print("-" * len(header))

    # Print each dataset-mask combination as a row
    for dataset in all_datasets:
        for mask in mask_levels:
            dataset_name = dataset.split('/')[-1]
            row = f"{dataset_name:<20} {mask:<5} "
            for model in all_models:
                accuracy = results.get(model, {}).get(dataset, {}).get(mask, 'N/A')
                if isinstance(accuracy, float):
                    row += f"| {accuracy:<22.2f}"
                else:
                    row += f"| {str(accuracy):<22}"
            print(row)
        print("-" * len(header))

if __name__ == "__main__":
    datasets = {
        "QA Dataset": "blackerx/turkish_v2",
        "Review Dataset": "fthbrmnby/turkish_product_reviews", 
        "Biomedical Dataset": "hazal/Turkish-Biomedical-corpus-trM",
    }

    # Define models including the checkpoint model
    models = {
        "YTU BERT" : "ytu-ce-cosmos/turkish-base-bert-uncased",
        "DBMDZ BERTurk" : "dbmdz/bert-base-turkish-uncased"
    }

    # Add checkpoint model
    checkpoint_model = {
        "name": "TabiBERT",
        "checkpoint_path": "/workspace/pretraining_checkpoints/modernbert-base-learning-rate-decay/latest-rank0.pt",
        "tokenizer": "boun-tabilab/TabiBERT"
    }

    mlm_probabilities = [0.05, 0.10, 0.15]

    logger.info("📥 Loading datasets from Hugging Face Hub...")
    loaded_datasets = load_datasets_from_hf(datasets)
    logger.info("✅ All datasets loaded.\n")

    # Load checkpoint model
    logger.info(f"Loading checkpoint model from {checkpoint_model['checkpoint_path']}")
    checkpoint_model_instance, checkpoint_tokenizer = load_model(
        checkpoint_model['checkpoint_path'],
        checkpoint_model['tokenizer']
    )
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    checkpoint_model_instance = checkpoint_model_instance.to(device)
    logger.info("✅ Checkpoint model loaded.\n")

    # Run benchmark for HuggingFace models
    results = run_inference_benchmark(models, loaded_datasets, mlm_probabilities)

    # Run benchmark for checkpoint model (uncased)
    checkpoint_results_uncased = run_checkpoint_benchmark(
        checkpoint_model_instance,
        checkpoint_tokenizer,
        loaded_datasets,
        mlm_probabilities,
        device,
        checkpoint_model['name'],
        uncased=True
    )

    # Run benchmark for checkpoint model (cased)
    checkpoint_results_cased = run_checkpoint_benchmark(
        checkpoint_model_instance,
        checkpoint_tokenizer,
        loaded_datasets,
        mlm_probabilities,
        device,
        checkpoint_model['name'],
        uncased=False
    )

    # Merge results
    results.update(checkpoint_results_uncased)
    results.update(checkpoint_results_cased)

    
    logger.info("🏁 Benchmarking completed.\n")
    # Print results in table format
    print_results_table(results)
    
    # Save results to file
    logger.info("📤 Saving results to 'benchmark_results.json'...")
    with open('benchmark_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    logger.info("✅ Results successfully saved to 'benchmark_results.json'.")