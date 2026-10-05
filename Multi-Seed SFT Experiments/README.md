# Multi-Seed Evaluations

Our original fine-tuning experiments used a single seed. To check how robust the smallest performance margins between TabiBERT and the previous best Turkish model are, we reran fine-tuning and evaluation with 5 seeds: `[7, 25, 42, 100, 1234]`.

Reported single-seed margins (performance difference, ∆) are those from the last two rows of Table 5 in the TabiBERT paper.

Per-seed scores for every dataset and category are in `[per_seed_scores.csv](per_seed_scores.csv)` (columns: `category, model, dataset, seed, score`; rows named `[category weighted avg]` are the test-size-weighted category scores used in the paper). Means are over the five seeds and ± is the sample standard deviation (n-1).

## Experiment #1: Head-to-head on the two closest tasks

Of all tasks, NLI has the smallest margin by which TabiBERT leads (+0.18), and Token Classification has the smallest margin by which it trails (-0.25). We ran multi-seed fine-tuning and evaluation for **both TabiBERT and BERTurk** on these two tasks.


| Metric                           | Token Clf    | NLI          |
| -------------------------------- | ------------ | ------------ |
| BERTurk (single-seed)            | 93.67        | 84.33        |
| TabiBERT (single-seed)           | 93.42        | 84.51        |
| Margin (single-seed)             | -0.25        | +0.18        |
| BERTurk (multi-seed mean ± std)  | 93.37 ± 0.58 | 84.34 ± 0.14 |
| TabiBERT (multi-seed mean ± std) | 93.31 ± 0.08 | 84.45 ± 0.13 |
| Margin (multi-seed)              | -0.06        | +0.11        |


**Conclusion:** Under multi-seed evaluation, TabiBERT's lead on NLI narrows slightly but holds (+0.11), and its deficit on Token Classification narrows from -0.25 to -0.06 but remains. Both differences are of the same size as the seed-to-seed spread, and a Welch t-test on the five-seed category scores is not significant for either (NLI t = 1.23, Token Classification t = -0.21), so we treat them as indicative rather than established.

## Experiment #2: TabiBERT-only check on other close tasks

We also identified three further tasks with small single-seed margins: STS (-0.59), Information Retrieval (+0.60), and Academic Understanding (+0.77). Due to compute constraints, we ran multi-seed fine-tuning and evaluation for **TabiBERT only** on these tasks (no BERTurk comparison).


| Metric                                    | STS          | Information Retrieval | Academic Understanding |
| ----------------------------------------- | ------------ | --------------------- | ---------------------- |
| TabiBERT (single-seed)                    | 84.74        | 75.44                 | 70.06                  |
| Margin (single-seed)                      | -0.59        | +0.60                 | +0.77                  |
| TabiBERT (multi-seed mean ± std)          | 85.10 ± 0.44 | 75.61 ± 0.17          | 69.88 ± 0.21           |
| Margin vs. published BERTurk (multi-seed) | -0.23        | +0.77                 | +0.59                  |


**Conclusion:** TabiBERT continues to lead on Information Retrieval and Academic Understanding, and its multi-seed STS margin narrows substantially relative to the single-seed result, though it still trails on this task.