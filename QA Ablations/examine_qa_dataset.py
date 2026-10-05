# Datasets:
# XQuad datase in HF: boun-tabilab/XQuAD-TR
# XQuad datase in HF: boun-tabilab/TQuad-2

# Models' paths: 
# - TabiBERT: boun-tabilab/TabiBERT
# - BERTurk: dbmdz/bert-base-turkish-cased
# - TurkishBERTweet: VRLLab/TurkishBERTweet
# - YTU-Cosmos-BERT: ytu-ce-cosmos/turkish-base-bert-uncased
# - mmBERT: mmBERT/base

# TASK:
# 1. Find the share of TQuAD/XQuAD examples over 512 tokens under each model's tokenizer;
# 2. Fine-tune all models with max_length 512.
# Before that: 
#      * settle the protocol (re-run the three 512-token baselines or declare their published scores already capped), 
#      * confirm the QA pipeline hard-truncates (no doc-stride),
#      * and check that XQuAD's '833-token' 95th percentile is not a copy of its 833-example train split. 

# Normal finetuning yamls are: under the finetuning/yamls folder.
# See finetuning/README.md for more details on how to run the finetuning.

# ----------------------------------------------------------------------------------------------
# Task 1: share of examples longer than MAX_LEN tokens under each model's tokenizer.
#
# Mirrors finetuning/dataloaders/qa.py::QADataset: the input is the (question, context) pair with
# special tokens, lowercased first for the uncased models (is_lower in finetuning/yamls/class-*.yaml).
# ">512" means the untruncated pair does not fit in 512 tokens, i.e. `truncation='only_second'`
# in QADataset would cut the context. Model paths follow finetuning/yamls/class-*.yaml.
#
# Usage: python QA Ablations/examine_qa_dataset.py [--max_len 512] [--out QA Ablations/qa_length_stats.csv]
# ----------------------------------------------------------------------------------------------
import argparse
import csv

import numpy as np
from datasets import load_dataset
from transformers import AutoTokenizer
from transformers.utils import logging as hf_logging

hf_logging.set_verbosity_error()  # silence "sequence length is longer than the max" warnings

DATASETS = ["boun-tabilab/XQuAD-TR", "boun-tabilab/TQuad-2"]

# name -> (tokenizer path, is_lower)
MODELS = {
    "TabiBERT": ("boun-tabilab/TabiBERT", False),
    "BERTurk": ("dbmdz/bert-base-turkish-cased", False),
    "TurkishBERTweet": ("VRLLab/TurkishBERTweet", True),
    "YTU-Cosmos-BERT": ("ytu-ce-cosmos/turkish-base-bert-uncased", True),
    "mmBERT": ("jhu-clsp/mmBERT-base", False),
}


def to_lower_tr(s: str) -> str:
    # same as QADataset.to_lower_tr
    return s.replace("I", "ı").lower()


def first_answer(answers):
    """(text, answer_start) of the first gold answer, or None. Handles XQuAD (dict) and TQuAD (list)."""
    if isinstance(answers, dict):
        texts, starts = answers.get("text", []), answers.get("answer_start", [])
    else:
        texts = [a["text"] for a in answers if "text" in a]
        starts = [a["answer_start"] for a in answers if "answer_start" in a]
    return (texts[0], starts[0]) if texts and starts else None


def length_stats(tok, split, is_lower, max_len):
    questions = [ex["question"] for ex in split]
    contexts = [ex["context"] for ex in split]
    answers = [first_answer(ex["answers"]) for ex in split]
    if is_lower:
        questions = [to_lower_tr(q) for q in questions]
        contexts = [to_lower_tr(c) for c in contexts]
        answers = [(to_lower_tr(a[0]), a[1]) if a else None for a in answers]

    lengths = np.array([len(ids) for ids in tok(questions, contexts, truncation=False)["input_ids"]])
    over = np.flatnonzero(lengths > max_len)

    # For over-length examples, how many lose their gold answer to only_second truncation?
    # (QADataset then sets start=end=0, i.e. trains/evaluates on a lost answer.)
    answer_lost = 0
    if len(over):
        enc = tok([questions[i] for i in over], [contexts[i] for i in over], truncation="only_second",
                  max_length=max_len, return_offsets_mapping=True)
        for j, i in enumerate(over):
            if answers[i] is None:
                continue
            text, start = answers[i]
            last_ctx_char = max(e for (_, e), sid in zip(enc["offset_mapping"][j], enc.sequence_ids(j)) if sid == 1)
            answer_lost += (start + len(text)) > last_ctx_char

    return {
        "n": len(lengths),
        "n_over": len(over),
        "pct_over": 100 * len(over) / len(lengths),
        "pct_answer_lost": 100 * answer_lost / len(lengths),
        "median": int(np.median(lengths)),
        "p95": int(np.percentile(lengths, 95)),
        "max": int(lengths.max()),
    }


def task1(max_len, out_path):
    data = {}
    for name in DATASETS:
        dd = load_dataset(name)
        # "all" = every split concatenated (XQuAD-TR: 833+178+179 = 1190 original rows)
        data[name.split("/")[-1]] = {**dd, "all": [ex for s in dd.values() for ex in s]}

    rows = []
    for model, (path, is_lower) in MODELS.items():
        tok = AutoTokenizer.from_pretrained(path)
        for ds_name, splits in data.items():
            for split_name, split in splits.items():
                rows.append({"model": model, "dataset": ds_name, "split": split_name,
                             **length_stats(tok, split, is_lower, max_len)})

    cols = ["dataset", "split", "model", "n", "n_over", "pct_over", "pct_answer_lost", "median", "p95", "max"]
    print(f"\nExamples with (question + context) > {max_len} tokens (special tokens included)\n")
    print(f"{'dataset':<10} {'split':<11} {'model':<16} {'n':>6} {'n_over':>7} {'%>'+str(max_len):>7} "
          f"{'%ans lost':>9} {'median':>7} {'p95':>6} {'max':>6}")
    for r in sorted(rows, key=lambda r: (r["dataset"], r["split"] != "all", r["split"], r["model"])):
        print(f"{r['dataset']:<10} {r['split']:<11} {r['model']:<16} {r['n']:>6} {r['n_over']:>7} "
              f"{r['pct_over']:>7.2f} {r['pct_answer_lost']:>9.2f} {r['median']:>7} {r['p95']:>6} {r['max']:>6}")

    with open(out_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows({c: (round(r[c], 3) if isinstance(r[c], float) else r[c]) for c in cols} for r in rows)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--max_len", type=int, default=512)
    ap.add_argument("--out", default="QA Ablations/qa_length_stats.csv")
    args = ap.parse_args()
    task1(args.max_len, args.out)
