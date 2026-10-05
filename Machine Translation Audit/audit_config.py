"""Shared configuration for the TabiBench translation-adequacy audit.

Each entry maps one of the seven GPT-4.1-translated datasets to the local pipeline
folders under ../ (sft/). `fields` maps the *translated* column of the released
TR dataset to the results folder that holds its {idx}-idx_{uuid}.json pairs.
`gold` is the column that carries the task-validity context (label or gold document).
"""
import os

SFT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT_ROOT = os.path.dirname(os.path.abspath(__file__))
PAIRS_DIR = os.path.join(OUT_ROOT, "pairs")
INTEG_DIR = os.path.join(OUT_ROOT, "integrity")
SAMPLE_DIR = os.path.join(OUT_ROOT, "sample")
SEED = 20260924
N_PER_DATASET = 20
N_OUTLIERS_PER_DATASET = 3  # extra, separately labelled stratum

DATASETS = {
    "MedNLI": dict(root="academic_datasets/MedNLI", ds="MedNLI-TR",
                   fields={"sentence1": "results_sentence_one", "sentence2": "results_sentence_two"},
                   gold="label", task="nli", code=False),
    "PubMedRCT": dict(root="academic_datasets/Pubmed", ds="PubmedRCT-10K-TR",
                      fields={"text": "results"}, gold="label", task="classification", code=False),
    "SciCite": dict(root="academic_datasets/SciCite", ds="SciCite-TR",
                    fields={"text": "results"}, gold="label", task="classification", code=False),
    "Apps": dict(root="code_data_generation/Apps", ds="Apps-TR",
                 fields={"query": "results"}, gold="doc", task="retrieval", code=True),
    # NOTE: in CodeSearchNet-21K-TR the translated docstring is stored in `doc`; `query` holds the code.
    "CodeSearchNet": dict(root="code_data_generation/CodeSearchNet", ds="CodeSearchNet-21K-TR",
                          fields={"doc": "results"}, gold="query", task="retrieval", code=True),
    "CosQA": dict(root="code_data_generation/CosQA", ds="CosQA-TR",
                  fields={"query": "results"}, gold="doc", task="retrieval", code=True),
    "StackOverflowQA": dict(root="code_data_generation/StackoverflowQA", ds="StackoverflowQA-TR",
                            fields={"query": "results_queries", "doc": "results_corpus"},
                            gold=None, task="retrieval-both", code=True),
}

PROMPT_ECHO_MARKERS = ["Yukarıdaki metni", "yerelleştir", "Yerelleştirilmiş metin"]
EN_STOPWORDS = {"the", "and", "of", "to", "is", "are", "with", "for", "this", "that", "in", "on",
                "be", "was", "were", "has", "have", "it", "as", "by", "from", "not", "or", "an", "at",
                "which", "we", "our", "their", "these", "those", "than", "then", "when", "where"}
