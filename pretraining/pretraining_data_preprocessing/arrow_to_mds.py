import argparse
import os
import json
import tqdm
import gc
from datasets import load_dataset, Dataset
from streaming import MDSWriter

MDS_COLS_TEXT = {
    'text': 'str',
    'id': 'str',
}

def convert_arrow_to_mds(arrow_path, output_dir, split_name="train", chunk_size=100000):
    os.makedirs(output_dir, exist_ok=True)

    print(f"📦 Loading dataset from {arrow_path}...")
    dataset = Dataset.load_from_disk(arrow_path)
    print(f"🔢 Total records in split '{split_name}': {len(dataset)}")

    # Initialize MDS writer
    print(f"📝 Writing to MDS at {output_dir}...")
    with MDSWriter(out=output_dir, columns=MDS_COLS_TEXT, compression=None) as writer:
        print(f"✅ MDS writer initialized with columns: {MDS_COLS_TEXT}")
    
        instance_count = 0
        batch = []

        for item in tqdm.tqdm(dataset):
            batch.append({
                "text": item.get("text", ""),
                "id": str(item.get("id", f"item-{instance_count}"))
            })
            instance_count += 1

            if len(batch) >= chunk_size:
                for example in batch:
                    writer.write(example)
                batch = []
                gc.collect()

        # Write remaining batch
        for example in batch:
            writer.write(example)

    total_size = sum(
        os.path.getsize(os.path.join(dirpath, f))
        for dirpath, _, filenames in os.walk(output_dir)
        for f in filenames
    )

    print(f"✅ Successfully converted dataset to {output_dir}")
    print(f"📦 Total size: {total_size / 1e9:.2f} GB")
    print(f"🔢 Total instances: {instance_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--arrow_path', type=str, required=True, help='Path to the .arrow dataset directory (loaded via Dataset.load_from_disk)')
    parser.add_argument('-o', '--output_dir', type=str, required=True, help='Output directory for MDS files')
    args = parser.parse_args()

    convert_arrow_to_mds(args.arrow_path, args.output_dir)

# Example usage:
# python new_src/arrow_to_mds.py -a fineweb_en_dedup_5m_subset/ -o /workspace/mds_datasets/fineweb_en_dedup_5m_subset/train