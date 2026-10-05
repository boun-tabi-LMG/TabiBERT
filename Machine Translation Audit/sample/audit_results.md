# Translation adequacy audit: results (3 raters: A, B, C)

## Stratum: main (n = 120 items rated by all 3 raters)

- MAJOR (meaning changed), majority vote: 12/120 = 10.0% (95% Wilson CI 5.8-16.7%)
  - sensitivity: 3 tie(s) resolved to the more severe label; under the median rule MAJOR = 9/120 = 7.5%; MAJOR by any rater 13/120; by all raters 2/120
- MINOR or worse: 28/120 = 23.3% (CI 16.7-31.7%)
- Task validity broken (gold no longer holds): 1/120 = 0.8% (CI 0.1-4.6%)

Per-rater rating distribution:

| rater   |   MAJOR |   MINOR |   OK |
|:--------|--------:|--------:|-----:|
| A       |       9 |      22 |   89 |
| B       |       3 |       5 |  112 |
| C       |      12 |      32 |   76 |

Per-dataset adjudicated counts (descriptive only):

| dataset         |   MAJOR |   MINOR |   OK |
|:----------------|--------:|--------:|-----:|
| Apps            |       3 |       4 |   13 |
| CodeSearchNet   |       2 |       1 |   17 |
| CosQA           |       1 |       2 |   17 |
| PubMedRCT       |       2 |       4 |   14 |
| SciCite         |       2 |       4 |   14 |
| StackOverflowQA |       2 |       1 |   17 |

Inter-rater agreement:

- A vs B: raw agreement 71.7%, Cohen's kappa 3-class = 0.05, linear-weighted = 0.12; MAJOR-vs-not: raw 93.3%, kappa = 0.31
- A vs C: raw agreement 80.0%, Cohen's kappa 3-class = 0.58, linear-weighted = 0.66; MAJOR-vs-not: raw 97.5%, kappa = 0.84
- B vs C: raw agreement 62.5%, Cohen's kappa 3-class = 0.05, linear-weighted = 0.09; MAJOR-vs-not: raw 90.8%, kappa = 0.24
- Fleiss' kappa (3 raters, n = 120): 3-class = 0.24; MAJOR-vs-not = 0.51

Draft for Section 7.3:

> By majority vote among 3 raters over 120 test-split items (20 per dataset) from the 6 datasets we translated, meaning was changed in 12 items (10.0 per cent; 95 per cent Wilson interval 5.8-16.7), a further 16 had lesser flaws, and the gold label or gold document no longer held for 1 item (0.8 per cent); Fleiss' kappa = 0.51 for meaning-changed versus not (0.24 on the three-level scale).

Items with a MAJOR vote on which the raters disagree: 11

| item_id    | A     | B     | C     | adjudicated   |
|:-----------|:------|:------|:------|:--------------|
| APPS-003   | MAJOR | OK    | MAJOR | MAJOR         |
| APPS-006   | MINOR | OK    | MAJOR | MAJOR         |
| APPS-009   | MAJOR | OK    | MAJOR | MAJOR         |
| CODESE-012 | MAJOR | OK    | MAJOR | MAJOR         |
| CODESE-018 | MAJOR | MINOR | MAJOR | MAJOR         |
| PUBMED-006 | MAJOR | OK    | MAJOR | MAJOR         |
| PUBMED-019 | MINOR | OK    | MAJOR | MAJOR         |
| SCICIT-007 | OK    | MAJOR | OK    | OK            |
| SCICIT-017 | MINOR | OK    | MAJOR | MAJOR         |
| SCICIT-020 | MAJOR | OK    | MAJOR | MAJOR         |
| STACKO-009 | MAJOR | OK    | MAJOR | MAJOR         |

## Stratum: outlier (n = 17 items rated by all 3 raters)

- MAJOR (meaning changed), majority vote: 11/17 = 64.7% (95% Wilson CI 41.3-82.7%)
  - sensitivity: 0 tie(s) resolved to the more severe label; under the median rule MAJOR = 11/17 = 64.7%; MAJOR by any rater 11/17; by all raters 9/17
- MINOR or worse: 12/17 = 70.6% (CI 46.9-86.7%)
- Task validity broken (gold no longer holds): 2/17 = 11.8% (CI 3.3-34.3%)

Per-rater rating distribution:

| rater   |   MAJOR |   MINOR |   OK |
|:--------|--------:|--------:|-----:|
| A       |      11 |       1 |    5 |
| B       |       9 |       0 |    8 |
| C       |      11 |       2 |    4 |

Per-dataset adjudicated counts (descriptive only):

| dataset         |   MAJOR |   MINOR |   OK |
|:----------------|--------:|--------:|-----:|
| Apps            |       3 |       0 |    0 |
| CodeSearchNet   |       1 |       0 |    2 |
| CosQA           |       2 |       0 |    0 |
| PubMedRCT       |       1 |       1 |    1 |
| SciCite         |       1 |       0 |    2 |
| StackOverflowQA |       3 |       0 |    0 |

Inter-rater agreement:

- A vs B: raw agreement 82.4%, Cohen's kappa 3-class = 0.66, linear-weighted = 0.70; MAJOR-vs-not: raw 88.2%, kappa = 0.76
- A vs C: raw agreement 94.1%, Cohen's kappa 3-class = 0.88, linear-weighted = 0.93; MAJOR-vs-not: raw 100.0%, kappa = 1.00
- B vs C: raw agreement 76.5%, Cohen's kappa 3-class = 0.57, linear-weighted = 0.64; MAJOR-vs-not: raw 88.2%, kappa = 0.76
- Fleiss' kappa (3 raters, n = 17): 3-class = 0.70; MAJOR-vs-not = 0.84
