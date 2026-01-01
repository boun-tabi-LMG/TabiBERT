import argparse
import os
import json
import tqdm
import gc
from datasets import load_dataset
from streaming import MDSWriter

MDS_COLS_TEXT = {
    'text': 'str',
    'id': 'str'
}


def parquet_to_mds(parquet_path, dataset_path, output_dir, repo_name="fineweb2_turkish", split_name = "train", config_name = "tur_Latn", chunk_size = 10000):
    # Load dataset in streaming mode
    dataset = load_dataset("parquet", data_files=parquet_path, streaming=True)['train']
    
    # Initialize MDS writer
    print(f"Writing to MDS at {dataset_path}...")
    with MDSWriter(out=dataset_path, columns=MDS_COLS_TEXT, compression=None) as writer:
    # with MDSWriter(out=dataset_path, columns=MDS_COLS_TEXT, compression='zstd') as writer:
        print("MDS writer initialized.")
        print(f"Column definitions: {MDS_COLS_TEXT}")
    
        instance_count = 0
        batch = []
    
        print("Starting to iterate through dataset...")
        # Stream through dataset without loading into RAM all at once
        for item in tqdm.tqdm(dataset):
            batch.append({
                "text": item.get("text", ""),
                "id": item.get("id", f"item-{instance_count}")
            })
            instance_count += 1
           
            # Process in chunks to avoid memory overflow
            if len(batch) >= chunk_size:
                for example in batch:
                    writer.write(example)
                # Clear batch and release memory
                batch = []
                gc.collect()
    
        # Write any remaining examples
        for example in batch:
            writer.write(example)
    
    # Calculate dataset size
    total_size = sum(
        os.path.getsize(os.path.join(dirpath, f))
        for dirpath, _, filenames in os.walk(dataset_path)
        for f in filenames
    )
    
    # Save dataset info
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "dataset_info.jsonl"), "a") as f:
        f.write(json.dumps({
            "dataset": repo_name,
            "split_name": split_name,
            "config_name": config_name,
            "size_gb": total_size / 1e9,
            "instances": instance_count,
            "local_path": dataset_path
        }) + "\n")
    
    print(f"✅ Successfully converted dataset to {dataset_path}")
    print(f"📦 Total size: {total_size / 1e9:.2f} GB")
    print(f"🔢 Total instances: {instance_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-p', '--parquet_path', type=str, required=True, help='Path to the original data file')
    parser.add_argument('-d', '--dataset_path', type=str, required=True, help='Path to write the converted data file')
    parser.add_argument('-o', '--output_dir', type=str, required=True, help='')
    parser.add_argument('-r', '--repo_name', type=str, help='Hugging face repo name')
    parser.add_argument('-s', '--split_name', type=str, help='Split name')
    
    args = parser.parse_args()

    if args.repo_name and args.split_name:
        parquet_to_mds(args.parquet_path, args.dataset_path, args.output_dir, args.repo_name, args.split_name, chunk_size = 100000)
    elif args.repo_name:
        parquet_to_mds(args.parquet_path, args.dataset_path, args.output_dir, args.repo_name, chunk_size = 100000)
    elif args.split_name:
        parquet_to_mds(args.parquet_path, args.dataset_path, args.output_dir, args.split_name, chunk_size = 100000)
    else:
        parquet_to_mds(args.parquet_path, args.dataset_path, args.output_dir, chunk_size = 100000)
        
# Example usage:
# python new_src/parquet_to_mds.py -p "./original_datasets/fineweb_2_tr/train/*.parquet" -d "./mds_datasets/fineweb_2_tr/train" -o "./mds_datasets/fineweb_2_tr"
# python new_src/parquet_to_mds.py -p "./fineweb2/sample/*.parquet" -d "./fineweb2_mds/sample" -o "./fineweb2_mds/sample"
# python new_src/parquet_to_mds.py -p "./fineweb2/train/*.parquet" -d "./fineweb2_mds/train" -o "./fineweb2_mds/train"