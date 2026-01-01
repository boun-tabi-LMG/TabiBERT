import os
import argparse
from streaming import StreamingDataset, MDSWriter

MDS_COLS_TEXT = {
    'text': 'str',
    'id': 'str',
}

def merge_datasets(dataset_dirs, output_dir, schema):
    """Merge multiple MDS datasets into a single output directory."""
    os.makedirs(output_dir, exist_ok=True)
    total_samples = 0

    with MDSWriter(out=output_dir, columns=schema, compression=None) as writer:
        for dir_path in dataset_dirs:
            print(f"\n📂 Processing: {dir_path}")
            dataset = StreamingDataset(local=dir_path, batch_size=1)
            sample_count = 0
            for sample in dataset:
                writer.write(sample)
                sample_count += 1
            print(f"✔️  {sample_count} samples written from {dir_path}")
            total_samples += sample_count

    print(f"\n✅ Merging complete. Total samples written: {total_samples}")


if __name__ == "__main__":
    # Sampling ratios: fineweb en 1, fineweb tr 1, code 1, math 1, yoktez 1, dergipark 1, wiki 2, bilkent 3, book 3, parliment 5
    
    train_dataset_dirs = [
        # "mds_datasets/fineweb_en_dedup_5m_subset/train/",
        # "mds_datasets/fineweb_2_tr/train/",
        # "mds_datasets/code_corpus/train/",
        # "mds_datasets/math_corpus/train/",
        # "mds_datasets/yoktez/train",
        # "mds_datasets/dergipark/train",
        # "mds_datasets/wiki/train/",
        # "mds_datasets/wiki/train/",
        # "mds_datasets/bilkent_creative_writings/train",
        # "mds_datasets/bilkent_creative_writings/train",
        # "mds_datasets/bilkent_creative_writings/train",
        # "mds_datasets/book_corpus_v2/train",
        # "mds_datasets/book_corpus_v2/train",
        # "mds_datasets/book_corpus_v2/train",
        # "mds_datasets/parlamint_tr/train",
        # "mds_datasets/parlamint_tr/train",
        # "mds_datasets/parlamint_tr/train",
        # "mds_datasets/parlamint_tr/train",
        # "mds_datasets/parlamint_tr/train",
    ]
    
    validation_dataset_dirs = [
        "mds_datasets/fineweb_2_tr/val/",
        "mds_datasets/yoktez/val",
        "mds_datasets/dergipark/val",
        "mds_datasets/bilkent_creative_writings/val",
        "mds_datasets/book_corpus_v2/val",
        "mds_datasets/parlamint_tr/val",
    ]

    parser = argparse.ArgumentParser()

    # parser.add_argument('-t', '--train_output_dir', type=str, required=True, help='Path to write the merged train dataset')
    parser.add_argument('-v', '--val_output_dir', type=str, required=True, help='Path to write the merged val dataset')
    
    args = parser.parse_args()

    print('# Merging the train splits:')
    # merge_datasets(train_dataset_dirs, args.train_output_dir, MDS_COLS_TEXT)

    print('# Merging the validation splits:')
    merge_datasets(validation_dataset_dirs, args.val_output_dir, MDS_COLS_TEXT)

# Example usage:
# python new_src/merge_datasets.py -t "mds_datasets/merged_multiple_sampled_ones/train" -v "all_tr_mds_datasets/merged_all_tr/val"