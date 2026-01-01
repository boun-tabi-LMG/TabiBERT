import os
import sys
import random
from datetime import datetime
import hydra
from omegaconf import DictConfig
from hydra import compose, initialize
from pathlib import Path
from typing import Optional, cast
from omegaconf import OmegaConf as om

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import torch
import numpy as np
from sklearn.metrics import ndcg_score, average_precision_score
from transformers import EarlyStoppingCallback
from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer
from sentence_transformers.losses import MultipleNegativesRankingLoss
from sentence_transformers import SentenceTransformerTrainingArguments
from sentence_transformers.training_args import BatchSamplers
from sentence_transformers.evaluation import SentenceEvaluator
from sentence_transformers.util import cos_sim
from finetuning.dataloaders.dataloaders import build_retrieval_dataloader
from finetuning.hyperparam_retrieval_eval import eval_retrieval
from utils import setup_logging

# Import wandb for logging configuration
try:
    import wandb
except ImportError:
    wandb = None

logger = setup_logging('hyperparameter_retrieval_train.py')

torch.set_float32_matmul_precision('high')

class NDCGEvaluator(SentenceEvaluator):
    """
    Custom evaluator for NDCG@k metric during training.
    Inherits from SentenceEvaluator to be compatible with SentenceTransformerTrainer.
    
    This evaluator performs proper query-to-corpus retrieval evaluation:
    - Builds a corpus from all unique documents in the eval dataset
    - For each query, ranks all documents in the corpus
    - Computes NDCG based on relevance judgments
    """
    
    def __init__(self, eval_dataset, name: str = "", k: int = 10, batch_size: int = 32, 
                 return_loss: bool = False, loss_model=None):
        """
        Initialize NDCG evaluator.
        
        Args:
            eval_dataset: Dataset with 'anchor' and 'positive' columns
            name: Name for the evaluator (used in logging)
            k: Top-k for NDCG@k calculation
            batch_size: Batch size for encoding
            return_loss: If True, compute and return loss as primary metric (for early stopping on loss)
            loss_model: Loss function to use if return_loss is True
        """
        self.eval_dataset = eval_dataset
        self.name = name
        self.k = k
        self.batch_size = batch_size
        self.return_loss = return_loss
        self.loss_model = loss_model
        
        # Pre-extract anchors (queries) and positives (relevant documents)
        self.anchors = list(eval_dataset["anchor"])
        self.positives = list(eval_dataset["positive"])
        
        # Build corpus: all unique documents (positives)
        # This creates a corpus where each query can be ranked against all documents
        self.corpus = self.positives  # For now, corpus = all positives
        # Create mapping: for each query, which documents in corpus are relevant
        # In this setup, query_i is relevant to document_i (at same index)
        self.query_to_relevant_docs = {i: [i] for i in range(len(self.anchors))}
        
        logger.info(f"NDCGEvaluator initialized: {len(self.anchors)} queries, {len(self.corpus)} documents in corpus, k={k}, return_loss={return_loss}")
    
    def __call__(self, model, output_path: str = None, epoch: int = -1, steps: int = -1) -> float:
        """
        Evaluate the model and return NDCG@k score or loss.
        
        Performs proper query-to-corpus retrieval:
        - Encodes all queries and all documents in corpus
        - For each query, computes similarity to all documents
        - Ranks documents for each query and computes NDCG
        
        Args:
            model: SentenceTransformer model to evaluate
            output_path: Optional path to save results
            epoch: Current epoch number
            steps: Current step number
        
        Returns:
            float: NDCG@k score (or loss if return_loss=True)
        """
        import torch.nn.functional as F
        
        # Encode queries (anchors)
        query_embeddings = model.encode(
            self.anchors, 
            convert_to_tensor=True, 
            show_progress_bar=False,
            batch_size=self.batch_size
        )
        
        # Encode corpus documents (all documents that queries will be ranked against)
        corpus_embeddings = model.encode(
            self.corpus, 
            convert_to_tensor=True, 
            show_progress_bar=False,
            batch_size=self.batch_size
        )
        
        # Compute loss if requested (for early stopping)
        # For loss computation, we still use the original positive pairs
        if self.return_loss and self.loss_model is not None:
            # Encode positives for loss computation
            positive_embeddings = model.encode(
                self.positives, 
                convert_to_tensor=True, 
                show_progress_bar=False,
                batch_size=self.batch_size
            )
            # Compute loss using the provided loss model
            # For MultipleNegativesRankingLoss, we need to compute pairwise similarities
            # and apply the loss function
            similarity_matrix = cos_sim(query_embeddings, positive_embeddings)
            
            # For MNRL loss: we want diagonal to be high (positive pairs)
            # and off-diagonal to be low (negative pairs)
            # Loss = -log(exp(sim_pos) / sum(exp(sim_all)))
            # Simplified: use cross-entropy with diagonal as targets
            labels = torch.arange(len(query_embeddings)).to(query_embeddings.device)
            loss = F.cross_entropy(similarity_matrix, labels)
            loss_value = loss.item()
            
            # Log the loss
            if epoch != -1:
                logger.info(f"Epoch {epoch}: Eval Loss = {loss_value:.4f}")
            elif steps != -1:
                logger.info(f"Step {steps}: Eval Loss = {loss_value:.4f}")
            else:
                logger.info(f"Eval Loss = {loss_value:.4f}")
        
        # Compute query-to-corpus similarity matrix for NDCG
        # similarity_matrix[i][j] = similarity(query_i, corpus_doc_j)
        similarity_matrix = cos_sim(query_embeddings, corpus_embeddings)
        similarity_matrix = similarity_matrix.cpu().numpy()
        
        # Build ground truth matrix: y_true[i][j] = 1 if corpus_doc_j is relevant to query_i
        y_true = np.zeros((len(self.anchors), len(self.corpus)))
        for query_idx, relevant_doc_indices in self.query_to_relevant_docs.items():
            for doc_idx in relevant_doc_indices:
                if doc_idx < len(self.corpus):
                    y_true[query_idx][doc_idx] = 1.0
        
        y_score = similarity_matrix
        
        # Calculate NDCG@k for each query, then average
        ndcg_scores = []
        for i in range(len(self.anchors)):
            if np.sum(y_true[i]) > 0:  # Only compute if query has relevant documents
                ndcg_i = ndcg_score(y_true[i:i+1], y_score[i:i+1], k=self.k)
                ndcg_scores.append(ndcg_i)
        
        ndcg_at_k = np.mean(ndcg_scores) if ndcg_scores else 0.0
        
        # Log the NDCG result
        if epoch != -1:
            logger.info(f"Epoch {epoch}: NDCG@{self.k} = {ndcg_at_k:.4f}")
        elif steps != -1:
            logger.info(f"Step {steps}: NDCG@{self.k} = {ndcg_at_k:.4f}")
        else:
            logger.info(f"NDCG@{self.k} = {ndcg_at_k:.4f}")
        
        # Optionally save results to file
        if output_path is not None:
            csv_path = os.path.join(output_path, f"{self.name}_results.csv")
            os.makedirs(output_path, exist_ok=True)
            
            # Check if file exists to determine if we need to write header
            write_header = not os.path.exists(csv_path)
            
            with open(csv_path, mode='a', newline='') as f:
                import csv
                writer = csv.writer(f)
                if self.return_loss:
                    if write_header:
                        writer.writerow(['epoch', 'steps', 'eval_loss', f'ndcg@{self.k}'])
                    writer.writerow([epoch, steps, loss_value if self.return_loss else None, ndcg_at_k])
                else:
                    if write_header:
                        writer.writerow(['epoch', 'steps', f'ndcg@{self.k}'])
                    writer.writerow([epoch, steps, ndcg_at_k])
        
        # Return the primary metric based on configuration
        if self.return_loss:
            return loss_value  # Return loss for early stopping (lower is better)
        else:
            return ndcg_at_k  # Return NDCG for early stopping (higher is better)


def compute_ndcg_metrics(model, eval_dataset, k_values=[5, 10, 20]):
    """
    Compute NDCG and other retrieval metrics using sklearn.
    
    Performs proper query-to-corpus retrieval evaluation:
    - Builds a corpus from all documents in eval_dataset
    - For each query, ranks all documents in the corpus
    - Computes metrics based on relevance judgments
    
    Args:
        model: SentenceTransformer model
        eval_dataset: Dataset with 'anchor' and 'positive' columns
        k_values: List of k values for NDCG@k and Recall@k
    
    Returns:
        dict: Dictionary containing NDCG@k, MAP, MRR, and Recall@k metrics
    """
    logger.info("Computing NDCG-based retrieval metrics with sklearn...")
    
    # Extract queries (anchors) and relevant documents (positives)
    anchors = list(eval_dataset["anchor"])
    positives = list(eval_dataset["positive"])
    
    # Build corpus: all unique documents that queries will be ranked against
    corpus = positives  # Corpus = all documents from eval dataset
    # Create relevance mapping: query_i is relevant to document_i
    query_to_relevant_docs = {i: [i] for i in range(len(anchors))}
    
    logger.info(f"Evaluating on {len(anchors)} queries against corpus of {len(corpus)} documents")
    
    # Encode queries and corpus documents
    query_embeddings = model.encode(anchors, convert_to_tensor=True, show_progress_bar=False)
    corpus_embeddings = model.encode(corpus, convert_to_tensor=True, show_progress_bar=False)
    
    # Compute query-to-corpus similarity matrix: similarity[i][j] = similarity(query_i, corpus_doc_j)
    similarity_matrix = cos_sim(query_embeddings, corpus_embeddings)
    similarity_matrix = similarity_matrix.cpu().numpy()
    
    # Build ground truth matrix: y_true[i][j] = 1 if corpus_doc_j is relevant to query_i
    y_true = np.zeros((len(anchors), len(corpus)))
    for query_idx, relevant_doc_indices in query_to_relevant_docs.items():
        for doc_idx in relevant_doc_indices:
            if doc_idx < len(corpus):
                y_true[query_idx][doc_idx] = 1.0
    
    y_score = similarity_matrix
    
    # Calculate metrics
    metrics = {}
    
    # NDCG@k for different k values (compute per-query, then average)
    for k in k_values:
        ndcg_scores = []
        for i in range(len(anchors)):
            if np.sum(y_true[i]) > 0:  # Only compute if query has relevant documents
                ndcg_i = ndcg_score(y_true[i:i+1], y_score[i:i+1], k=k)
                ndcg_scores.append(ndcg_i)
        metrics[f'ndcg@{k}'] = np.mean(ndcg_scores) if ndcg_scores else 0.0
        logger.info(f"NDCG@{k}: {metrics[f'ndcg@{k}']:.4f}")
    
    # Mean Average Precision (MAP)
    map_scores = []
    for i in range(len(anchors)):
        if np.sum(y_true[i]) > 0:  # Only compute if query has relevant documents
            ap = average_precision_score(y_true[i], y_score[i])
            map_scores.append(ap)
    metrics['map'] = np.mean(map_scores) if map_scores else 0.0
    logger.info(f"MAP: {metrics['map']:.4f}")
    
    # Recall@k: proportion of relevant documents found in top-k
    for k in k_values:
        recall_at_k_list = []
        for i in range(len(anchors)):
            if np.sum(y_true[i]) > 0:  # Only compute if query has relevant documents
                # Get top-k indices for this query (sorted by similarity, descending)
                top_k_indices = np.argsort(y_score[i])[-k:][::-1]
                # Count how many relevant docs are in top-k
                relevant_in_topk = np.sum(y_true[i][top_k_indices])
                total_relevant = np.sum(y_true[i])
                recall = relevant_in_topk / total_relevant if total_relevant > 0 else 0.0
                recall_at_k_list.append(recall)
        metrics[f'recall@{k}'] = np.mean(recall_at_k_list) if recall_at_k_list else 0.0
        logger.info(f"Recall@{k}: {metrics[f'recall@{k}']:.4f}")
    
    # MRR (Mean Reciprocal Rank)
    mrr_scores = []
    for i in range(len(anchors)):
        if np.sum(y_true[i]) > 0:  # Only compute if query has relevant documents
            # Get ranking of all docs for this query (sorted by similarity, descending)
            ranked_indices = np.argsort(y_score[i])[::-1]
            # Find position of first relevant doc in the ranking
            for rank, doc_idx in enumerate(ranked_indices, start=1):
                if y_true[i][doc_idx] > 0:
                    mrr_scores.append(1.0 / rank)
                    break
    metrics['mrr'] = np.mean(mrr_scores) if mrr_scores else 0.0
    logger.info(f"MRR: {metrics['mrr']:.4f}")
    
    return metrics


def train_retrieval_model(
        model_path: str,
        tokenizer_name: str,
        is_lower: bool,
        task_name: str,
        task_content: dict,
        max_seq_len: int,
        model_name: str,
        hf_model_name: str,
        dataset_name: str,
        task_type: str,
        lr: float,
        weight_decay: float,
        epochs: int,
        batch_size: int,
        save_folder_str: str,
        wandb_name: str,
        eval_during_training: bool = True,
        early_stopping: bool = True,
        early_stopping_patience: int = 2,
        early_stopping_threshold: float = 0.0,
        early_stopping_metric: str = "loss",  # "loss" or "ndcg@10"
) -> dict:
    """
    Train a retrieval model using SentenceTransformers with NDCG@10 evaluation.
    
    Args:
        model_path: Path to the base model
        tokenizer_name: Name/path of the tokenizer
        is_lower: Whether to lowercase input
        task_name: Name of the task
        task_content: Dictionary containing task configuration (must have 'id' key)
        max_seq_len: Maximum sequence length
        model_name: Name of the model
        hf_model_name: HuggingFace model name
        dataset_name: Name of the dataset
        task_type: Type of task
        lr: Learning rate
        weight_decay: Weight decay
        epochs: Number of epochs
        batch_size: Batch size
        save_folder_str: Base save folder path for final model
        wandb_name: Name for wandb run
        early_stopping: Whether to use early stopping (default: True)
        early_stopping_patience: Number of evaluation calls with no improvement after which training will be stopped (default: 2)
        early_stopping_threshold: Minimum change to qualify as an improvement (default: 0.0)
        early_stopping_metric: Metric to monitor for early stopping - "loss" or "ndcg@10" (default: "loss")
        
    Returns:
        Dictionary containing evaluation metrics and metadata
    """
    epochs_str = str(epochs) + "ep"
    # Set seed for reproducibility (matching seed: 25 from default config)
    seed = 25
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

    save_folder_retrieval = f"./finetuning_checkpoints/{task_type}/{task_name}/{model_name}/" + str(
        lr) + "/" + str(weight_decay) + "/" + str(epochs_str) + "/" + str(
            batch_size)

    retrieval_model = SentenceTransformer(model_path)
    # Access the underlying Hugging Face transformer model and its config
    max_len = retrieval_model._first_module().max_seq_length
    print(f"### Model Max Sequence Length: {max_len}")

    # FIX for Sabanci model
    if "tweet" in model_path.lower(
    ) or "roberta" in retrieval_model.__class__.__name__.lower():
        max_seq_len = 512  # force this
        retrieval_model.max_seq_length = 512
    else:
        max_seq_len = max_len
        retrieval_model.max_seq_length = max_len

    train_dataset = build_retrieval_dataloader(
        split='train',
        tokenizer_name=tokenizer_name,
        max_seq_length=max_seq_len,
        is_lower=is_lower,
        retrieval_task_id=task_content['id'],
    )

    eval_dataset = build_retrieval_dataloader(
        split='validation',
        tokenizer_name=tokenizer_name,
        max_seq_length=max_seq_len,
        is_lower=is_lower,
        retrieval_task_id=task_content['id'],
    )

    mnrl_loss = MultipleNegativesRankingLoss(retrieval_model)

    # Determine early stopping configuration
    monitor_loss = early_stopping_metric.lower() == "loss"
    metric_name = "eval_loss" if monitor_loss else "eval_ndcg@10"
    greater_is_better = False if monitor_loss else True  # For loss, lower is better; for NDCG, higher is better

    logger.info(
        f"Early stopping configuration: metric={metric_name}, greater_is_better={greater_is_better}"
    )


    retrieval_args = SentenceTransformerTrainingArguments(
        # Required parameter:
        output_dir=save_folder_retrieval,
        # Training parameters (matching other finetuning tasks):
        num_train_epochs=epochs,
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size,
        learning_rate=lr,
        weight_decay=weight_decay,
        warmup_ratio=
        0.06,  # 6% warmup to match scheduler.t_warmup: 0.06dur from default config
        # Precision settings:
        bf16=True,  # Matching precision: amp_bf16 from default config
        # Batch sampler for MultipleNegativesRankingLoss:
        batch_sampler=BatchSamplers.
        NO_DUPLICATES,  # MultipleNegativesRankingLoss benefits from no duplicate samples in a batch
        # Evaluation and saving:
        eval_strategy="epoch",  # Evaluate every epoch for early stopping
        save_strategy="epoch",
        save_total_limit=1,  # Keep only the best checkpoint
        load_best_model_at_end=True if early_stopping else
        False,  # Load best model at end of training (required for early stopping)
        metric_for_best_model=metric_name
        if early_stopping else None,  # Metric to monitor for best model
        greater_is_better=greater_is_better
        if early_stopping else None,  # Direction of metric optimization
        # Logging:
        logging_steps=
        1,  # Matching console_log_interval: 1ba (log every batch) - may be verbose, adjust if needed
        # Reproducibility (seed also set manually above for full reproducibility):
        seed=seed,  # Matching seed: 25 from default config
        # Learning rate scheduler (matching linear_decay_with_warmup):
        lr_scheduler_type=
        "linear",  # Linear decay with warmup (note: transformers linear scheduler decays to 0, not 0.02x like Composer's LinearWithWarmupScheduler)
        # Wandb logging (matching loggers.wandb config):
        report_to="wandb",  # Enable wandb logging if wandb is initialized
    )

    # Define evaluators for evaluation datasets (for trainer evaluation during training)
    # Use custom NDCG evaluator
    logger.info(
        f"Creating evaluator for training monitoring (metric: {early_stopping_metric})..."
    )
    ndcg_evaluator = NDCGEvaluator(
        eval_dataset=eval_dataset,
        name=task_name,
        k=10,  # NDCG@10
        batch_size=batch_size,
        return_loss=
        monitor_loss,  # Return loss if monitoring loss, else return NDCG
        loss_model=mnrl_loss if monitor_loss else None,
    )

    # Setup callbacks
    callbacks = []
    if early_stopping:
        logger.info(
            f"Early stopping enabled: metric={metric_name}, patience={early_stopping_patience} epochs, threshold={early_stopping_threshold}"
        )
        early_stopping_callback = EarlyStoppingCallback(
            early_stopping_patience=
            early_stopping_patience,  # Stop after N evaluations without improvement
            early_stopping_threshold=
            early_stopping_threshold,  # Minimum improvement to count as improvement
        )
        callbacks.append(early_stopping_callback)
    if eval_during_training:
        trainer = SentenceTransformerTrainer(
            model=retrieval_model,
            args=retrieval_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            loss=mnrl_loss,
            evaluator=ndcg_evaluator,
            callbacks=callbacks,  # Add early stopping callback
        )
    else:
        trainer = SentenceTransformerTrainer(
            model=retrieval_model,
            args=retrieval_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            loss=mnrl_loss,
        )                                            k_values=[10])

    # Train the model
    logger.info("=== STARTING TRAINING ===")
    logger.info(
        f"Configuration: LR={lr}, WD={weight_decay}, Epochs={epochs}, BS={batch_size}"
    )
    logger.info(f"Train dataset size: {len(train_dataset)}")
    logger.info(f"Eval dataset size: {len(eval_dataset)}")
    if early_stopping:
        logger.info(
            f"Early stopping: metric={metric_name}, patience={early_stopping_patience}, threshold={early_stopping_threshold}"
        )

    trainer.train()

    # Check if training was stopped early
    actual_epochs = trainer.state.epoch
    if early_stopping and actual_epochs < epochs:
        logger.info(
            f"Training stopped early at epoch {actual_epochs}/{epochs}")
    else:
        logger.info(f"Training completed all {actual_epochs} epochs")

    logger.info("=== TRAINING COMPLETED ===")
    logger.info(f"Training history steps: {trainer.state.global_step}")
    logger.info(
        f"Training loss (last): {trainer.state.log_history[-1] if trainer.state.log_history else 'No logs'}"
    )

    # Get trained model (best model is loaded automatically if load_best_model_at_end=True)
    trained_model = trainer.model

    # Save final model
    os.makedirs(os.path.dirname(save_folder_str + "/final"), exist_ok=True)
    trained_model.save_pretrained(save_folder_str + "/final")
    logger.info(f"Model saved to: {save_folder_str}/final")

    logger.info("=== EVALUATION (AFTER TRAINING) ===")
    logger.info("--- NDCG-based Metrics (sklearn) ---")
    final_ndcg_metrics = compute_ndcg_metrics(trained_model,
                                              eval_dataset,
                                              k_values=[5, 10, 20])

    # Get test samples count
    test_samples = len(eval_dataset)
    evaluation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Return results as a dictionary - combining both evaluation methods
    return {
        'model_name': model_name,
        'task_name': task_name,
        'learning_rate': lr,
        'weight_decay': weight_decay,
        'epochs': epochs,
        'actual_epochs': int(actual_epochs),  # Actual number of epochs trained
        'batch_size': batch_size,
        'early_stopped': early_stopping and actual_epochs < epochs,
        'ndcg@10': final_ndcg_metrics['ndcg@10'], 
        'map': final_ndcg_metrics['map'], 
        'mrr': final_ndcg_metrics['mrr'], 
        'recall@10': final_ndcg_metrics['recall@10'], 
        'test_samples': test_samples,
        'evaluation_date': evaluation_date,
    }


def evaluate_retrieval_detailed(model_path, eval_dataset, k_values=[5, 10, 20]):
    """
    Comprehensive evaluation with NDCG at multiple k values.
    Performs proper query-to-corpus retrieval evaluation.
    """
    from sklearn.metrics import ndcg_score, average_precision_score
    
    # Load model
    model = SentenceTransformer(model_path)
    
    # Extract queries (anchors) and relevant documents (positives)
    anchors = list(eval_dataset["anchor"])
    positives = list(eval_dataset["positive"])
    
    # Build corpus: all unique documents that queries will be ranked against
    corpus = positives  # Corpus = all documents from eval dataset
    # Create relevance mapping: query_i is relevant to document_i
    query_to_relevant_docs = {i: [i] for i in range(len(anchors))}
    
    logger.info(f"Evaluating on {len(anchors)} queries against corpus of {len(corpus)} documents")
    
    # Encode queries and corpus documents
    query_embeddings = model.encode(anchors, convert_to_tensor=True, show_progress_bar=True)
    corpus_embeddings = model.encode(corpus, convert_to_tensor=True, show_progress_bar=True)
    
    # Compute query-to-corpus similarity matrix: similarity[i][j] = similarity(query_i, corpus_doc_j)
    similarity_matrix = cos_sim(query_embeddings, corpus_embeddings).cpu().numpy()
    
    # Build ground truth matrix: y_true[i][j] = 1 if corpus_doc_j is relevant to query_i
    y_true = np.zeros((len(anchors), len(corpus)))
    for query_idx, relevant_doc_indices in query_to_relevant_docs.items():
        for doc_idx in relevant_doc_indices:
            if doc_idx < len(corpus):
                y_true[query_idx][doc_idx] = 1.0
    
    y_score = similarity_matrix
    
    # Calculate metrics
    results = {}
    
    # NDCG@k for different k values (compute per-query, then average)
    for k in k_values:
        ndcg_scores = []
        for i in range(len(anchors)):
            if np.sum(y_true[i]) > 0:  # Only compute if query has relevant documents
                ndcg_i = ndcg_score(y_true[i:i+1], y_score[i:i+1], k=k)
                ndcg_scores.append(ndcg_i)
        results[f'ndcg@{k}'] = np.mean(ndcg_scores) if ndcg_scores else 0.0
    
    # Additional metrics: Mean Average Precision (MAP)
    # For MAP, we need to calculate AP for each query and average
    map_scores = []
    for i in range(len(anchors)):
        if np.sum(y_true[i]) > 0:  # Only compute if query has relevant documents
            # Get scores for this query
            query_scores = y_score[i]
            query_true = y_true[i]
            
            # Calculate average precision for this query
            ap = average_precision_score(query_true, query_scores)
            map_scores.append(ap)
    
    results['map'] = np.mean(map_scores) if map_scores else 0.0
    
    # Recall@k: proportion of relevant docs found in top-k
    for k in k_values:
        recall_at_k_list = []
        for i in range(len(anchors)):
            if np.sum(y_true[i]) > 0:  # Only compute if query has relevant documents
                # Get top-k indices for this query (sorted by similarity, descending)
                top_k_indices = np.argsort(y_score[i])[-k:][::-1]
                # Count how many relevant docs are in top-k
                relevant_in_topk = np.sum(y_true[i][top_k_indices])
                total_relevant = np.sum(y_true[i])
                recall = relevant_in_topk / total_relevant if total_relevant > 0 else 0.0
                recall_at_k_list.append(recall)
        results[f'recall@{k}'] = np.mean(recall_at_k_list) if recall_at_k_list else 0.0
    
    return results


def train_and_evaluate_retrieval_model(cfg):

    torch._dynamo.disable()
    
    task_content = {
        'id': cfg.retrieval_task_id
    }

    lr, weight_decay, epochs_str, batch_size = cfg.optimizer.lr, cfg.optimizer.weight_decay, cfg.max_duration, cfg.batch_size
    epochs = int(epochs_str[:-2])
    save_folder_retrieval = f"./finetuned_checkpoints/{cfg.task_type}/{cfg.dataset_name}/{cfg.hf_model_name}/" + str(
        lr) + "/" + str(weight_decay) + "/" + str(
            epochs_str) + "/" + str(batch_size)
    wandb_name = "finetuning/" + cfg.task_type + "/" + cfg.dataset_name + "/" + cfg.hf_model_name + "/" + str(
        lr) + "/" + str(weight_decay) + "/" + str(
            epochs_str) + "/" + str(batch_size)


    results = train_retrieval_model(
        model_path=cfg.model_path,
        tokenizer_name=cfg.tokenizer_name,
        is_lower=cfg.is_lower,
        task_name=cfg.dataset_name,
        task_content=task_content,
        max_seq_len=cfg.max_seq_len,
        model_name=cfg.hf_model_name,
        hf_model_name=cfg.hf_model_name,  # hf_model_name is set to model_name in model_config
        dataset_name=cfg.dataset_name,  # dataset_name is set to task_name in task_config
        task_type=cfg.task_type,
        lr=lr,
        weight_decay=weight_decay,
        epochs=epochs,
        batch_size=batch_size,
        save_folder_str=save_folder_retrieval,
        wandb_name=wandb_name,
        eval_during_training=False,
        early_stopping=False
    )

    finetuned_model_path = save_folder_retrieval + "/final/"
    
    test_dataset = build_retrieval_dataloader(
        split='test',
        tokenizer_name=cfg.tokenizer_name,
        max_seq_length=cfg.max_seq_len,
        is_lower=cfg.is_lower,
        retrieval_task_id=task_content['id'],
    )
    results = eval_retrieval(finetuned_model_path,
                   test_dataset,
                   cfg.max_seq_len,
                   batch_size,
                   k_values=[1,3,5,10,20])
    print(f"Model in the path: {finetuned_model_path}")
    print("\nDetailed Evaluation Results:")
    print("=" * 50)
    print(results)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python hyperparam_retrieval_train.py <model_config_name> <task_config_name>")
        sys.exit(1)

    model_config_name, task_config_name = sys.argv[1], sys.argv[2]

    # Initialize Hydra and load task config with defaults
    with initialize(config_path="yamls", version_base=None):
        task_cfg = compose(config_name=task_config_name)
    om.set_struct(task_cfg, False)
    
    # Load model config:
    with open(model_config_name) as f:
        model_cfg = om.load(f)
    om.set_struct(model_cfg, False)
    cfg = om.merge(task_cfg, model_cfg)
    cfg = cast(DictConfig, cfg)
    
    train_and_evaluate_retrieval_model(cfg) 
