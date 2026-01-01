MODELS = {
    'TabiBERT': {
        'model_path': 'boun-tabilab/TabiBERT',
        'max_position_embeddings': 8192,
    },
    # 'MDZ_BERTurk': {
    #     'model_path': 'dbmdz/bert-base-turkish-cased',
    #     'max_position_embeddings': 512
    # },
    # 'YTU_BERT': {
    #     'model_path': 'ytu-ce-cosmos/turkish-base-bert-uncased',
    #     'max_position_embeddings': 512
    # },
    # 'Sabanci_TurkishBERTweet': {
    #     'model_path': 'VRLLab/TurkishBERTweet',
    #     'max_position_embeddings': 512
    # },
    # 'mmBERT_base': {
    #     'model_path': 'jhu-clsp/mmBERT-base',
    #     'max_position_embeddings': 8192 
    # },
}

TASKS = {
    # 'news_cat': {
    #     'task_type': 'classification',
    #     'num_labels': 5,
    #     'max_seq_len': 1280
    # },
    # 'prod_review': {
    #     'task_type': 'classification',
    #     'num_labels': 2,
    #     'max_seq_len': 384
    # },
    # 'bil_tweet_news': {
    #     'task_type': 'classification',
    #     'num_labels': 5,
    #     'max_seq_len': 128
    # },
    # 'gender_hate_speech': {
    #     'task_type': 'classification',
    #     'num_labels': 3,
    #     'max_seq_len': 128
    # },
    # 'pubmed_RCT': {      # boun-tabilab/PubmedRCT-10K-TR
    #     'task_type': 'classification',
    #     'num_labels': 5,
    #     'max_seq_len': 128      
    # },
    # 'sci_cite_TR': {      # boun-tabilab/SciCite-TR
    #     'task_type': 'classification',
    #     'num_labels': 3,
    #     'max_seq_len': 256      
    # },
    # 'thesis_abstract': {      # boun-tabilab/ThesisAbstractClassification-11K
    #     'task_type': 'classification',
    #     'num_labels': 187,
    #     'max_seq_len': 1152      
    # },
    # 'wiki_ner': {  # 'turkish-nlp-suite/turkish-wikiNER'
    #     'task_type': 'ner', 
    #     'num_labels': 39,
    #     'max_seq_len': 128
    # },
    # 'wiki_ann_ner' : {
    #     'task_type': 'ner', 
    #     'num_labels': 7,
    #     'max_seq_len': 128
    # },
    # 'pos_ud_boun': {
    #     'task_type': 'pos', 
    #     'num_labels': 17,
    #     'max_seq_len': 128 
    # },
    # 'pos_ud_imst': {
    #     'task_type': 'pos', 
    #     'num_labels': 15,
    #     'max_seq_len': 128 
    # },
    # 'sts': {
    #     'task_type': 'regression',
    #     'num_labels': 1,
    #     'max_seq_len': 128
    # },
    # 'sick_tr': {
    #     'task_type': 'regression',
    #     'num_labels': 1,
    #     'max_seq_len': 128
    # },
    # 'xquad_qa': {   # load_dataset("google/xtreme", "XQuAD.tr") OR load_dataset("google/xquad", 'xquad.tr')
    #     'task_type': 'qa', 
    #     'num_labels': -1,
    #     'max_seq_len': 384,
    # },
    # 'tquad2_qa': {   # load_dataset("erdometo/tquad2")
    #     'task_type': 'qa', 
    #     'num_labels': -1,
    #     'max_seq_len': 1024,
    # },
    # 'multinli': {
    #     'task_type': 'nli',
    #     'num_labels': 3,
    #     'max_seq_len': 128
    # },
    # 'snli': {
    #     'task_type': 'nli',
    #     'num_labels': 3,
    #     'max_seq_len': 128
    # },
    # 'med_nli': {
    #     'task_type': 'nli',
    #     'num_labels': 3,
    #     'max_seq_len': 128       
    # },
    # 'wmt16': {  # BiText - "trmteb/wmt16_en_tr_fine_tuning_dataset"
    #     'task_type': 'retrieval', 
    #     'num_labels': -1,
    #     'max_seq_len': 256,
    #     'id': 0,
    # },
    'msmarco': {  # MsMarco-TR - "trmteb/msmarco-tr_fine_tuning_dataset"
        'task_type': 'retrieval', 
        'num_labels': -1,
        'max_seq_len': 256,
        'id': 1,
    },
    'scifact': {  # Scifact-TR - "trmteb/scifact-tr_fine_tuning_dataset"
        'task_type': 'retrieval', 
        'num_labels': -1,
        'max_seq_len': 512,
        'id': 2,
    },
    'fiqa': {  # Fiqa-TR - "trmteb/fiqa-tr_fine_tuning_dataset"
        'task_type': 'retrieval', 
        'num_labels': -1,
        'max_seq_len': 512,
        'id': 3,
    },
    # 'nfcorpus': {  # NFCorpus-TR - "trmteb/nfcorpus-tr_fine_tuning_dataset"
    #     'task_type': 'retrieval', 
    #     'num_labels': -1,
    #     'max_seq_len': 512,
    #     'id': 4,
    # },
    # 'quora': {  # Quora-TR - "trmteb/quora-tr_fine_tuning_dataset"
    #     'task_type': 'retrieval', 
    #     'num_labels': -1,
    #     'max_seq_len': 128,
    #     'id': 5,
    # },
    # 'apps_tr': {
    #     'task_type': 'retrieval', 
    #     'num_labels': -1,
    #     'max_seq_len': 1152,
    #     'id': 10,
    # },
    # 'cosqa_tr': {
    #     'task_type': 'retrieval', 
    #     'num_labels': -1,
    #     'max_seq_len': 128,
    #     'id': 11,
    # },
    # 'stackoverflow_qa_tr': { 
    #     'task_type': 'retrieval', 
    #     'num_labels': -1,
    #     'max_seq_len': 2560,
    #     'id': 12,
    # },
    # 'codeSearchNet_tr': { 
    #     'task_type': 'retrieval', 
    #     'num_labels': -1,
    #     'max_seq_len': 1024,
    #     'id': 13,
    # },
}