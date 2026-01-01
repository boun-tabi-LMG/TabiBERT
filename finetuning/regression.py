"""Alternative regression model that uses pre-computed loss."""

import torch
import torch.nn.functional as F
from composer.models import HuggingFaceModel
from composer.metrics import LossMetric
from scipy.stats import pearsonr, spearmanr
import numpy as np


class RegressionHuggingFaceModel(HuggingFaceModel):
    """Custom HuggingFace model wrapper for regression tasks."""
    
    def __init__(self, model):
        super().__init__(model)
    
    def forward(self, batch):
        """Forward pass that includes labels for loss computation."""
        # Include labels in the forward pass so model computes loss
        return self.model(
            input_ids=batch['input_ids'],
            attention_mask=batch.get('attention_mask'),
            labels=batch['labels']
        )
    
    def loss(self, outputs, batch):
        """Use pre-computed loss from model output."""
        if isinstance(outputs, dict) and 'loss' in outputs:
            return outputs['loss']
        else:
            raise ValueError(f"Expected 'loss' in outputs, got keys: {list(outputs.keys()) if isinstance(outputs, dict) else 'Not a dict'}")

    def get_metrics(self, is_train: bool = False):
        metrics = super().get_metrics(is_train)
        
        def _loss_fn(outputs, batch):
            return self.loss(outputs, batch)
            
        metrics["loss"] = LossMetric(loss_function=_loss_fn)
        return metrics