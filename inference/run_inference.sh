python inference/checkpoint_evaluator.py \
    -d "/workspace/TabiBERT/checkpoints/tabibert-base-pretraining/" \
    -t "boun-tabilab/TabiBERT" \
    -p "inference/inference_dataset/short_masked.json" \
    -n 10 -k 3 -o "inference/inference_results/evaluation_results_short.md"

python inference/checkpoint_evaluator.py \
    -d "/workspace/TabiBERT/checkpoints/tabibert-base-pretraining/" \
    -t "boun-tabilab/TabiBERT" \
    -p "inference/inference_dataset/mid_masked.json" \
    -n 10 -k 3 -o "inference/inference_results/evaluation_results_mid.md"

python inference/checkpoint_evaluator.py \
    -d "/workspace/TabiBERT/checkpoints/tabibert-base-pretraining/" \
    -t "boun-tabilab/TabiBERT" \
    -p "inference/inference_dataset/long_masked.json" \
    -n 10 -k 3 -o "inference/inference_results/evaluation_results_long.md"
    