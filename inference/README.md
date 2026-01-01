# TabiBERT Inference Pipeline

This directory contains the implementation of the inference pipeline for TabiBERT. 
It is designed to evaluate the model's performance during pre-training and fine-tuning phases.

## Components

### 1. Model Loading and Analysis
- `load_model_from_checkpoint.py`: Loads the model and tokenizer from checkpoints created during pre-training
- `checkpoint_analyzer.py`: Utility for analyzing checkpoint contents, parameter statistics, and model architecture
- `checkpoint_evaluator.py`: Evaluates and compares multiple checkpoints using MLM inference tasks, generating a detailed markdown report

### 2. MLM Inference
- `mlm_inference.py`: Implements masked language model inference with the following features:
  - Loads model from checkpoints
  - Processes JSON-formatted input texts
  - Performs masked token prediction
  - Logs predictions with context
  - Supports both Turkish and English texts

### 3. Logging and Utilities
- `utils.py`: Centralized logging configuration
  - Creates timestamped log files
  - Configures console and file output
  - Maintains consistent logging format across components

## Usage

1. Model Loading and Analysis:
```bash
python checkpoint_analyzer.py -c path/to/checkpoint.pt
```

2. MLM Inference:
```bash
python mlm_inference.py \
    -c path/to/checkpoint.pt \
    -t tokenizer_name \
    -p path/to/input.json -k 5
```

3. Checkpoint Evaluation and Comparison:
```bash
python checkpoint_evaluator.py -c path/to/checkpoints/directory -t tokenizer_name -d path/to/evaluation/dataset -o path/to/output/report.md
```

## Checkpoint Evaluation

The `checkpoint_evaluator.py` script provides a comprehensive way to evaluate and compare multiple model checkpoints using MLM inference tasks. It generates a detailed markdown report that helps track model performance improvements across different training stages.

### Features
- Evaluates multiple checkpoints in a single run
- Performs MLM inference on a standardized evaluation dataset
- Generates a detailed markdown report with:
  - Original texts
  - Masked texts
  - Predictions from each checkpoint
  - Performance comparison across checkpoints
- Supports both Turkish and English evaluation
- Organizes results by:
  - Domain (web, publications, scientific)
  - Text length (short, mid, long)
  - Language (Turkish, English)
  - Mask probability

### Report Structure
The markdown report includes:
- Generation timestamp and dataset information
- Collapsible sections for each sample
- For each sample:
  - Domain, language, length, and mask probability metadata
  - Original text
  - Masked text
  - Predictions from each checkpoint showing:
    - Filled text with best predictions
    - Top predictions for each masked token

### Example Report Format

```markdown
# TabiBERT Checkpoint Evaluation Report

Generated on: **2024/03/21 15:30:45**

Text path: **path/to/evaluation/dataset**

## Sample 1

<details>
<summary> web / tr / short / 0.15 </summary>

**Domain:** web
**Language:** tr
**Length:** short

### Original Text

[Original text content]

### Masked Text
[Text with [MASK] tokens]

#### Checkpoint: checkpoint_10000
[Filled text with predictions]

#### Checkpoint: checkpoint_20000
[Filled text with predictions]

</details>
```

## Input Format
The inference pipeline expects JSON files with the following structure:
```json
[
    {
        "id": "unique_id",
        "domain": "domain_name",
        "language": "tr|en",
        "length": "short|mid|long",
        "text": "Text with [MASK] tokens..."
    }
]
```

## MLM Evaluation Dataset

The inference pipeline uses a diverse evaluation dataset to evaluate the checkpoints' performance across different domains and text types. 

The dataset is structured to provide comprehensive coverage of various text categories and lengths.

### Dataset Categories and Text Length Distribution

| Category       | Language | Total Examples | Short | Mid | Long |
|----------------|----------|----------------|-------|-----|------|
| web            | tr       | 3              | 1     | 1   | 1    |
| web            | en       | 3              | 1     | 1   | 1    |
| creative       | tr       | 3              | 1     | 1   | 1    |
| article        | tr       | 3              | 1     | 1   | 1    |
| thesis         | tr       | 3              | 1     | 1   | 1    |
| parliment      | tr       | 3              | 1     | 1   | 1    |
| code           | en       | 3              | 1     | 1   | 1    |
| math           | en       | 3              | 1     | 1   | 1    |

### Length Categories
- **Short**: 1-8 sentences
- **Mid**: 9-15 sentences
- **Long**: 20-30 sentences

### Dataset Characteristics
- **Total examples**: 24
- **Language distribution**: 15 Turkish, 9 English
- Each example has **3 levels of mask_probability**: 15%, 30% and 45%
- Examples are selected to be representative of their domains while avoiding direct overlap with training data

## Dataset Tokenization and Masking
The `tokenize_dataset.py` script prepares evaluation datasets by:
- Tokenizing input texts using the model's tokenizer
- Adding mask tokens with specified probability (15%, 30%, or 45%)
- Preserving original text metadata (domain, language, length)
- Generating masked versions of texts for MLM evaluation

Usage:
```bash
# Tokenize and mask short texts
python tokenize_dataset.py \
    -t "boun-tabilab/TabiBERT" \
    -d "inference_dataset/short.json" \
    -o "inference_dataset/short_masked.json" \
    -l 1024 \
    -m 0.15

# Tokenize and mask medium-length texts
python tokenize_dataset.py \
    -t "boun-tabilab/TabiBERT" \
    -d "inference_dataset/mid.json" \
    -o "inference_dataset/mid_masked.json" \
    -l 1024 \
    -m 0.15

# Tokenize and mask long texts
python tokenize_dataset.py \
    -t "boun-tabilab/TabiBERT" \
    -d "inference_dataset/long.json" \
    -o "inference_dataset/long_masked.json" \
    -l 1024 \
    -m 0.15
```

Parameters:
- `-t, --tokenizer`: Path to the tokenizer
- `-d, --dataset`: Path to the input dataset
- `-o, --output`: Path to save the masked dataset
- `-l, --max_seq_len`: Maximum sequence length (default: 512)
- `-m, --mask_probability`: Probability of masking each token (default: 0.15)
