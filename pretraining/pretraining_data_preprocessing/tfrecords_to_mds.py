import argparse
import os
import json
import tqdm
import gc
from datasets import load_dataset, Dataset
from streaming import MDSWriter
import tensorflow as tf
import glob

MDS_COLS_TEXT = {
    'text': 'str',
    'id': 'str',
}

# ---- TFRecord parsing section ----

def parse_example(example_proto):
    feature_description = {
        "id": tf.io.FixedLenFeature([], tf.int64),
        "text": tf.io.FixedLenFeature([], tf.string),
        "corpus": tf.io.FixedLenFeature([], tf.string),
        "article": tf.io.FixedLenFeature([], tf.string),
    }
    return tf.io.parse_single_example(example_proto, feature_description)

def load_tfrecords_to_list(tfrecord_dir):
    tfrecord_files = sorted(glob.glob(os.path.join(tfrecord_dir, "*.tfrecord-*")))
    raw_dataset = tf.data.TFRecordDataset(tfrecord_files)
    parsed_dataset = raw_dataset.map(parse_example)

    data = []
    for example in parsed_dataset:
        data.append({
            "id": int(example["id"].numpy()),
            "text": example["text"].numpy().decode("utf-8"),
            "corpus": example["corpus"].numpy().decode("utf-8"),
            "article": example["article"].numpy().decode("utf-8"),
        })
    return data


def convert_to_mds(tfrecord_dataset, output_dir, split_name = "train", config_name = "tur_Latn", chunk_size = 100000):
    os.makedirs(output_dir, exist_ok=True)

    # Initialize MDS writer
    print(f"Writing to MDS at {output_dir}...")
    with MDSWriter(out=output_dir, columns=MDS_COLS_TEXT, compression=None) as writer:
        print("MDS writer initialized.")
        print(f"Column definitions: {MDS_COLS_TEXT}")
    
        instance_count = 0
        batch = []
    
        print("Starting to iterate through dataset...")
        # Stream through dataset without loading into RAM all at once
        for item in tqdm.tqdm(tfrecord_dataset):
            batch.append({
                "text": item.get("text", ""),
                "id": str(item.get("id", f"item-{instance_count}"))
            })
            instance_count += 1
           
            # Process in chunks to avoid memory overflow
            if len(batch) >= chunk_size:
                for example in batch:
                    writer.write(example)
                # Clear batch and release memory
                batch = []
                gc.collect()
            if instance_count % 10000 == 0:
                print(f'Count: {instance_count}')
        # Write any remaining examples
        for example in batch:
            # print(f'\n\n##### EXAMPLE: {example}\n\n')
            writer.write(example)
    
    # Calculate dataset size
    total_size = sum(
        os.path.getsize(os.path.join(dirpath, f))
        for dirpath, _, filenames in os.walk(output_dir)
        for f in filenames
    )
    
    # Save dataset info
    # os.makedirs(output_dir, exist_ok=True)
    # with open(os.path.join(output_dir, "dataset_info.jsonl"), "a") as f:
    #     f.write(json.dumps({
    #         "dataset": repo_name,
    #         "split_name": split_name,
    #         "config_name": config_name,
    #         "size_gb": total_size / 1e9,
    #         "instances": instance_count,
    #         "local_path": dataset_path
    #     }) + "\n")
    
    print(f"✅ Successfully converted dataset to {output_dir}")
    print(f"📦 Total size: {total_size / 1e9:.2f} GB")
    print(f"🔢 Total instances: {instance_count}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument('-t', '--tfrecord_path', type=str, required=True, help='Path to the original data file')
    parser.add_argument('-o', '--output_dir', type=str, required=True, help='')
    parser.add_argument('-s', '--split_name', type=str, help='Split name')
    
    args = parser.parse_args()

    print(f"Loading TFRecords from: {args.tfrecord_path}")
    parsed_dataset = tf.data.TFRecordDataset(sorted(glob.glob(os.path.join(args.tfrecord_path, "*.tfrecord-*"))))
    parsed_dataset = parsed_dataset.map(parse_example)
    
    def gen_items():
        for example in parsed_dataset:
            yield {
                "id": int(example["id"].numpy()),
                "text": example["text"].numpy().decode("utf-8"),
                "corpus": example["corpus"].numpy().decode("utf-8"),
                "article": example["article"].numpy().decode("utf-8"),
            }

    print(f"Converting to MDS format in: {args.output_dir}")
    convert_to_mds(gen_items(), args.output_dir)

    # data = load_tfrecords_to_list(args.tfrecord_path)
    # convert_to_mds(data, args.output_dir)

    print("✅ Done!")
   

# python new_src/tfrecords_to_mds.py -t all_tr_datasets/dergipark/1.0.0/train -o all_tr_mds_datasets/dergipark/train
# python new_src/tfrecords_to_mds.py -t all_tr_datasets/yoktez/1.0.0/train -o all_tr_mds_datasets/yoktez/train
