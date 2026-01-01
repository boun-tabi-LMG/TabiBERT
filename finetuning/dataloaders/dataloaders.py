from transformers import AutoTokenizer, RobertaTokenizerFast
from dataloaders.nli_tr import NLIDataset
from dataloaders.stsb_tr import STSDataset, SICKReader, STSBReader
from dataloaders.text_classification import TextClassificationDataset
from dataloaders.news_cat import NewsCatDataset
from dataloaders.ner import NERDataset
from dataloaders.wiki_ann_ner import WikiANNNERDataset
from dataloaders.pos_ud import POSUDDataset
from dataloaders.qa import QADataset
from dataloaders.retrieval import RetrievalPairDataset

import sys
import csv
from datasets import load_dataset, concatenate_datasets, load_from_disk, Dataset, DatasetDict
import datasets
from conllu import parse_incr


def build_multinli_dataloader(split: str, tokenizer_name: str,
                         max_seq_length: int, is_lower: bool = False):
    """Build dataloader for MultiNLI dataset.
    
    Args:
        split (str): One of 'train', 'validation', or 'test'
        tokenizer_name (str): Name of the tokenizer to use
        max_seq_length (int): Maximum sequence length
        
    Returns:
        Dataset: A dataset for NLI task
    """
    if split == 'train':
        multi_nli = load_from_disk("/workspace/TabiBERT/finetuning/datasets/multinli_tr/train/")
    elif split == 'validation' or split == 'test':
        multi_nli = load_from_disk("/workspace/TabiBERT/finetuning/datasets/multinli_tr/validation_matched/")
        multi_nli_splitted = multi_nli.train_test_split(test_size=0.5, seed=25)
        if split == 'validation':
            multi_nli = multi_nli_splitted['train']
        elif split == 'test':
            multi_nli = multi_nli_splitted['test']
    else:
        raise ValueError(f"Unknown split: {split}")

    # Filter out rows with -1 labels before creating dataset instance
    original_size = len(multi_nli)
    print(f"Original dataset size: {original_size}")
    multi_nli = multi_nli.filter(lambda example: example['label'] != -1)
    filtered_size = len(multi_nli)
    print(f"Filtered dataset size: {filtered_size} (removed {original_size - filtered_size} samples with label -1)")

    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    # Create dataset instance
    dataset = NLIDataset(multi_nli, tokenizer, max_seq_length, is_lower)

    return dataset


def build_snli_dataloader(split: str, tokenizer_name: str,
                         max_seq_length: int, is_lower: bool = False):
    """Build dataloader for MultiNLI dataset.
    
    Args:
        split (str): One of 'train', 'validation', or 'test'
        tokenizer_name (str): Name of the tokenizer to use
        max_seq_length (int): Maximum sequence length
        
    Returns:
        Dataset: A dataset for NLI task
    """
    if split == 'train':
        snli = load_from_disk("/workspace/TabiBERT/finetuning/datasets/snli_tr/train/")
    elif split == 'test':
        snli = load_from_disk("/workspace/TabiBERT/finetuning/datasets/snli_tr/test/")
    elif split == 'validation':
        snli = load_from_disk("/workspace/TabiBERT/finetuning/datasets/snli_tr/validation/")
    else:
        raise ValueError(f"Unknown split: {split}")

    # Filter out rows with -1 labels before creating dataset instance
    original_size = len(snli)
    print(f"Original dataset size: {original_size}")
    snli = snli.filter(lambda example: example['label'] != -1)
    filtered_size = len(snli)
    print(f"Filtered dataset size: {filtered_size} (removed {original_size - filtered_size} samples with label -1)")

    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    # Create dataset instance
    dataset = NLIDataset(snli, tokenizer, max_seq_length, is_lower)

    return dataset

def build_med_nli_dataloader(split: str, tokenizer_name: str,
                         max_seq_length: int, is_lower: bool = False):
    ds = load_dataset(
        "boun-tabilab/MedNLI-TR",
        data_files={
            "train": "train-*.parquet",
            "dev": "dev-*.parquet",
            "test": "test-*.parquet"
        }
    )

    label2id = {
        'entailment': 0,
        'neutral': 1,
        'contradiction': 2,
    }

    for split_str in ds.keys():
        ds[split_str] = ds[split_str].rename_columns({
        'sentence1': 'premise',
        'sentence2': 'hypothesis',
    }).map(lambda x: {"label": label2id[x["label"]]})
    
    dataset_map = {
        'train': ds['train'],
        'validation': ds['dev'],
        'test': ds['test'],
    }

    if split not in dataset_map:
        raise ValueError(
            f"Unknown split: {split}. Expected one of: {list(dataset_map.keys())}"
        )

    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    # Create dataset instance
    dataset = NLIDataset(dataset_map[split], tokenizer, max_seq_length, is_lower)

    return dataset

def build_review_dataloader(split: str, tokenizer_name: str,
                            max_seq_length: int, is_lower: bool = False):
    
    dataset = load_dataset("fthbrmnby/turkish_product_reviews")

    # Rename "sentence" to "text", "sentiment" to "label"
    dataset = dataset.rename_columns({
        "sentence": "text",
        "sentiment": "label"
    })

    # Split the train dataset into train, validation, and test
    train_val_test = dataset['train'].train_test_split(test_size=0.3, seed=25)
    train_dataset, eval_test_dataset = train_val_test['train'], train_val_test[
        'test']
    eval_test_dataset = eval_test_dataset.train_test_split(test_size=0.5,
                                                           seed=25)
    eval_dataset, test_dataset = eval_test_dataset['train'], eval_test_dataset[
        'test']

    # Create train_val_dataset as combination of train_dataset + eval_dataset
    train_val_dataset = concatenate_datasets([train_dataset, eval_dataset])

    
    dataset_map = {
        'train': train_dataset,
        'validation': eval_dataset,
        'test': test_dataset,
        'train_val': train_val_dataset,
    }

    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    if split not in dataset_map:
        raise ValueError(
            f"Unknown split: {split}. Expected one of: {list(dataset_map.keys())}"
        )

    dataset = TextClassificationDataset(dataset_map[split], tokenizer, max_seq_length, is_lower)
    return dataset

def build_bil_tweet_news_dataloader(split: str, tokenizer_name: str,
                             max_seq_length: int, is_lower: bool = False):
    tweet_news = load_dataset("ctoraman/BilTweetNews-sentiment-analysis")['train']
    # 'Majority' are: {'Multi', 'Negative', 'Neutral', 'Positive', 'Sarcastic'}
    tweet_news = tweet_news.rename_columns({
        'Text': 'text',
        'Majority': 'label',
        "TweetID" : 'id',
    })

    tweet_news = tweet_news.remove_columns(
        [col for col in tweet_news.column_names if col not in ["text", "label", "id"]]
    )

    # Define mapping
    label2id = {
        'Multi': 0,
        'Negative': 1,
        'Neutral': 2,
        'Positive': 3,
        'Sarcastic': 4
    }

    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    tweet_news = tweet_news.map(lambda x: {"label": label2id[x["label"]]})

    split_dataset = tweet_news.train_test_split(test_size=0.3, seed=25)
    train_dataset, val_test = split_dataset['train'], split_dataset['test']
    val_test = val_test.train_test_split(test_size=0.5, seed=25)
    eval_dataset, test_dataset = val_test['train'], val_test['test']

    dataset_map = {
        'train': train_dataset,
        'validation': eval_dataset,
        'test': test_dataset,
    }

    if split not in dataset_map:
        raise ValueError(
            f"Unknown split: {split}. Expected one of: {list(dataset_map.keys())}"
        )

    dataset = TextClassificationDataset(dataset_map[split], tokenizer, max_seq_length, is_lower)
    return dataset


def gender_hate_speech_dataloader(split: str, tokenizer_name: str,
                             max_seq_length: int, is_lower: bool = False):


    hate_speech_dataset = load_dataset("ctoraman/gender-hate-speech-turkish")
    hate_speech_dataset['train'] = hate_speech_dataset['train'].rename_columns({
        'Text': 'text',
        'Label': 'label',
    })
    hate_speech_dataset['test'] = hate_speech_dataset['test'].rename_columns({
        'Text': 'text',
        'Label': 'label',
    })

    split_dataset = hate_speech_dataset['train'].train_test_split(test_size=0.1, seed=25)
    train_dataset, eval_dataset = split_dataset['train'], split_dataset['test']
    test_dataset = hate_speech_dataset['test']

    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    dataset_map = {
        'train': train_dataset,
        'validation': eval_dataset,
        'test': test_dataset,
    }

    if split not in dataset_map:
        raise ValueError(
            f"Unknown split: {split}. Expected one of: {list(dataset_map.keys())}"
        )

    dataset = TextClassificationDataset(dataset_map[split], tokenizer, max_seq_length, is_lower)
    return dataset

def build_pubmed_RCT_dataloader(split: str, tokenizer_name: str,
                             max_seq_length: int, is_lower: bool = False):
    if split == "validation":
        split = "dev"
        
    ds = datasets.load_dataset(
        "boun-tabilab/PubmedRCT-10K-TR",
        data_files={
            "train": "train-*.parquet",
            "dev": "dev-*.parquet",
            "test": "test-*.parquet"
        }
    )[split]
    
    all_labels = set()
    all_labels.update(ds["label"])
    
    label2id = {label: idx for idx, label in enumerate(sorted(all_labels))}

    def map_label(example):
        label = example["label"]
        if label not in label2id:
            raise ValueError(
                f"Label '{label}' found in dataset but not in train/dev splits. "
                f"This indicates a data quality issue - all test labels should exist in train/dev."
            )
        example["label"] = label2id[label]
        return example

    ds = ds.map(map_label)
    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    dataset = TextClassificationDataset(ds, tokenizer, max_seq_length, is_lower)
    return dataset

def build_sci_cite_dataloader(split: str, tokenizer_name: str,
                             max_seq_length: int, is_lower: bool = False):
    if split == "validation":
        split = "dev"
        
    ds = datasets.load_dataset(
        "boun-tabilab/SciCite-TR",
        data_files={
            "train": "data/train-*.parquet",
            "dev": "data/dev-*.parquet",
            "test": "data/test-*.parquet"
        }
    )[split]
    
    all_labels = set()
    all_labels.update(ds["label"])
    
    label2id = {label: idx for idx, label in enumerate(sorted(all_labels))}

    def map_label(example):
        label = example["label"]
        if label not in label2id:
            raise ValueError(
                f"Label '{label}' found in dataset but not in train/dev splits. "
                f"This indicates a data quality issue - all test labels should exist in train/dev."
            )
        example["label"] = label2id[label]
        return example

    ds = ds.map(map_label)
    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    dataset = TextClassificationDataset(ds, tokenizer, max_seq_length, is_lower)
    return dataset

def build_thesis_abstract_dataloader(split: str, tokenizer_name: str,
                             max_seq_length: int, is_lower: bool = False):
    if split == "validation":
        split = "dev"
        
    ds = datasets.load_dataset(
        "boun-tabilab/ThesisAbstractClassification-11K",
        data_files={
            "train": "data/train-*.parquet",
            "dev": "data/dev-*.parquet",
            "test": "data/test-*.parquet"
        }
    )[split].rename_columns({
        'abstract': 'text',
    })
    
    all_labels = set()
    all_labels.update(ds["label"])
    
    label2id = {label: idx for idx, label in enumerate(sorted(all_labels))}

    def map_label(example):
        label = example["label"]
        if label not in label2id:
            raise ValueError(
                f"Label '{label}' found in dataset but not in train/dev splits. "
                f"This indicates a data quality issue - all test labels should exist in train/dev."
            )
        example["label"] = label2id[label]
        return example

    ds = ds.map(map_label)
    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    dataset = TextClassificationDataset(ds, tokenizer, max_seq_length, is_lower)
    return dataset
    
def build_stsb_tr_dataloader(split: str, tokenizer_name: str,
                             max_seq_length: int, is_lower: bool = False):
    """
    Build dataloader for Turkish STS-B dataset
    
    Args:
        split: One of 'train', 'validation', 'test'
        tokenizer_name: HuggingFace tokenizer name
        max_seq_length: Maximum sequence length for tokenization
    
    Returns:
        STSDataset instance
    """

    path_STSB = '/workspace/TabiBERT/finetuning/datasets/stsb_tr/'
    stsb_reader = STSBReader(path_STSB)
    sts_dataset = stsb_reader.get_datasets()

    train_dataset, eval_dataset, test_dataset = sts_dataset['train'], sts_dataset[
        'dev'], sts_dataset['test']

    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    
    dataset_map = {
        'train': train_dataset,
        'validation': eval_dataset,
        'test': test_dataset,
    }

    if split not in dataset_map:
        raise ValueError(
            f"Unknown split: {split}. Expected one of: {list(dataset_map.keys())}"
        )

    dataset_instance = STSDataset(dataset_map[split], tokenizer,
                                  max_seq_length, is_lower)

    return dataset_instance


def build_sick_tr_dataloader(split: str, tokenizer_name: str,
                             max_seq_length: int, is_lower: bool = False):
    """
    Build dataloader for Turkish STS-B dataset
    
    Args:
        split: One of 'train', 'validation', 'test'
        tokenizer_name: HuggingFace tokenizer name
        max_seq_length: Maximum sequence length for tokenization
    
    Returns:
        STSDataset instance
    """

    path_SICK = '/workspace/TabiBERT/finetuning/datasets/sick_tr/'
    sick_reader = SICKReader(path_SICK)
    sick_dataset = sick_reader.get_datasets()

    train_dataset, eval_dataset, test_dataset = sick_dataset['train'], sick_dataset[
        'trial'], sick_dataset['test']

    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    
    dataset_map = {
        'train': train_dataset,
        'validation': eval_dataset,
        'test': test_dataset,
    }

    if split not in dataset_map:
        raise ValueError(
            f"Unknown split: {split}. Expected one of: {list(dataset_map.keys())}"
        )

    dataset_instance = STSDataset(dataset_map[split], tokenizer,
                                  max_seq_length, is_lower)

    return dataset_instance

def build_news_cat_dataloader(split: str, tokenizer_name: str,
                              max_seq_length: int, is_lower: bool=False):

    label2id = {
        'economy': 0,
        'health': 1,
        'magazine': 2,
        'politics': 3,
        'sport': 4,
    }

    # Load from HF (category column values are int):
    dataset = load_dataset("mcemilg/news-cat")
    train_dataset, eval_dataset, test_dataset = dataset['train'], dataset[
        'validation'], dataset['test']

    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name, timeout=60)

    # Create train_val_dataset as combination of train_dataset + eval_dataset
    train_val_dataset = concatenate_datasets([train_dataset, eval_dataset])

    
    dataset_map = {
        'train': train_dataset,
        'validation': eval_dataset,
        'test': test_dataset,
        'train_val': train_val_dataset,
    }

    if split not in dataset_map:
        raise ValueError(
            f"Unknown split: {split}. Expected one of: {list(dataset_map.keys())}"
        )

    dataset = NewsCatDataset(dataset_map[split], tokenizer, max_seq_length, label2id, is_lower)

    return dataset

def build_wiki_ner_dataloader(split: str, tokenizer_name: str, max_seq_length: int, is_lower: bool = False):
    

    if split == "train_val":
        train_dataset = load_dataset("turkish-nlp-suite/turkish-wikiNER")['train']
        eval_dataset = load_dataset("turkish-nlp-suite/turkish-wikiNER")['validation']
        dataset = concatenate_datasets([train_dataset, eval_dataset])
    else:
        dataset = load_dataset("turkish-nlp-suite/turkish-wikiNER")[split]

    # Build tag2id mapping
    unique_tags = set(tag for row in dataset for tag in row['tags'])
    tag2id = {tag: i for i, tag in enumerate(sorted(unique_tags))}

    
    if 'TurkishBERTweet' in tokenizer_name:
        tokenizer = RobertaTokenizerFast.from_pretrained(tokenizer_name, add_prefix_space=True)
    else:
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    # Create the custom dataset
    ner_dataset = NERDataset(dataset, tokenizer, tag2id, max_seq_length, is_lower)

    return ner_dataset, tag2id

def build_wiki_ann_ner_dataloader(split: str, tokenizer_name: str, max_seq_length: int, is_lower: bool = False):
    

    if split == "train":
        dataset = load_from_disk("/workspace/TabiBERT/finetuning/datasets/wiki_ann_ner/train/")
    elif split == "test":
        dataset = load_from_disk("/workspace/TabiBERT/finetuning/datasets/wiki_ann_ner/test/")
    elif split == "validation":
        dataset = load_from_disk("/workspace/TabiBERT/finetuning/datasets/wiki_ann_ner/validation/")
    else:
        raise ValueError(f"Unknown split: {split}")

    unique_tags = {0, 1, 2, 3, 4, 5, 6}

    
    if 'TurkishBERTweet' in tokenizer_name:
        tokenizer = RobertaTokenizerFast.from_pretrained(tokenizer_name, add_prefix_space=True)
    else:
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    # Create the custom dataset
    ner_dataset = WikiANNNERDataset(dataset, tokenizer, max_seq_length, is_lower)

    return ner_dataset, unique_tags

def build_pos_ud_boun_dataloader(split: str, tokenizer_name: str, max_seq_length: int, is_lower: bool = False):
    pos_boun_train_path = "/workspace/TabiBERT/finetuning/datasets/pos_ud_boun/tr_boun-ud-train.conllu"
    pos_boun_test_path = "/workspace/TabiBERT/finetuning/datasets/pos_ud_boun/tr_boun-ud-test.conllu"
    pos_boun_dev_path = "/workspace/TabiBERT/finetuning/datasets/pos_ud_boun/tr_boun-ud-dev.conllu"

    def load_conllu_to_dataset(filepath):
        sentences = []
        with open(filepath, "r", encoding="utf-8") as f:
            for tokenlist in parse_incr(f):
                tokens = [token["form"] for token in tokenlist]
                lemmas = [token["lemma"] for token in tokenlist]
                pos_tags = [token["upostag"] for token in tokenlist]

                sentences.append({
                    "tokens": tokens,
                    "lemmas": lemmas,
                    "pos_tags": pos_tags
                })
        return Dataset.from_list(sentences)

    if split == "train":
        dataset = load_conllu_to_dataset(pos_boun_train_path)
    elif split == "validation":
        dataset = load_conllu_to_dataset(pos_boun_dev_path)
    elif split == "test":
        dataset = load_conllu_to_dataset(pos_boun_test_path)
    else:
        raise ValueError(
            f"Unknown split: {split}. Expected one of: {list(dataset_map.keys())}"
        )

    # Build tag2id mapping
    unique_tags = set(tag for row in dataset for tag in row['pos_tags'])
    tag2id = {tag: i for i, tag in enumerate(sorted(unique_tags))}

    
    if 'TurkishBERTweet' in tokenizer_name:
        tokenizer = RobertaTokenizerFast.from_pretrained(tokenizer_name, add_prefix_space=True)
    else:
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    # Create the custom dataset
    dataset = POSUDDataset(dataset, tokenizer, max_seq_length, is_lower)

    return dataset, tag2id


def build_pos_ud_imst_dataloader(split: str, tokenizer_name: str, max_seq_length: int, is_lower: bool = False):
    pos_imst_train_path = "/workspace/TabiBERT/finetuning/datasets/pos_ud_imst/tr_imst-ud-train.conllu"
    pos_imst_test_path = "/workspace/TabiBERT/finetuning/datasets/pos_ud_imst/tr_imst-ud-test.conllu"
    pos_imst_dev_path = "/workspace/TabiBERT/finetuning/datasets/pos_ud_imst/tr_imst-ud-dev.conllu"

    def load_conllu_to_dataset(filepath):
        sentences = []
        with open(filepath, "r", encoding="utf-8") as f:
            for tokenlist in parse_incr(f):
                tokens = [token["form"] for token in tokenlist]
                lemmas = [token["lemma"] for token in tokenlist]
                pos_tags = [token["upostag"] for token in tokenlist]

                sentences.append({
                    "tokens": tokens,
                    "lemmas": lemmas,
                    "pos_tags": pos_tags
                })
        return Dataset.from_list(sentences)

    if split == "train":
        dataset = load_conllu_to_dataset(pos_imst_train_path)
    elif split == "validation":
        dataset = load_conllu_to_dataset(pos_imst_dev_path)
    elif split == "test":
        dataset = load_conllu_to_dataset(pos_imst_test_path)
    else:
        raise ValueError(
            f"Unknown split: {split}. Expected one of: {list(dataset_map.keys())}"
        )

    # Build tag2id mapping
    unique_tags = set(tag for row in dataset for tag in row['pos_tags'])
    tag2id = {tag: i for i, tag in enumerate(sorted(unique_tags))}

    
    if 'TurkishBERTweet' in tokenizer_name:
        tokenizer = RobertaTokenizerFast.from_pretrained(tokenizer_name, add_prefix_space=True)
    else:
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    # Create the custom dataset
    dataset = POSUDDataset(dataset, tokenizer, max_seq_length, is_lower)

    return dataset, tag2id

def build_xtreme_qa_dataloader(split: str, tokenizer_name: str, max_seq_length: int, is_lower: bool = False):
    xtreme_qa = load_dataset("google/xquad", 'xquad.tr')['validation']
    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    train_test_val = xtreme_qa.train_test_split(test_size=0.3, seed=25)

    train_dataset, val_test_split = train_test_val['train'], train_test_val['test']

    val_test_split = val_test_split.train_test_split(test_size=0.5, seed=25)

    eval_dataset, test_dataset = val_test_split['train'], val_test_split['test']

    dataset_map = {
        'train': train_dataset,
        'validation': eval_dataset,
        'test': test_dataset,
    }

    if split not in dataset_map:
        raise ValueError(
            f"Unknown split: {split}. Expected one of: {list(dataset_map.keys())}"
        )
    dataset = dataset_map[split]

    # Create the custom dataset
    xtreme_dataset = QADataset(dataset, tokenizer, max_seq_length, is_lower)

    return xtreme_dataset

def build_tquad_qa_dataloader(split: str, tokenizer_name: str, max_seq_length: int, is_lower: bool = False):
    tquad_qa = load_dataset("erdometo/tquad2")
    train_val_dataset = tquad_qa['train']
    test_dataset = tquad_qa['validation']

    
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    train_val = train_val_dataset.train_test_split(test_size=0.17, seed=25)

    train_dataset, eval_dataset = train_val['train'], train_val['test']

    dataset_map = {
        'train': train_dataset,
        'validation': eval_dataset,
        'test': test_dataset,
    }

    if split not in dataset_map:
        raise ValueError(
            f"Unknown split: {split}. Expected one of: {list(dataset_map.keys())}"
        )
    dataset = dataset_map[split]

    # Create the custom dataset
    tquad_qa_dataset = QADataset(dataset, tokenizer, max_seq_length, is_lower)

    return tquad_qa_dataset


def build_retrieval_dataloader(
    split: str,
    tokenizer_name: str,
    max_seq_length: int,
    is_lower: bool,
    retrieval_task_id: int,
):
    if retrieval_task_id > 5:
        return build_code_retrieval_dataloader(
            split,
            tokenizer_name,
            max_seq_length,
            is_lower,
            retrieval_task_id - 10,
        )
    # features: ['anchor', 'positive']

    if retrieval_task_id == 0:
        dataset = load_dataset("trmteb/wmt16_en_tr_fine_tuning_dataset")
    elif retrieval_task_id == 1:
        dataset = load_dataset("trmteb/msmarco-tr_fine_tuning_dataset")
    elif retrieval_task_id == 2:
        dataset = load_dataset("trmteb/scifact-tr_fine_tuning_dataset")
        train_dev = dataset['train'].train_test_split(test_size=0.36, seed=25)
        train = train_dev['train']
        dev = train_dev['test']
        dataset['train'] = train
        dataset['validation'] = dev
    elif retrieval_task_id == 3:
        dataset = load_dataset("trmteb/fiqa-tr_fine_tuning_dataset")
    elif retrieval_task_id == 4:
        dataset = load_dataset("trmteb/nfcorpus-tr_fine_tuning_dataset")
    elif retrieval_task_id == 5:
        dataset = load_dataset("trmteb/quora-tr_fine_tuning_dataset")
        train_dev = dataset['dev'].train_test_split(test_size=0.2, seed=25)
        train = train_dev['train']
        dev = train_dev['test']
        dataset['train'] = train
        dataset['validation'] = dev
    if "validation" not in dataset and "dev" in dataset:
        dataset["validation"] = dataset.pop("dev")

    dataset_split = dataset[split]
    
    if is_lower:
        def lower_case_example(example):
            for col in example:
                if example[col] is not None:
                    example[col] = example[col].lower()
            return example

        # Use map to apply the lowercasing function to all samples efficiently
        dataset_split = dataset_split.map(lower_case_example, num_proc=4) # num_proc=4 is a common default for speed
        
    dataset_split = check_and_remove_none(dataset_split,
                                          ["anchor", "positive"])

    return dataset_split
    

def check_and_remove_none(dataset, text_column_names):
    """
    Checks for and removes rows with None values in specified columns.

    Args:
        dataset (datasets.Dataset): The dataset to process.
        text_column_names (list): List of column names to check for None values.

    Returns:
        datasets.Dataset: The processed dataset with None rows removed.
    """
    indices_to_keep = []
    for i in range(len(dataset)):
        is_valid = True
        for column_name in text_column_names:
            if dataset[i][column_name] is None:
                is_valid = False
                break
        if is_valid:
            indices_to_keep.append(i)
    return dataset.select(indices_to_keep)


def build_code_retrieval_dataloader(
    split: str,
    tokenizer_name: str,
    max_seq_length: int,
    is_lower: bool,
    code_retrieval_task_id: int,
):
    
    if split == "validation":
        split = "dev"
        
    code_retrieval_datasets = [
        "boun-tabilab/Apps-TR",
        "boun-tabilab/CosQA-TR",
        "boun-tabilab/StackoverflowQA-TR",
        "boun-tabilab/CodeSearchNet-21K-TR"
    ]

    dataset = load_dataset(
        code_retrieval_datasets[code_retrieval_task_id],
    )
    if "dev" not in dataset:
        train_dev_split = dataset['train'].train_test_split(test_size=0.75, seed=25)
        dataset['train'] = train_dev_split['train']
        dataset['dev'] = train_dev_split['test']

    dataset_split = dataset[split]
    dataset_split = dataset_split.rename_columns({
        "query": "anchor",
        "doc": "positive"
    })

    if is_lower:
        def lower_case_example(example):
            for col in example:
                if example[col] is not None:
                    example[col] = example[col].lower()
            return example

        # Use map to apply the lowercasing function to all samples efficiently
        dataset_split = dataset_split.map(lower_case_example, num_proc=4) # num_proc=4 is a common default for speed
        
    dataset_split = check_and_remove_none(dataset_split,
                                          ["anchor", "positive"])

    return dataset_split
    