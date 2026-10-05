"""Step 2: exhaustive automated integrity checks over every EN-TR pair (100% coverage, no sampling).

Flags per item:
  empty_tr        translation is empty
  identical       translation identical to the source (untranslated)
  prompt_echo     translation contains the instruction text (model echoed the prompt)
  en_residue      non-code text whose tokens are >8% English stopwords (likely untranslated span)
  len_ratio       len(tr)/len(en) in characters
  len_z           z-score of len_ratio within (dataset, field)
  len_outlier     |len_z| > 2  -> candidate omission/addition; becomes the outlier stratum in the sample
  fence_mismatch  (StackOverflowQA answers only) number of ``` fences differs between EN and TR
Writes integrity/flags_{dataset}__{field}.csv and integrity/summary.md
"""
import os, re, json, math
import pandas as pd
from audit_config import PAIRS_DIR, INTEG_DIR, DATASETS, PROMPT_ECHO_MARKERS, EN_STOPWORDS

os.makedirs(INTEG_DIR, exist_ok=True)
tok = re.compile(r"[A-Za-zÇçĞğİıÖöŞşÜü']+")

def en_residue(text):
    words = [w.lower() for w in tok.findall(text)]
    if len(words) < 6:
        return 0.0
    return sum(w in EN_STOPWORDS for w in words) / len(words)

rows_summary = []
for name, cfg in DATASETS.items():
    for field in cfg["fields"]:
        recs = [json.loads(l) for l in open(os.path.join(PAIRS_DIR, f"{name}__{field}.jsonl"), encoding="utf-8")]
        df = pd.DataFrame(recs)
        df["len_en"] = df.text_en.str.len()
        df["len_tr"] = df.text_tr.str.len()
        df["empty_tr"] = df.text_tr.str.strip().eq("")
        df["identical"] = df.text_tr.str.strip().eq(df.text_en.str.strip()) & ~df.empty_tr
        df["prompt_echo"] = df.text_tr.apply(lambda t: any(m.lower() in t.lower() for m in PROMPT_ECHO_MARKERS))
        df["en_residue_ratio"] = df.text_tr.apply(en_residue)
        df["en_residue"] = (df.en_residue_ratio > 0.08) & (not cfg["code"])
        df["len_ratio"] = df.len_tr / df.len_en.clip(lower=1)
        ok = ~df.empty_tr
        mu, sd = df.loc[ok, "len_ratio"].mean(), df.loc[ok, "len_ratio"].std(ddof=0) or 1.0
        df["len_z"] = (df.len_ratio - mu) / sd
        df["len_outlier"] = ok & (df.len_z.abs() > 2)
        if name == "StackOverflowQA" and field == "doc":
            df["fence_mismatch"] = df.text_en.str.count("```") != df.text_tr.str.count("```")
        else:
            df["fence_mismatch"] = False
        df["any_flag"] = df[["empty_tr", "identical", "prompt_echo", "en_residue", "len_outlier", "fence_mismatch"]].any(axis=1)
        df.to_csv(os.path.join(INTEG_DIR, f"flags_{name}__{field}.csv"), index=False, encoding="utf-8")
        rows_summary.append(dict(dataset=name, field=field, n=len(df), empty_tr=int(df.empty_tr.sum()),
                                 identical=int(df.identical.sum()), prompt_echo=int(df.prompt_echo.sum()),
                                 en_residue=int(df.en_residue.sum()), len_outlier=int(df.len_outlier.sum()),
                                 fence_mismatch=int(df.fence_mismatch.sum()), mean_len_ratio=round(mu, 3),
                                 sd_len_ratio=round(sd, 3), dup_result_files=int((df.n_files > 1).sum())))
        print(f"{name:16} {field:10} n={len(df):6} empty={int(df.empty_tr.sum()):3} identical={int(df.identical.sum()):4} "
              f"echo={int(df.prompt_echo.sum()):3} residue={int(df.en_residue.sum()):4} len_out={int(df.len_outlier.sum()):4} "
              f"fence={int(df.fence_mismatch.sum()):3} ratio={mu:.2f}+-{sd:.2f}")

summ = pd.DataFrame(rows_summary)
summ.to_csv(os.path.join(INTEG_DIR, "summary.csv"), index=False)
with open(os.path.join(INTEG_DIR, "summary.md"), "w", encoding="utf-8") as f:
    f.write("# Automated integrity checks (100% of translated items)\n\n")
    f.write(summ.to_markdown(index=False))
    f.write("\n\nNotes: gold code/document fields in Apps, CodeSearchNet and CosQA are copied from the English source "
            "by construction (see each construct_Dataset.ipynb), so they are not translated and need no check. "
            "`en_residue` is a heuristic and is not applied to code-related datasets.\n")
print("written to", INTEG_DIR)
