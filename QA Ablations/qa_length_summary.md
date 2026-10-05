# QA length ablation: share of examples over 512 tokens

Source: [examine_qa_dataset.py](examine_qa_dataset.py) → [qa_length_stats.csv](qa_length_stats.csv).

The percentages are the share of examples where (question + context), special tokens included, exceeds 512 tokens under each model's tokenizer. That is exactly when `truncation='only_second'` in `QADataset` would cut the context. Uncased models (TurkishBERTweet, YTU-Cosmos-BERT) are lowercased first, as in `QADataset`.

## All splits combined

| Model | XQuAD-TR (n=1190) | TQuAD-2 (n=16,741) |
|---|---|---|
| TabiBERT | 1.35% | 12.93% |
| BERTurk | 1.35% | 11.98% |
| TurkishBERTweet | 1.60% | 11.21% |
| YTU-Cosmos-BERT | 1.35% | 11.34% |
| mmBERT | 2.86% | 23.06% |

## Per split (train / validation / test)

| Model | XQuAD-TR | TQuAD-2 |
|---|---|---|
| TabiBERT | 1.44 / 1.69 / 0.56 | 13.17 / 13.98 / 10.83 |
| BERTurk | 1.44 / 1.69 / 0.56 | 11.98 / 13.15 / 10.87 |
| TurkishBERTweet | 1.68 / 2.25 / 0.56 | 11.07 / 12.12 / 10.95 |
| YTU-Cosmos-BERT | 1.44 / 1.69 / 0.56 | 11.32 / 11.95 / 10.83 |
| mmBERT | 2.88 / 3.37 / 2.23 | 24.32 / 25.35 / 14.96 |

Split sizes: XQuAD-TR 833 / 178 / 179; TQuAD-2 11,803 / 2,418 / 2,520.

## Takeaways

- **XQuAD-TR:** truncation barely matters. Only 1–3% of examples are over 512 tokens, and the gold answer is lost in at most 0.08% of examples for the Turkish tokenizers (0.42% for mmBERT).
- **TQuAD-2:** about 11–13% of examples are over 512 tokens for the four Turkish-oriented tokenizers. The gold answer falls outside the truncated context in roughly 2.8–3.3% of examples. The long tail is heavy: p95 is around 700–850 tokens and the max is near 2,700.
- **mmBERT:** its multilingual tokenizer splits Turkish into more tokens, so about twice as many TQuAD-2 examples are over 512 (23%). The answer is lost in 6.8% of examples, about double the others. Any 512-token comparison therefore disadvantages mmBERT most.
- **TabiBERT:** it has the highest over-512 share among the four Turkish-oriented tokenizers on TQuAD-2 (12.9% vs 11.2–12.0%), driven by train and validation.
- **Test split:** the test split is shorter than train/validation for every model, at about 10.8–11.0% for the Turkish tokenizers.

## Answer lost to truncation (% of examples, all splits)

| Model | XQuAD-TR | TQuAD-2 |
|---|---|---|
| TabiBERT | 0.08% | 3.32% |
| BERTurk | 0.08% | 3.12% |
| TurkishBERTweet | 0.08% | 2.91% |
| YTU-Cosmos-BERT | 0.08% | 2.84% |
| mmBERT | 0.42% | 6.85% |
