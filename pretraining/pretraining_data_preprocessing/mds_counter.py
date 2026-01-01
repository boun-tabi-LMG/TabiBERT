import os
import json
from streaming import StreamingDataset
from collections import deque

def fast_count_samples(dir_path: str) -> int:
    """
    Quickly counts the number of samples in a streaming dataset by reading index.json.

    Args:
        dir_path (str): Path to the dataset directory containing index.json.

    Returns:
        int: Total number of samples.
    """
    index_path = os.path.join(dir_path, "index.json")
    if not os.path.exists(index_path):
        raise FileNotFoundError(f"index.json not found in {dir_path}")

    with open(index_path, "r") as f:
        index = json.load(f)

    total_samples = sum(shard.get("samples", 0) for shard in index.get("shards", []))
    return total_samples


def analyze_dataset(dir_path: str, example_numbers : int = 3, batch_size: int = 1):
    """
    Analyzes a StreamingDataset by printing the total number of samples,
    the first 3 samples, and the last 3 samples.

    Parameters:
        dir_path (str): Path to the dataset directory.
        batch_size (int): Batch size for StreamingDataset (default is 1).
    """
    dataset = StreamingDataset(local=dir_path, batch_size=batch_size)

    sample_count = 0
    first_samples = []
    last_samples = deque(maxlen=example_numbers)

    print(f"## {dir_path}: ", end='')

    for sample in dataset:
        sample_count += 1
        if sample_count <= example_numbers:
            first_samples.append(sample)
        last_samples.append(sample)

        if sample_count % 10000 == 0:
            print(f'sample count: {sample_count}')

    print(f"{sample_count} samples\n")

    print(f"📌 First and last {example_numbers} samples:")
    for i, sample in enumerate(first_samples, 1):
        sample_str = str(sample)[:1000]
        print(f"\n{i}: {sample_str}...")

    for i, sample in enumerate(last_samples, sample_count - len(last_samples) + 1):
        sample_str = str(sample)[:1000]
        print(f"\n{i}: {sample_str}...")


def validate_merged_dataset(dir_path: str, examples_to_print: list, batch_size: int = 1) -> None:
    index_path = os.path.join(dir_path, "index.json")
    if not os.path.exists(index_path):
        raise FileNotFoundError(f"index.json not found in {dir_path}")

    with open(index_path, "r") as f:
        index = json.load(f)

    total_samples = sum(shard.get("samples", 0) for shard in index.get("shards", []))

    dataset = StreamingDataset(local=dir_path, batch_size=batch_size)

    sample_count = 0
    samples = []

    for sample in dataset:
        sample_count += 1
        if sample_count in examples_to_print:
            sample_str = str(sample)[:1000]
            print(f"\nExample {sample_count}: {sample_str}...")
            # samples.append(sample)

    print(f"✔️  {sample_count} samples found in {dir_path}\n")

    return 


def analyze_individual_datasets():
    directory_paths = [
        # "mds_datasets/fineweb_2_tr/train",
        # "mds_datasets/bilkent_creative_writings/train",
        # "mds_datasets/book_corpus_v2/train",
        # "mds_datasets/dergipark/train",
        # "mds_datasets/parlamint_tr/train",
        # "mds_datasets/yoktez/train",
        # "mds_datasets/wiki/train",
        # "mds_datasets/code_corpus_2_5m/train",
        # "mds_datasets/fineweb_en_dedup_5m_subset/train",
        # "mds_datasets/math_corpus/train",
        # "mds_datasets/fineweb_2_tr/val",
        # "mds_datasets/bilkent_creative_writings/val",
        # "mds_datasets/book_corpus_v2/val",
        # "mds_datasets/dergipark/val",
        # "mds_datasets/parlamint_tr/val",
        # "mds_datasets/yoktez/val",
    ]

    for dir_path in directory_paths:
        count = fast_count_samples(dir_path)
        analyze_dataset(dir_path, example_numbers=2)    
        print(f"\nTotal samples: {count}\n")

def analyze_merged_datasets():
    train_examples_to_print = [
        1,        2,          8456,    8457, 
        8458,     8459,       13534,   13535,
        13536,    13537,     347963,  347964,
        347965,   347966,    349296,  349297,
        349298,   349299,    954012,  954013,
    ]
    
    val_examples_to_print = [
        1,	    2,	    33595,	33596,
        33597,	33598,	33600,	33601,
        33602,	33603,	33631,	33632,
        33633,	33634,	33804,	33805,
        33806,	33807,		
        33808,	33809,		
    ]

    merged_multiple_sampled_ones_to_print = [ 
        1,	        2,	        604715,	604716,
        604717,	    604718,	    1209431,	1209432,
        1209433,	1209434,	1217888,	1217889,
        1217890,	1217891,	1226345,	1226346,
        1226347,	1226348,	1234802,	1234803,
        1234804,	1234805,	1239880,	1239881,
        1239882,	1239883,	1244958,	1244959,
        1244960,	1244961,	1250036,	1250037,
        1250038,	1250039,	1251369,	1251370,
        1251371,	1251372,	1252702,	1252703,
        1252704,	1252705,	1254035,	1254036,
        1254037,	1254038,	1255368,	1255369,
        1255370,	1255371,	1256701,	1256702,
    ]

    merged_math_yoktez_dergipark_to_print = [
        1,	2,	817391,	817392,
        817393,	817394,	1293208,	1293209,
        1293210,	1293211,	1627637,	1627638,
    ]

    # print('#### Sampled Train counter:\n') 
    # validate_merged_dataset("mds_datasets/merged_math_yoktez_dergipark/train", merged_math_yoktez_dergipark_to_print)
    # print('#### Train counter:\n') 
    # validate_merged_dataset("mds_datasets/merged_all/train/", train_examples_to_print)
    print('#### Val counter:\n') 
    validate_merged_dataset("mds_datasets/merged_validation_all/", val_examples_to_print)


# analyze_individual_datasets()
analyze_merged_datasets()
