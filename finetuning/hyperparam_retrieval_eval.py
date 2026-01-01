import numpy as np
import torch
from collections import defaultdict

from transformers import AutoTokenizer, AutoModel
from datasets import load_dataset

# ---------- Embedding (batched + mask-aware mean pooling + optional L2 norm) ----------
def embed_texts(model, tokenizer, texts, batch_size, max_length, device="cuda", l2_normalize=True):
    model.eval()
    all_embs = []

    with torch.no_grad():
        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            enc = tokenizer(
                batch,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=max_length,
            ).to(device)

            out = model(**enc)
            token_emb = out.last_hidden_state                           # [B, T, H]
            mask = enc["attention_mask"].unsqueeze(-1).float()           # [B, T, 1]

            # mean over real tokens only
            summed = (token_emb * mask).sum(dim=1)                      # [B, H]
            counts = mask.sum(dim=1).clamp(min=1e-9)                    # [B, 1]
            emb = summed / counts                                       # [B, H]

            if l2_normalize:
                emb = torch.nn.functional.normalize(emb, p=2, dim=1)

            all_embs.append(emb.cpu().numpy())

    return np.concatenate(all_embs, axis=0)

# ---------- Retrieval-style eval: corpus + queries + qrels ----------
def build_retrieval_format(hf_split, query_key="anchor", doc_key="positive"):
    """
    Converts (anchor, positive) pairs into:
      - queries: unique anchors
      - corpus:  unique positives
      - qrels:   mapping query_idx -> set(doc_idx) of relevant docs
    """
    anchor2pos = defaultdict(set)
    for ex in hf_split:
        anchor2pos[ex[query_key]].add(ex[doc_key])

    queries = list(anchor2pos.keys())
    doc_set = set()
    for s in anchor2pos.values():
        doc_set |= s
    corpus = list(doc_set)

    qid = {q: i for i, q in enumerate(queries)}
    did = {d: j for j, d in enumerate(corpus)}

    qrels = [set() for _ in range(len(queries))]
    for q, pos_set in anchor2pos.items():
        qi = qid[q]
        for d in pos_set:
            qrels[qi].add(did[d])

    return queries, corpus, qrels


def ndcg_cut_at_k(scores, qrels, k):
    """
    BEIR/MTEB-style nDCG@k for binary qrels:
      nDCG@k = mean_q DCG@k / IDCG@k
    """
    n_queries = scores.shape[0]
    denom_cache = {}  # IDCG for a given (#relevant, k)

    ndcgs = []
    for qi in range(n_queries):
        rel_docs = qrels[qi]
        if not rel_docs:
            continue

        row = scores[qi]
        kk = min(k, row.shape[0])

        # top-k indices sorted by score desc
        topk = np.argpartition(-row, kk - 1)[:kk]
        topk = topk[np.argsort(-row[topk])]

        # DCG
        dcg = 0.0
        for rank, di in enumerate(topk):
            if di in rel_docs:
                dcg += 1.0 / np.log2(rank + 2.0)

        # IDCG
        r = min(len(rel_docs), kk)
        key = (r, kk)
        if key not in denom_cache:
            denom_cache[key] = sum(1.0 / np.log2(rank + 2.0) for rank in range(r))
        idcg = denom_cache[key]

        ndcgs.append(dcg / idcg if idcg > 0 else 0.0)

    return float(np.mean(ndcgs)) if ndcgs else 0.0


def eval_retrieval(model_name,
                   dataset_split,
                   max_seq_length,
                   batch_size,
                   k_values: list = [1, 3, 5, 10, 20]):
    """
    Evaluate a fine-tuned model on a retrieval task.
    
    Args:
        model_path (str): Path to the pre-trained model
    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name).to(device)


    # 1) Convert to retrieval format
    queries, corpus, qrels = build_retrieval_format(dataset_split,
                                                    query_key="anchor",
                                                    doc_key="positive")
    print(
        f"#queries={len(queries)}  #corpus_docs={len(corpus)}  avg_rels/query={np.mean([len(x) for x in qrels]):.2f}"
    )

    # 2) Embed + score against the whole corpus
    print("Embedding queries...")
    Q = embed_texts(model,
                    tokenizer,
                    queries,
                    batch_size=batch_size,
                    max_length=max_seq_length,
                    device=device,
                    l2_normalize=True)

    print("Embedding corpus...")
    D = embed_texts(model,
                    tokenizer,
                    corpus,
                    batch_size=batch_size,
                    max_length=max_seq_length,
                    device=device,
                    l2_normalize=True)

    # cosine scores (since we L2-normalized, dot product == cosine)
    scores = Q @ D.T  # shape: [n_queries, n_docs]

    # Evaluate nDCG@k (retrieval-style)
    for k in k_values:
        ndcg = ndcg_cut_at_k(scores, qrels, k)
        print(f"nDCG@{k}: {ndcg:.4f}")
