# Question Answering Ablation: Context Length

TabiBERT scores far above the other Turkish models on question answering. On TQuAD it reaches **72.34 F1**, against **63.30** for BERTurk, a gap of 9.04 F1.

TabiBERT and mmBERT were fine-tuned on TQuAD with a **1024-token** context cap. BERTurk, TweetBERT and YTU-BERT only support **512** tokens. Some of the gap could therefore come from the longer context and not from the model.

This ablation separates the two effects. The full write-up is in the paper appendix.

## Setup

- **Dataset:** TQuAD. XQuAD is excluded because every model used the same 384-token cap there, and only 1.35% of its examples exceed 512 tokens.
- **Re-runs:** We fine-tuned TabiBERT and mmBERT again on TQuAD with the context capped at **512** tokens. Only the context is truncated. The question is always kept intact.
- **Baselines:** BERTurk, TweetBERT and YTU-BERT already ran under the 512 cap, so their published scores are used as they are.
- **Hyperparameters:** The re-runs reuse each model's original best configuration from the main search. A second full search was not computationally feasible.



## 1. How much input does a 512 cap affect?

Share of TQuAD examples (question + context) longer than 512 tokens under each model's tokenizer:


| Model     | Train | Val   | Test  |
| --------- | ----- | ----- | ----- |
| BERTurk   | 11.98 | 13.15 | 10.87 |
| TweetBERT | 11.07 | 12.12 | 10.95 |
| YTU-BERT  | 11.32 | 11.95 | 10.83 |
| TabiBERT  | 13.17 | 13.98 | 10.83 |
| mmBERT    | 24.32 | 25.35 | 14.96 |


About 11–14% of examples are affected for the Turkish-oriented tokenizers. mmBERT's multilingual tokenizer splits Turkish into more subwords, so 15–25% of its examples exceed the limit.

## 2. Results (TQuAD F1)


| Model        | Published | 512-cap   | Δ     |
| ------------ | --------- | --------- | ----- |
| TweetBERT    | 38.04     | 38.04     | 0.00  |
| YTU-BERT     | 32.01     | 32.01     | 0.00  |
| BERTurk      | 63.30     | 63.30     | 0.00  |
| **TabiBERT** | 72.34     | **70.31** | −2.03 |
| mmBERT       | 71.55     | 69.26     | −2.29 |


For the three baselines, the published score and the 512-cap score are the same number, because they already ran at 512.

## Findings

- **Context length matters, but only a little.** The 512 cap lowers TabiBERT by 2.03 F1 and mmBERT by 2.29 F1.
- **Most of the gap is a model effect.** Of the 9.04 F1 gap between TabiBERT and BERTurk, about **2 F1** comes from context length. The other **~7 F1** (70.31 vs. 63.30) remains with both models at 512 tokens.
- **mmBERT shows the same pattern.** At 512 tokens it scores 69.26, still 5.96 F1 above BERTurk.
- **The effect is specific to long-passage data.** It shows up on TQuAD and not on XQuAD, whose 384-token cap fits essentially all examples for every model.



## Caveats

- Scores come from single fine-tuning runs.
- The 512-cap re-runs reuse the original hyperparameters, with no tuning at the new context length. This may slightly understate the 512-capped scores.

