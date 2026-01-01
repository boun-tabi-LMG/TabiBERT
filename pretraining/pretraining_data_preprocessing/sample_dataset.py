import os
import pandas as pd
import pyarrow.parquet as pq
import glob
import duckdb
import argparse
import pyarrow.ipc as pa_ipc
from datasets import Dataset, DatasetDict, load_from_disk

def count_parquet_examples(file_path):
    file_paths = glob.glob(file_path)
    total_rows = 0
    print(f'Counting the number of examples in the dataset directory: {file_path}')
    for file in file_paths:
        num_rows = pq.ParquetFile(file).metadata.num_rows
        print(f'File {file}: {num_rows/1e6:.3f}M example')
        total_rows += num_rows
    # total_rows = sum(pq.ParquetFile(file).metadata.num_rows for file in file_paths)
    print(f"Total number of examples: {total_rows/1.e6:.3f}M")

def count_arrow_examples(dataset_dir):
    print(f'Counting the number of examples in the dataset directory: {dataset_dir}')
    dataset = load_from_disk(dataset_dir)  # Correct way for saved datasets
    print(f'Type : {type(dataset)}')
    print(f'index 0 : {str(dataset[0])[:1000]}\n')
    print(f'index 1 : {str(dataset[1])[:1000]}\n')
    print(f'index -1 : {str(dataset[-2])[:1000]}\n')
    print(f'index -2 : {str(dataset[-1])[:1000]}\n')

    total_rows = len(dataset)
    print(f"Total number of examples: {total_rows / 1e6:.3f}M")
    return total_rows
    
def sample_random_examples_in_parquet(input_dir, output_file, sample_size=1_000_000):
    """
    Uses DuckDB to sample 1M rows directly from Parquet files without loading everything into memory.
    """
    print(f'Preparing a sample dataset with size {sample_size} from the input directory {input_dir}')
    query = f"""
    COPY (SELECT * FROM read_parquet('{input_dir}/*.parquet')
          USING SAMPLE {sample_size}) TO '{output_file}' (FORMAT 'parquet');
    """
    duckdb.sql(query)
    print(f"✅ {sample_size} samples saved to {output_file}.")


def sample_first_examples_in_arrow(input_dir, output_dir, sample_size=5_000_000):
    print(f"🔍 Loading dataset from {input_dir}")
    dataset = Dataset.from_file(os.path.join(input_dir, "data-00000-of-00001.arrow"))

    print(f"📝 Taking the first {sample_size:,} rows...")
    sampled = dataset.select(range(sample_size))

    os.makedirs(output_dir, exist_ok=True)
    save_path = os.path.join(output_dir, "sampled.arrow")

    print(f"💾 Saving to {save_path}")
    sampled.save_to_disk(output_dir)
    print("✅ Done.")


def sample_random_examples_in_arrow(input_dir, output_dir, sample_size=2_500_000):
    print(f"🔍 Loading dataset from {input_dir}")
    dataset = Dataset.from_file(os.path.join(input_dir, "data-00000-of-00001.arrow"))

    print(f"🎲 Shuffling and sampling {sample_size:,} rows...")
    sampled = dataset.shuffle(seed=42).select(range(sample_size))

    os.makedirs(output_dir, exist_ok=True)
    save_path = os.path.join(output_dir, "sampled.arrow")

    print(f"💾 Saving to {save_path}")
    sampled.save_to_disk(output_dir)
    print("✅ Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input_dir', type=str, required=True, help='Path to the input dataset')
    parser.add_argument('-o', '--output_dir', type=str, required=True, help='Path to write the sampled dataset')
    parser.add_argument('-f', '--format', type=str, required=True, help='Parquet or Arrow')
    parser.add_argument('-s', '--sampling_type', type=str, required=True, help='Sequential or random sampling')
    parser.add_argument('-c', '--sampling_count', type=str, required=True, help='Sample size')
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    sampling_count = int(args.sampling_count)

    if args.format == 'parquet':
        sample_random_examples_in_parquet(input_dir, output_dir, sampling_count)
        count_parquet_examples(f'{output_dir}/000_00000.parquet')

    elif args.format == 'arrow':
        if args.sampling_type == 'sequential':
            # sample_first_examples_in_arrow(input_dir, output_dir, sampling_count)
            count_arrow_examples(output_dir)
        elif args.sampling_type == 'random':
            # sample_random_examples_in_arrow(input_dir, output_dir, sampling_count)
            count_arrow_examples(f'{output_dir}')
        else:
            print(f'ERROR: Sampling type {args.sampling_type} is not recognized.')
    else:
        print(f'ERROR: Sampling format {args.format} is not recognized.')

# Example usage:
# Sample 1M examples from the parquet dataset:
# python new_src/sample_dataset.py -i "./fineweb2/train" -o "./fineweb2/sample/000_00000.parquet" -f "parquet" -s "random" -c 1000000

# Sample first 5M examples from Fineweb_en:
# python new_src/sample_dataset.py -i "./fineweb_en_dedup_25m_subset/" -o "./fineweb_en_dedup_5m_subset/" -f "arrow" -s "sequential" -c 5000000

# Sample random 2.5M examples from Code:
# python new_src/sample_dataset.py -i "code_corpus/" -o "code_corpus_2_5m/" -f "arrow" -s "random" -c 2500000