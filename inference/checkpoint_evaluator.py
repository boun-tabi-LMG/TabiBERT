"""
This script is used to evaluate the performance of checkpoints.
It takes a checkpoint directory, a tokenizer, a text path, and a number of checkpoints to evaluate.
It then runs inference on the text path and saves the results to a markdown file.

Example usage:
python checkpoint_evaluator.py \
    -d "./checkpoints/directory/" \
    -t "boun-tabilab/TabiBERT" \
    -p "inference_dataset/short_masked.json" \
    -n 3 -k 3 -o "evaluation_results_short.md"
"""
# TODO: Apply OOP for inference results and outputs later.
import os
import argparse
import glob
from datetime import datetime
import torch
from typing import List, Dict, Any
import json
from mlm_inference import predict_masked_tokens
from read_dataset import read_json_dataset
from load_model_from_checkpoint import load_model
from utils import setup_logging

logger = setup_logging('checkpoint_evaluator.py')


def get_recent_checkpoints(checkpoint_dir: str, n: int = 5) -> List[str]:
    """
    Get the N most recent checkpoint files from the directory.
    
    Args:
        checkpoint_dir: Directory containing checkpoint files
        n: Number of recent checkpoints to return
        
    Returns:
        List of paths to the N most recent checkpoints
    """
    # Get all .pt files in the directory
    checkpoint_files = glob.glob(os.path.join(checkpoint_dir, "*.pt"))

    # Sort by modification time (newest first)
    checkpoint_files.sort(key=os.path.getmtime, reverse=True)
    checkpoint_files = [
        file for file in checkpoint_files if "latest-rank0.pt" not in file
    ]

    # Return the N most recent
    recent_checkpoint_files = list(reversed(checkpoint_files[:n]))
    return recent_checkpoint_files


def generate_markdown_report(results: Dict[str, List[Dict[str, Any]]],
                             text_path: str, output_path: str):
    """
    Generate a markdown report from the inference results.
    
    Args:
        results: Dictionary mapping checkpoint paths to their inference results
        output_path: Path to save the markdown report
    """

    inference = {}

    checkpoints = results.keys()

    for checkpoint in checkpoints:
        checkpoint_inference = results[checkpoint]
        for sample in checkpoint_inference:
            id = int(sample['id'])
            text = sample['text']
            masked_text = sample['masked_text']
            domain = sample['domain']
            language = sample['language']
            length = sample['length']
            mask_probability = float(sample['mask_probability'])
            predictions = sample['predictions']
            filled_text = sample['filled_text']

            if mask_probability == 0.15:
                mask_index = 0
            elif mask_probability == 0.30:
                mask_index = 1
            elif mask_probability == 0.45:
                mask_index = 2

            sample_index = mask_index * 8 + id + 1

            if sample_index not in inference:
                inference[sample_index] = {
                    'original_text': text,
                    'masked_text': masked_text,
                    'domain': domain,
                    'language': language,
                    'length': length,
                    'mask_probability': mask_probability,
                    'checkpoints': {}
                }

            inference[sample_index]['checkpoints'][checkpoint] = {
                'filled_text': filled_text,
                'predictions': predictions
            }

    with open(output_path, 'w', encoding='utf-8') as f:
        # Write header
        f.write("# TabiBERT Checkpoint Evaluation Report\n\n")
        f.write(
            f"Generated on: **{datetime.now().strftime('%Y/%m/%d %H:%M:%S')}**\n\n"
        )
        f.write(f"Text path: **{text_path}**\n\n")

        for sample_idx, sample in inference.items():
            f.write(f"## Sample {sample_idx}\n\n")
            f.write(
                f"<details>\n<summary> {sample['domain']} / {sample['language']} / {sample['length']} / {sample['mask_probability']} </summary>\n\n"
            )
            f.write("### Original Text\n\n")
            original_text = sample['original_text']
            original_text = original_text.replace("```", "`")
            f.write(f"```\n{original_text}\n```\n\n")

            f.write("### Masked Text\n\n")
            masked_text = sample['masked_text']
            masked_text = masked_text.replace("```", "`")
            f.write(f"```\n{masked_text}\n```\n\n")

            for checkpoint, checkpoint_results in sample['checkpoints'].items(
            ):
                checkpoint_name = os.path.basename(checkpoint)
                f.write(f"#### Checkpoint: {checkpoint_name}\n\n")
                f.write(f"```\n{checkpoint_results['filled_text']}\n```\n\n")

            f.write("\n</details>\n\n")


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate multiple checkpoints using MLM inference")
    parser.add_argument('-d',
                        '--checkpoint_dir',
                        type=str,
                        required=True,
                        help="Directory containing checkpoint files")
    parser.add_argument('-t',
                        '--tokenizer',
                        type=str,
                        required=True,
                        help="Path or HuggingFace repo to tokenizer")
    parser.add_argument('-p',
                        '--text_path',
                        type=str,
                        required=True,
                        help="Path to the JSON file containing text samples")
    parser.add_argument(
        '-n',
        '--num_checkpoints',
        type=int,
        default=5,
        help="Number of recent checkpoints to evaluate (default: 5)")
    parser.add_argument(
        '-k',
        '--top_k',
        type=int,
        default=5,
        help="Number of top predictions to return for each mask (default: 5)")
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default="evaluation_report.md",
        help="Path to save the markdown report (default: evaluation_report.md)"
    )

    args = parser.parse_args()

    # Get recent checkpoints
    checkpoints = get_recent_checkpoints(args.checkpoint_dir,
                                         args.num_checkpoints)
    logger.info(f"Found {len(checkpoints)} recent checkpoints")
    logger.info(f"       ######      Checkpoints: {checkpoints}")

    # Load text samples
    text_path = args.text_path
    samples = read_json_dataset(text_path)
    logger.info(f"Loaded {len(samples)} text samples")

    # Store results for each checkpoint
    all_results = {}

    # Process each checkpoint
    for checkpoint_path in checkpoints:
        logger.info(f"\nProcessing checkpoint: {checkpoint_path}")

        # Load model and tokenizer
        model, tokenizer = load_model(checkpoint_path, args.tokenizer)
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        model.to(device)  # Use CPU for inference

        # Run inference
        results = []
        for sample in samples:
            logger.info(f"Processing sample {sample['id']}")
            predictions, filled_text = predict_masked_tokens(model,
                                                             tokenizer,
                                                             sample,
                                                             top_k=args.top_k)
            results.append({
                'id': sample['id'],
                'text': sample['text'],
                'masked_text': sample['masked_text'],
                'domain': sample['domain'],
                'language': sample['language'],
                'length': sample['length'],
                'mask_probability': sample['mask_probability'],
                'predictions': predictions,
                'filled_text': filled_text
            })

        all_results[checkpoint_path] = results

        # Clear memory
        del model
        torch.cuda.empty_cache()

    # Generate markdown report
    generate_markdown_report(all_results, text_path, args.output)
    logger.info(f"Evaluation report saved to: {args.output}")


if __name__ == "__main__":
    main()
    logger.info("Script completed successfully")
