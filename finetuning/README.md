# Finetuning for Downstream Tasks

This directory contains the finetuning pipeline for evaluating Turkish language models on downstream NLP tasks.

## Models

We evaluate the following models:

* **[TabiBERT](https://huggingface.co/boun-tabilab/TabiBERT)** - Our model
* [BERTurk](https://huggingface.co/dbmdz/bert-base-turkish-cased)
* [YTU-Cosmos-BERT](https://huggingface.co/ytu-ce-cosmos/turkish-base-bert-uncased)
* [TurkishBERTweet](https://huggingface.co/VRLLab/TurkishBERTweet)
* [mmBERT](https://huggingface.co/jhu-clsp/mmBERT-base)

## Tasks

| Task | Datasets | Description |
|------|----------|-------------|
| **Text Classification** | NewsCat, Product Reviews, Bil Tweet News, Gender Hate Speech | News categorization, sentiment analysis, hate speech detection |
| **Token Classification** | WikiNER, WikiANN TR, PosUD BOUN, PosUD IMST | Named entity recognition and part-of-speech tagging |
| **Semantic Textual Similarity** | SICK-TR, STSb-TR | Semantic similarity scoring between sentence pairs |
| **Natural Language Inference** | SNLI-TR, MultiNLI-TR | Entailment, contradiction, and neutral classification |
| **Question Answering** | TQuAD, XQuAD | Turkish question answering |
| **Information Retrieval** | BiText, MsMarco-TR, Scifact-TR, Fiqa-TR, NFCorpus-TR, Quora-TR | Multi-domain retrieval tasks (web search, scientific, financial) |
| **Code Retrieval** | Apps-TR, CodeSearchNet-21K-TR, CosQA-TR, StackoverflowQA-TR | Code retrieval with Turkish queries/documents |
| **Academic Domain** | MedNLI, PubmedRCT-20K, SciCite, Thesis-Abstract-Classification | Medical NLI, abstract classification, citation intent, thesis classification |

## Setup

Install dependencies:
```sh
bash finetuning.sh
```

## Usage

### Hyperparameter Tuning

- **hyperparameter_tuner.py**: Performs grid search over hyperparameters (learning rate, weight decay, epochs, batch size) for models and tasks defined in `hyperparam_tuning.py`. Supports classification, regression, NER, POS, NLI, QA, and IR tasks.
- **hyperparam_tuning.py**: Configuration file that defines models, tasks, and their parameters.

### Finetuning

```sh
composer finetuning/sequence_classification.py finetuning/yamls/class-<model-name>.yaml <task-name>
```

Example:
```sh
# Finetune TabiBERT on product reviews
composer finetuning/sequence_classification.py finetuning/yamls/class-tabibert.yaml prod_review
```

For Information Retrieval and Code Retrieval tasks, use the following command for fine-tuning and evaluation:
```sh
python finetuning/hyperparam_retrieval_train.py finetuning/yamls/class-<model-name>.yaml <task-name>
```

### Evaluation

Use task-specific evaluation scripts:

```sh
# Text classification
python finetuning/eval_text_classification.py finetuning/yamls/class-tabibert.yaml \
    prod_review finetuned_checkpoints/classification/prod_review/TabiBERT/latest-rank0.pt 1

# Token classification
python finetuning/eval_token_classification.py finetuning/yamls/class-tabibert.yaml \
    pos_ud_boun finetuned_checkpoints/pos/pos_ud_boun/TabiBERT/latest-rank0.pt 1

# Semantic textual similarity
python finetuning/hyperparam_sts_eval.py finetuning/yamls/class-tabibert.yaml sts \
    finetuned_checkpoints/regression/sts/TabiBERT/latest-rank0.pt sts

# NLI:
python finetuning/hyperparam_nli_eval.py finetuning/yamls/class-tabibert.yaml snli \
    finetuned_checkpoints/nli/snli/TabiBERT/latest-rank0.pt snli

# Question answering
python finetuning/hyperparam_qa_eval.py finetuning/yamls/class-tabibert.yaml tquad \
    finetuned_checkpoints/qa/tquad/TabiBERT/latest-rank0.pt 1
```

## Troubleshooting

**Common Issues:**
- Model loading errors → Verify YAML matches model architecture
- Memory issues → Reduce batch size or sequence length
- Import errors → Check Python path and dependencies
- Checkpoint mismatch → Use `strict=False` when loading

**Performance Tips:**
- Monitor GPU memory and adjust batch sizes
- Use appropriate data loading workers
- Enable mixed precision training
- Use gradient accumulation for larger effective batch sizes

## Adding New Models/Tasks

1. Create a YAML configuration file in `yamls/`
2. Update data loaders in `dataloaders/` if needed
3. Test end-to-end pipeline
4. Update this README
