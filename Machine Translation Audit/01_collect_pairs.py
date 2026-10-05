"""Step 1: collect every EN-TR pair written by the translation pipeline into one JSONL per (dataset, field).

Reads results*/{idx}-idx_{uuid}.json (keys: idx, text-en, text-tr) and writes pairs/{dataset}__{field}.jsonl
with one record per idx: {"idx", "text_en", "text_tr", "n_files"} (n_files > 1 flags duplicate result files).
"""
import os, json, sys
from collections import defaultdict
from audit_config import SFT_ROOT, PAIRS_DIR, DATASETS

os.makedirs(PAIRS_DIR, exist_ok=True)
summary = []
for name, cfg in DATASETS.items():
    for field, rdir in cfg["fields"].items():
        path = os.path.join(SFT_ROOT, cfg["root"], rdir)
        by_idx = defaultdict(list)
        with os.scandir(path) as it:
            for e in it:
                if not e.name.endswith(".json"):
                    continue
                try:
                    idx = int(e.name.split("-idx")[0])
                except ValueError:
                    continue
                with open(e.path, encoding="utf-8") as f:
                    rec = json.load(f)
                assert rec.get("idx") == idx, (name, field, e.name)
                by_idx[idx].append((rec.get("text-en", ""), rec.get("text-tr", "")))
        out = os.path.join(PAIRS_DIR, f"{name}__{field}.jsonl")
        n_dup = 0
        with open(out, "w", encoding="utf-8") as f:
            for idx in sorted(by_idx):
                recs = by_idx[idx]
                if len(recs) > 1:
                    n_dup += 1
                en, tr = recs[0]
                f.write(json.dumps({"idx": idx, "text_en": en, "text_tr": tr if tr is not None else "",
                                    "n_files": len(recs)}, ensure_ascii=False) + "\n")
        max_idx = max(by_idx) if by_idx else -1
        summary.append((name, field, len(by_idx), max_idx + 1 - len(by_idx), n_dup))
        print(f"{name:16} {field:10} pairs={len(by_idx):6}  missing_idx={max_idx + 1 - len(by_idx):4}  dup_idx={n_dup}")

with open(os.path.join(PAIRS_DIR, "_summary.csv"), "w", encoding="utf-8") as f:
    f.write("dataset,field,n_pairs,n_missing_idx,n_duplicate_idx\n")
    for row in summary:
        f.write(",".join(map(str, row)) + "\n")
print("written to", PAIRS_DIR)
