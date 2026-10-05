"""Step 3: build the stratified audit sample from the TEST split of each released TR dataset.

For every test row, the translated field(s) are matched back (exact text match) to the EN-TR pairs,
recovering the English source and the pipeline idx. Then, with a fixed seed:
  * N_PER_DATASET items per dataset (StackOverflowQA: half rated on the query, half on the answer);
  * plus up to N_OUTLIERS_PER_DATASET additional items whose translated field is a length-ratio outlier
    (stratum = "outlier"), so that outliers are examined without biasing the headline rate.
Writes sample/sample_items.jsonl (rater-facing content) and sample/answer_key_do_not_share.csv (idx mapping).
"""
import os, json, random
import pandas as pd
from datasets import load_from_disk
from audit_config import SFT_ROOT, PAIRS_DIR, INTEG_DIR, SAMPLE_DIR, DATASETS, SEED, N_PER_DATASET, N_OUTLIERS_PER_DATASET

os.makedirs(SAMPLE_DIR, exist_ok=True)
rng = random.Random(SEED)

def load_pairs(name, field):
    recs = [json.loads(l) for l in open(os.path.join(PAIRS_DIR, f"{name}__{field}.jsonl"), encoding="utf-8")]
    by_tr = {}
    for r in recs:
        by_tr.setdefault(r["text_tr"], []).append(r)
    return by_tr

def load_outliers(name, field):
    df = pd.read_csv(os.path.join(INTEG_DIR, f"flags_{name}__{field}.csv"))
    return set(df.loc[df.len_outlier, "idx"].tolist()), dict(zip(df.idx, df.len_z))

items, key, report = [], [], []
for name, cfg in DATASETS.items():
    ds = load_from_disk(os.path.join(SFT_ROOT, cfg["root"], cfg["ds"]))["test"]
    fields = list(cfg["fields"])
    pairs = {f: load_pairs(name, f) for f in fields}
    outl = {f: load_outliers(name, f) for f in fields}
    rows, unmatched, ambiguous = [], 0, 0
    for i, ex in enumerate(ds):
        row = dict(test_row=i, gold=ex.get(cfg["gold"]) if cfg["gold"] else None)
        okrow = True
        for f in fields:
            cands = pairs[f].get(ex[f], [])
            if not cands:
                okrow = False; break
            if len(cands) > 1:
                ambiguous += 1
            r = cands[0]
            row[f"{f}_en"], row[f"{f}_tr"], row[f"{f}_idx"] = r["text_en"], r["text_tr"], r["idx"]
            row[f"{f}_len_z"] = outl[f][1].get(r["idx"], 0.0)
            row[f"{f}_outlier"] = r["idx"] in outl[f][0]
        if okrow:
            # keep untranslated gold context for retrieval items
            if cfg["task"] == "retrieval":
                row["gold_en"] = ex[cfg["gold"]]
            rows.append(row)
        else:
            unmatched += 1
    report.append(f"{name:16} test={len(ds):5} matched={len(rows):5} unmatched={unmatched:3} ambiguous_tr_text={ambiguous}")

    # ---- main stratum ----
    if cfg["task"] == "retrieval-both":
        half = N_PER_DATASET // 2
        pool_q = [r for r in rows if not r["query_outlier"]]
        pool_d = [r for r in rows if not r["doc_outlier"]]
        pick = [(r, "query") for r in rng.sample(pool_q, half)]
        used = {r["test_row"] for r, _ in pick}
        pick += [(r, "doc") for r in rng.sample([r for r in pool_d if r["test_row"] not in used], N_PER_DATASET - half)]
    else:
        main_field = fields[0]
        pool = [r for r in rows if not any(r[f"{f}_outlier"] for f in fields)]
        pick = [(r, None) for r in rng.sample(pool, N_PER_DATASET)]
    strata = [("main", r, f) for r, f in pick]
    # ---- outlier stratum ----
    used = {r["test_row"] for r, _ in pick}
    out_pool = [r for r in rows if r["test_row"] not in used and any(r[f"{f}_outlier"] for f in fields)]
    for r in rng.sample(out_pool, min(N_OUTLIERS_PER_DATASET, len(out_pool))):
        f = next((f for f in fields if r[f"{f}_outlier"]), fields[0])
        strata.append(("outlier", r, f if cfg["task"] == "retrieval-both" else None))

    for k, (stratum, r, rated_field) in enumerate(strata, 1):
        item_id = f"{name[:6].upper()}-{k:03d}"
        it = dict(item_id=item_id, dataset=name, task=cfg["task"], stratum=stratum, split="test")
        if cfg["task"] == "nli":
            it.update(rated_field="premise + hypothesis",
                      english_source=f"PREMISE: {r['sentence1_en']}\n\nHYPOTHESIS: {r['sentence2_en']}",
                      turkish_translation=f"ÖNCÜL: {r['sentence1_tr']}\n\nHİPOTEZ: {r['sentence2_tr']}",
                      task_context=f"Gold label: {r['gold']}")
        elif cfg["task"] == "classification":
            it.update(rated_field="text", english_source=r["text_en"], turkish_translation=r["text_tr"],
                      task_context=f"Gold label: {r['gold']}")
        elif cfg["task"] == "retrieval":
            f = fields[0]
            it.update(rated_field=f, english_source=r[f"{f}_en"], turkish_translation=r[f"{f}_tr"],
                      task_context="Gold document (English, unchanged; first 1200 chars):\n" + str(r["gold_en"])[:1200])
        else:  # StackOverflowQA
            f = rated_field
            other = "doc" if f == "query" else "query"
            it.update(rated_field=("question" if f == "query" else "answer"),
                      english_source=r[f"{f}_en"], turkish_translation=r[f"{f}_tr"],
                      task_context=f"Paired {'answer' if other == 'doc' else 'question'} (English, first 800 chars):\n" + r[f"{other}_en"][:800])
        items.append(it)
        key.append(dict(item_id=item_id, dataset=name, stratum=stratum, test_row=r["test_row"],
                        rated_field=it["rated_field"],
                        **{f"{f}_idx": r[f"{f}_idx"] for f in fields},
                        **{f"{f}_len_z": round(r[f"{f}_len_z"], 2) for f in fields}))

with open(os.path.join(SAMPLE_DIR, "sample_items.jsonl"), "w", encoding="utf-8") as f:
    for it in items:
        f.write(json.dumps(it, ensure_ascii=False) + "\n")
pd.DataFrame(key).to_csv(os.path.join(SAMPLE_DIR, "answer_key_do_not_share.csv"), index=False, encoding="utf-8")
print("\n".join(report))
n_main = sum(i["stratum"] == "main" for i in items); n_out = len(items) - n_main
print(f"\nsampled: {n_main} main + {n_out} outlier = {len(items)} items  (seed {SEED}) -> {SAMPLE_DIR}")
