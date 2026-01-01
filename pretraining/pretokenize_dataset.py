"""
Script for pretokenizing a text dataset and converting it to MDS (Mosaic Data Sharding) format.

This script:
1. Loads a text dataset from a StreamingDataset
2. Tokenizes text using a pre-trained tokenizer
3. Chunks tokenized sequences into fixed-size pieces (for training efficiency)
4. Filters out chunks that are too short
5. Writes the pretokenized chunks to a new MDS dataset

The process is parallelized using multiprocessing to speed up tokenization.
"""

import uuid
import time
import concurrent
import multiprocessing
import logging
logging.getLogger("transformers.tokenization_utils_base").setLevel(logging.ERROR)
import os
# Enable parallel tokenization within the tokenizer library
os.environ["TOKENIZERS_PARALLELISM"] = "true"

import numpy as np

from transformers import AutoTokenizer
from streaming import StreamingDataset, MDSWriter

# ============================================================================
# Configuration parameters
# ============================================================================

# Maximum sequence length for each training chunk (in tokens)
max_len = 8192
# Maximum number of tokens per example chunk (including special tokens like [CLS], [SEP])
max_num_tokens_in_an_example = max_len
# Minimum token count threshold - chunks with fewer tokens will be excluded
exclude_examples_containing_tokens_less_than = 10

dataset_name = 'TabiBERT_pretraining_data'

tokenizer = AutoTokenizer.from_pretrained('boun-tabilab/TabiBERT', verbose=False)
dataset = StreamingDataset(local=dataset_name, shuffle=False, split=None, batch_size=1, keep_zip=False)
print(f'Total number of examples in the source dataset: {len(dataset):,}')

# Define the schema for the output MDS dataset
# Each example will have: input_ids (token IDs as uint16 array), id (unique identifier), len (length in tokens)
MDS_COLS_PRE_TOKENIZED = {
    'input_ids': 'ndarray:uint16',
    'id': 'str',
    'len': 'int'
}

def get_uuid():
    """Generate a unique identifier for each chunk."""
    return str(uuid.uuid4())

def pretokenize(idx):
    """
    Tokenize a single dataset example and split it into chunks.
    
    Args:
        idx: Index of the example in the dataset
        
    Returns:
        List of dictionaries, each containing:
            - 'id': Unique identifier for the chunk
            - 'input_ids': NumPy array of token IDs (uint16)
            - 'len': Length of the chunk in tokens
    """
    # Get the text from the dataset
    text = dataset[idx]['text']
    
    input_ids = tokenizer.encode(text, add_special_tokens=True, truncation=False)
    len_input_ids = len(input_ids)

    result = []
    for i in range(0, len(input_ids), max_num_tokens_in_an_example):
        low = i
        # Ensure we don't go beyond the end of the sequence
        high = min(low + max_num_tokens_in_an_example, len_input_ids)

        # Generate unique ID for this chunk
        id_ = get_uuid()
        input_ids_ = np.array(input_ids[low:high], dtype = np.uint16)
            
        result.append({'id': id_, 'input_ids': input_ids_, 'len': input_ids_.shape[0]})
    
    return result


# ============================================================================
# Main processing: Parallel tokenization
# ============================================================================

time_begin = time.time()
dataset_indices = range(len(dataset))
results = []
num_excluded_short_chunks = 0

with concurrent.futures.ProcessPoolExecutor() as executor:
    for result in executor.map(pretokenize, dataset_indices, 
                               chunksize = len(dataset_indices) // multiprocessing.cpu_count()):
        for result_ in result:
            if result_['len'] >= exclude_examples_containing_tokens_less_than:
                results.append(result_)
            else:
                num_excluded_short_chunks += 1

time_end = time.time()
duration = (time_end - time_begin) / 60
print(f'Tokenizing {len(dataset_indices):,} examples took {duration:.2f} minutes.')
print(f'Total number of chunks in the result: {len(results):,}')
print(f'Number of excluded short chunks: {num_excluded_short_chunks:,}')


# ============================================================================
# Write results to MDS format
# ============================================================================

print('Writing tokenized chunks as MDS dataset...')
# Create a new MDS dataset with the pretokenized chunks
# Output will be saved to '{dataset_name}_pretokenized_chunks'
with MDSWriter(out=f'{dataset_name}_pretokenized_chunks', columns=MDS_COLS_PRE_TOKENIZED, compression=None) as mds_writer:
    for item in results:
        mds_writer.write(item)
