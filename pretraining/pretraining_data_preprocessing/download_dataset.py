from huggingface_hub import snapshot_download
from datasets import load_dataset, load_from_disk, Dataset

# Download dataset in parquet format
def download_dataset(repo_name, output_file, split):
    # For faster downloads:
    # pip install huggingface_hub[hf_transfer]
    # export HF_HUB_ENABLE_HF_TRANSFER=1
    
    folder = snapshot_download(
        repo_name,
        repo_type="dataset",
        local_dir=output_file,
        allow_patterns=[f"data/tur_Latn/{split}/*"]
    )

# Download the fineweb train dataset:
download_dataset(repo_name="HuggingFaceFW/fineweb-2", output_file="./fineweb2/", split='train')

# Download the fineweb test dataset:
download_dataset(repo_name="HuggingFaceFW/fineweb-2", output_file="./fineweb2/", split='test')