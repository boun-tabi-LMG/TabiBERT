from dataloaders.dataloaders import (
    build_review_dataloader, build_news_cat_dataloader,
    build_bil_tweet_news_dataloader, gender_hate_speech_dataloader,
    build_pubmed_RCT_dataloader, build_sci_cite_dataloader,
    build_thesis_abstract_dataloader, build_multinli_dataloader,
    build_snli_dataloader, build_med_nli_dataloader, build_stsb_tr_dataloader,
    build_sick_tr_dataloader, build_wiki_ner_dataloader,
    build_wiki_ann_ner_dataloader, build_pos_ud_boun_dataloader,
    build_pos_ud_imst_dataloader, build_xtreme_qa_dataloader,
    build_tquad_qa_dataloader, build_retrieval_dataloader)

from omegaconf import DictConfig
from torch.utils.data import DataLoader
from composer.utils import dist
from transformers import default_data_collator, DataCollatorWithPadding, AutoTokenizer
from dataloaders.qa import DataCollatorForQuestionAnswering
import torch


def custom_collate_fn(batch):
    batch_out = {}
    for key in batch[0]:
        # If the key is 'text', keep as list of strings
        if key == "text":
            batch_out[key] = [item[key] for item in batch]
        # If the key is 'word_ids', stack as a tensor (should be same shape)
        elif key == "word_ids":
            # If already tensor, stack; if list, convert to tensor first
            word_ids = [
                item[key] if isinstance(item[key], torch.Tensor) else
                torch.tensor(item[key]) for item in batch
            ]
            batch_out[key] = torch.stack(word_ids)
        else:
            batch_out[key] = torch.stack([item[key] for item in batch])
    return batch_out


def build_dataset(cfg: DictConfig,
                  dataset_name: str,
                  split: str):
    if 'ytu' in cfg.tokenizer_name or 'TurkishBERTweet' in cfg.tokenizer_name:
        is_lower = True
    else:
        is_lower = False
    if dataset_name == "news_cat":
        dataset = build_news_cat_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
    elif dataset_name == "prod_review":
        dataset = build_review_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
    elif dataset_name == "bil_tweet_news":
        dataset = build_bil_tweet_news_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
    elif dataset_name == "gender_hate_speech":
        dataset = gender_hate_speech_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
    elif dataset_name == "pubmed_RCT":
        dataset = build_pubmed_RCT_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
    elif dataset_name == "sci_cite_TR":
        dataset = build_sci_cite_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
    elif dataset_name == "thesis_abstract":
        dataset = build_thesis_abstract_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
    elif dataset_name == "wiki_ner":
        dataset, tag2id = build_wiki_ner_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
        cfg.tag2id = tag2id
        return dataset, tag2id
    elif dataset_name == "wiki_ann_ner":
        dataset, _ = build_wiki_ann_ner_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
    elif dataset_name == "pos_ud_boun":
        dataset, tag2id = build_pos_ud_boun_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
        cfg.tag2id = tag2id
    elif dataset_name == "pos_ud_imst":
        dataset, tag2id = build_pos_ud_imst_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
        cfg.tag2id = tag2id
    elif dataset_name == "sts":
        dataset = build_stsb_tr_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
    elif dataset_name == "sick_tr":
        dataset = build_sick_tr_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
    elif dataset_name == "xquad_qa":
        dataset = build_xtreme_qa_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
    elif dataset_name == "tquad2_qa":
        dataset = build_tquad_qa_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
    elif dataset_name == "multinli":
        dataset = build_multinli_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
    elif dataset_name == "snli":
        dataset = build_snli_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
    elif dataset_name == "med_nli":
        dataset = build_med_nli_dataloader(
            split=split,
            tokenizer_name=cfg.tokenizer_name,
            max_seq_length=cfg.max_seq_len,
            is_lower=is_lower,
        )
    else:
        retrieval_tasks = {
            'wmt16': 0,
            'msmarco': 1,
            'scifact': 2,
            'fiqa': 3,
            'nfcorpus': 4,
            'quora': 5,
        }
        if dataset_name in retrieval_tasks.keys():
            dataset = build_retrieval_dataloader(
                split=split,
                tokenizer_name=cfg.tokenizer_name,
                max_seq_length=cfg.max_seq_len,
                is_lower=is_lower,
                retrieval_task_id=retrieval_tasks[dataset_name],
            )
        else:
            raise ValueError(
                f"Not sure how to build dataloader for task type: {dataset_name}"
            )
    return dataset


def custom_collate_fn(batch):
    # Separate tensor fields and text fields
    batch_out = {}
    # Assume all keys are present in the first item
    for key in batch[0]:
        if key == "text":
            batch_out[key] = [item[key] for item in batch]
        else:
            batch_out[key] = torch.stack([item[key] for item in batch])
    return batch_out


def build_my_dataloader(cfg: DictConfig,
                        dataset_name: str,
                        device_batch_size: int,
                        split: str):
    """Create a dataloader for classification, NLI, NER, or POS task."""
    result = build_dataset(cfg, dataset_name, split)

    # Handle cases where build_dataset returns a tuple (dataset, metadata)
    if isinstance(result, tuple):
        dataset = result[0]
    else:
        dataset = result

    # Use custom collate for NER and POS, and QA, default for others
    if dataset_name in ["wiki_ner", "wiki_ann_ner"]:
        collate_fn = custom_collate_fn
    elif dataset_name in ["xquad_qa", "tquad2_qa"]:
        collate_fn = DataCollatorForQuestionAnswering()
    else:
        collate_fn = default_data_collator

    dataloader = DataLoader(
        dataset,
        collate_fn=collate_fn,
        batch_size=device_batch_size,
        sampler=dist.get_sampler(dataset,
                                 drop_last=cfg.drop_last,
                                 shuffle=cfg.shuffle),
        num_workers=cfg.num_workers,
        pin_memory=cfg.get("pin_memory", True),
        prefetch_factor=cfg.get("prefetch_factor", 2),
        persistent_workers=cfg.get("persistent_workers", True),
        timeout=cfg.get("timeout", 0),
    )

    return dataloader
