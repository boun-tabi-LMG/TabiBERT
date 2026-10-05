# TabiBench translation-adequacy audit

Native-speaker audit of the six TabiBench datasets that we machine-translated with GPT-4.1
(Apps-TR, CodeSearchNet-21K-TR, CosQA-TR, StackOverflowQA-TR, PubMedRCT-10K-TR, SciCite-TR).
Reported in Section 7.3 of the paper. Nothing was re-translated on the basis of the audit; it measures quality.

## Design

* Sample: from the **test** split of each dataset, 20 items per dataset (120, the headline "main" stratum) plus up to
  3 items per dataset whose Turkish/English length ratio is an outlier (17, the separately reported "outlier" stratum).
  A seventh dataset, MedNLI-TR, was sampled and rated alongside these (23 items) but was removed from TabiBench during the
  revision because its source corpus requires PhysioNet credentialed access; its items are excluded from the released files
  and from every reported statistic (`05_score.py --exclude MedNLI`).
  Fixed seed (`audit_config.SEED`). StackOverflowQA items are half questions, half answers.
* Raters: three native Turkish speakers (graduate and undergraduate computer-engineering students, not authors),
  each rating **every** item independently against the English source, in a per-rater shuffled order.
* Rubric (`04_workbook.py`): OK (meaning preserved) / MINOR (preserved but flawed) / MAJOR (meaning changed),
  plus `task_valid` = does the gold label or gold document still hold for the Turkish version (YES / NO / UNSURE).
  Code is untouched by design; identifiers and code terms left in English are not errors.
* Adjudication (`05_score.py`, pre-specified): majority vote; a three-way split goes to the more severe label.
  The number of such splits and the median-rule rate are reported as a sensitivity check.
* Statistics: Wilson 95% intervals; pairwise Cohen's kappa (3-class, linear-weighted, MAJOR-vs-not); Fleiss' kappa.

## Files

| file | content |
|---|---|
| `sample/ratings_anonymized.csv` | every rating: item_id, dataset, stratum, rater (A/B/C), rating, task_valid, comment |
| `sample/audit_results.md`, `.csv` | scorer output: rates, intervals, per-dataset counts, agreement, disagreement list |
| `sample/sample_items.jsonl` | the rated items as shown to raters (English source, Turkish translation, task context). MedNLI text is withheld because the source corpus requires PhysioNet credentialed access; the manifest locates those items. |
| `sample/item_manifest.csv` | item_id -> dataset, stratum, test-split row index, rated field, translation-pipeline idx, length z-scores |
| `01_collect_pairs.py` .. `05_score.py`, `audit_config.py` | the pipeline; steps 1-4 need the translation pipeline's result files and the local datasets, step 5 needs only the filled workbooks |

Reproduce the reported numbers from the released ratings:

```
python 05_score.py sample/rater_A.xlsx sample/rater_B.xlsx sample/rater_C.xlsx   # from the original workbooks, or
python - <<'PY'                                                                    # from ratings_anonymized.csv
import pandas as pd; r = pd.read_csv("sample/ratings_anonymized.csv")
m = r[r.stratum == "main"].pivot(index="item_id", columns="rater", values="rating")
print((m == "MAJOR").sum(axis=1).ge(2).sum(), "items with a MAJOR majority; plus ties -> see 05_score.py")
PY
```
