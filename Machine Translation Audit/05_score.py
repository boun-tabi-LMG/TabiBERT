"""Step 5: score the filled rater workbooks.

Usage: python 05_score.py sample_collected/rater_A_*.xlsx sample_collected/rater_B_*.xlsx [sample_collected/rater_C_*.xlsx]
Optional: --exclude DATASET (repeatable) drops a dataset from the ratings, the released CSV and all statistics.
The rater label is the token right after "rater_" in the file name (rater_A_Name.xlsx -> "A"); names never reach the outputs.

Reports, for the MAIN stratum (headline) and separately for the OUTLIER stratum:
  * per-rater rating distribution;
  * adjudicated label per item = majority vote; a three-way split (one vote each) is resolved to the more severe
    label (pre-specified, conservative); the number of such splits and the rate under the median rule are reported
    as a sensitivity check;
  * pooled MAJOR rate, MINOR-or-worse rate and task-validity failure rate, each with a Wilson 95% interval;
  * per-dataset adjudicated counts (descriptive; n = 20 per dataset is too small for per-dataset intervals);
  * agreement: pairwise raw agreement, Cohen's kappa (3-class, linear-weighted, MAJOR-vs-not), and with >= 3 raters
    Fleiss' kappa (3-class and MAJOR-vs-not).
Writes sample/audit_results.md, sample/audit_results.csv and sample/ratings_anonymized.csv
(item_id, dataset, stratum, rater, rating, task_valid, comment), and prints a draft sentence for Section 7.3.
"""
import os, sys, math, json, itertools
from collections import Counter
import pandas as pd
from audit_config import SAMPLE_DIR

SEV = {"OK": 0, "MINOR": 1, "MAJOR": 2}

def wilson(k, n, z=1.96):
    if n == 0: return (float("nan"), float("nan"))
    p = k / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))

def cohen_kappa(a, b, weight=None):
    """Cohen's kappa. weight(x, y) in [0, 1] is the credit for a pair of labels (None = exact agreement only)."""
    n = len(a); cats = sorted(set(a) | set(b)); w = weight or (lambda x, y: 1.0 if x == y else 0.0)
    ca, cb = Counter(a), Counter(b)
    po = sum(w(x, y) for x, y in zip(a, b)) / n
    pe = sum(w(i, j) * (ca[i] / n) * (cb[j] / n) for i in cats for j in cats)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0

def linear_weight(x, y):  # x, y are severity levels 0..2
    return 1.0 - abs(x - y) / 2.0

def fleiss_kappa(table):  # table: list of Counters (one per item), all with the same total
    N = len(table); n = sum(table[0].values()); cats = set(c for t in table for c in t)
    P_i = [(sum(v * v for v in t.values()) - n) / (n * (n - 1)) for t in table]
    P_bar = sum(P_i) / N
    p_j = {c: sum(t.get(c, 0) for t in table) / (N * n) for c in cats}
    P_e = sum(v * v for v in p_j.values())
    return (P_bar - P_e) / (1 - P_e) if P_e < 1 else 1.0

def adjudicate(labels):
    """Majority vote; a tie (e.g. one vote each for OK/MINOR/MAJOR) goes to the more severe label."""
    cnt = Counter(labels); top = cnt.most_common()
    if len(top) == 1 or top[0][1] > top[1][1]:
        return top[0][0]
    tied = [c for c, k in top if k == top[0][1]]
    return max(tied, key=lambda c: SEV[c])

def median_label(labels):
    s = sorted(labels, key=lambda c: SEV[c]); return s[len(s) // 2]

def is_tie(labels):
    top = Counter(labels).most_common(); return len(top) > 1 and top[0][1] == top[1][1]

args = sys.argv[1:]; EXCLUDE = set()
while "--exclude" in args:
    i = args.index("--exclude"); EXCLUDE.add(args[i + 1]); del args[i:i + 2]
paths = args
assert len(paths) >= 2, "need at least two filled rater workbooks"
items = {json.loads(l)["item_id"]: json.loads(l) for l in open(os.path.join(SAMPLE_DIR, "sample_items.jsonl"), encoding="utf-8")}
frames = []
for p in paths:
    df = pd.read_excel(p, sheet_name="Items")[["item_id", "rating", "task_valid", "comment"]]
    df["rater"] = os.path.basename(p)[len("rater_"):].split("_")[0].split(".")[0]
    frames.append(df)
R = pd.concat(frames)
R["rating"] = R.rating.astype(str).str.strip().str.upper().replace({"NAN": ""})
R["task_valid"] = R.task_valid.astype(str).str.strip().str.upper().replace({"NAN": ""})
R["dataset"] = R.item_id.map(lambda i: items[i]["dataset"]); R["stratum"] = R.item_id.map(lambda i: items[i]["stratum"])
if EXCLUDE:
    print(f"excluding datasets {sorted(EXCLUDE)}: {int(R.dataset.isin(EXCLUDE).sum())} rating rows dropped"); R = R[~R.dataset.isin(EXCLUDE)]
R[["item_id", "dataset", "stratum", "rater", "rating", "task_valid", "comment"]].sort_values(["stratum", "item_id", "rater"]) \
    .to_csv(os.path.join(SAMPLE_DIR, "ratings_anonymized.csv"), index=False, encoding="utf-8")
missing = R[~R.rating.isin(SEV)]
if len(missing):
    print(f"WARNING: {len(missing)} unrated/invalid rating cells (excluded):\n", missing[["rater", "item_id", "rating"]].to_string(index=False))
R = R[R.rating.isin(SEV)]
raters = sorted(R.rater.unique())

out = [f"# Translation adequacy audit: results ({len(raters)} raters: {', '.join(raters)})\n"]
results_rows = []
for stratum in ["main", "outlier"]:
    S = R[R.stratum == stratum]
    if S.empty: continue
    wide = S.pivot_table(index="item_id", columns="rater", values="rating", aggfunc="first").dropna()
    n_all = S.item_id.nunique(); n = len(wide)
    adj = wide.apply(lambda r: adjudicate(list(r)), axis=1)
    adj_med = wide.apply(lambda r: median_label(list(r)), axis=1)
    ties = wide.apply(lambda r: is_tie(list(r)), axis=1)
    tv = S.groupby("item_id").task_valid.apply(lambda s: "NO" if (s == "NO").sum() * 2 >= len(s) else ("YES" if (s == "YES").any() else "UNSURE")).reindex(wide.index)
    k_major = int((adj == "MAJOR").sum()); k_minor_plus = int((adj != "OK").sum()); k_tv = int((tv == "NO").sum())
    k_major_med = int((adj_med == "MAJOR").sum()); k_any = int((wide == "MAJOR").any(axis=1).sum()); k_all = int((wide == "MAJOR").all(axis=1).sum())
    lo, hi = wilson(k_major, n); lo2, hi2 = wilson(k_minor_plus, n); lo3, hi3 = wilson(k_tv, n)
    out.append(f"## Stratum: {stratum} (n = {n} items rated by all {len(raters)} raters" + (f"; {n_all - n} item(s) dropped for a missing rating" if n_all != n else "") + ")\n")
    out.append(f"- MAJOR (meaning changed), majority vote: {k_major}/{n} = {100*k_major/n:.1f}% (95% Wilson CI {100*lo:.1f}-{100*hi:.1f}%)")
    out.append(f"  - sensitivity: {int(ties.sum())} tie(s) resolved to the more severe label; under the median rule MAJOR = {k_major_med}/{n} = {100*k_major_med/n:.1f}%; "
               f"MAJOR by any rater {k_any}/{n}; by all raters {k_all}/{n}")
    out.append(f"- MINOR or worse: {k_minor_plus}/{n} = {100*k_minor_plus/n:.1f}% (CI {100*lo2:.1f}-{100*hi2:.1f}%)")
    out.append(f"- Task validity broken (gold no longer holds): {k_tv}/{n} = {100*k_tv/n:.1f}% (CI {100*lo3:.1f}-{100*hi3:.1f}%)\n")
    out.append("Per-rater rating distribution:\n")
    out.append(S.pivot_table(index="rater", columns="rating", values="item_id", aggfunc="count", fill_value=0).to_markdown())
    out.append("\nPer-dataset adjudicated counts (descriptive only):\n")
    per = pd.DataFrame({"dataset": adj.index.map(lambda i: items[i]["dataset"]), "adj": adj.values, "tv": tv.values})
    out.append(per.pivot_table(index="dataset", columns="adj", values="tv", aggfunc="count", fill_value=0).to_markdown())
    out.append("\nInter-rater agreement:\n")
    kappa_bin = None
    for a, b in itertools.combinations(raters, 2):
        x, y = list(wide[a]), list(wide[b]); xs, ys = [SEV[v] for v in x], [SEV[v] for v in y]
        raw = sum(i == j for i, j in zip(x, y)) / n
        k3 = cohen_kappa(x, y); kw = cohen_kappa(xs, ys, linear_weight)
        xb, yb = [v == "MAJOR" for v in x], [v == "MAJOR" for v in y]
        k2 = cohen_kappa(xb, yb); raw2 = sum(i == j for i, j in zip(xb, yb)) / n
        out.append(f"- {a} vs {b}: raw agreement {100*raw:.1f}%, Cohen's kappa 3-class = {k3:.2f}, linear-weighted = {kw:.2f}; "
                   f"MAJOR-vs-not: raw {100*raw2:.1f}%, kappa = {k2:.2f}")
        kappa_bin = k2
    if len(raters) >= 3:
        table3 = [Counter(row.tolist()) for _, row in wide.iterrows()]
        tableb = [Counter(["MAJOR" if v == "MAJOR" else "NOT" for v in row.tolist()]) for _, row in wide.iterrows()]
        fk3, fkb = fleiss_kappa(table3), fleiss_kappa(tableb)
        out.append(f"- Fleiss' kappa ({len(raters)} raters, n = {n}): 3-class = {fk3:.2f}; MAJOR-vs-not = {fkb:.2f}")
        kappa_text = f"Fleiss' kappa = {fkb:.2f} for meaning-changed versus not ({fk3:.2f} on the three-level scale)"
    else:
        kappa_text = f"Cohen's kappa = {kappa_bin:.2f} for meaning-changed versus not"
    out.append("")
    results_rows.append(dict(stratum=stratum, n=n, raters=len(raters), major=k_major, major_rate=k_major/n, major_ci_lo=lo, major_ci_hi=hi,
                             major_median_rule=k_major_med, major_any=k_any, major_all=k_all, ties=int(ties.sum()),
                             minor_plus=k_minor_plus, task_invalid=k_tv, task_invalid_ci_lo=lo3, task_invalid_ci_hi=hi3))
    if stratum == "main":
        pl = lambda k: "item" if k == 1 else "items"
        n_ds = R.dataset.nunique()
        sent = (f"By majority vote among {len(raters)} raters over {n} test-split items ({n//n_ds} per dataset) from the {n_ds} datasets we translated, "
                f"meaning was changed in {k_major} {pl(k_major)} ({100*k_major/n:.1f} per cent; 95 per cent Wilson interval {100*lo:.1f}-{100*hi:.1f}), "
                f"a further {k_minor_plus-k_major} had lesser flaws, and the gold label or gold document no longer held for {k_tv} {pl(k_tv)} "
                f"({100*k_tv/n:.1f} per cent); {kappa_text}.")
        out.append("Draft for Section 7.3:\n\n> " + sent + "\n")
        dis = wide[(wide == "MAJOR").any(axis=1) & (wide.nunique(axis=1) > 1)]
        out.append(f"Items with a MAJOR vote on which the raters disagree: {len(dis)}\n")
        if len(dis):
            dis = dis.copy(); dis["adjudicated"] = adj.reindex(dis.index); out.append(dis.to_markdown() + "\n")

pd.DataFrame(results_rows).to_csv(os.path.join(SAMPLE_DIR, "audit_results.csv"), index=False)
open(os.path.join(SAMPLE_DIR, "audit_results.md"), "w", encoding="utf-8").write("\n".join(out))
print("\n".join(out))
