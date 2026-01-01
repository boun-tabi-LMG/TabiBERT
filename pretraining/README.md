# 📘 Pre-training ModernBERT on Turkish Data

This guide provides a walkthrough for pre-training [ModernBERT](https://huggingface.co/answerdotai/ModernBERT-base) on Turkish data using the ModernBERT framework with custom configurations. 
See the [training guidelines](https://github.com/AnswerDotAI/ModernBERT/blob/main/README.md#training) for details.

## 📋 Prerequisites

- **8 × H100 SXM GPUs**
- **~1000 GB storage** for data and checkpoints
- **Wandb access** for training logs
- **Turkish dataset** prepared and accessible

Verify GPU access:
```bash
nvidia-smi
```

## 📁 Phase 1: Environment Setup and Data Preparation

1. **Install dependencies:**
   ```bash
   bash pretraining-setup.sh
   ```

2. **Prepare data:**
   ```bash
   mkdir -p dataset_folder
   cp /path/to/your/1k_dataset/ dataset_folder/
   cp /path/to/your/8k_dataset/ dataset_folder/
   ```

3. **Configure YAML files:** Use the provided configs in this directory as examples. Update dataset paths, tokenizer names, `max_duration` and any other field as needed.

4. **Source code modification:** Update [src/text_data.py](https://github.com/AnswerDotAI/ModernBERT/blob/main/src/text_data.py) (line 485) in the ModernBERT repository:
   ```python
   if self.tokenizer.pad_token is None:
       self.tokenizer.pad_token = self.tokenizer.eos_token
   ```

## 🚀 Phase 2: Launch & Monitor Training

1. **Start training:**
   ```bash
   composer main.py yamls/pretraining/your-config.yaml
   ```

2. **Monitor progress:**
   ```bash
   nvitop  # GPU monitoring
   ```

3. **Checkpoint management:**
   - Checkpoints saved per `save_interval`
   - Monitor disk space: `df -h`
   - Backup important checkpoints

## 🧠 Best Practices

- Start with a small dataset to verify configuration
- Monitor loss curves and GPU utilization (>90% target)
- Keep track of disk space and GPU memory
- Use gradient clipping if needed

## ⚠️ Common Issues & Solutions

- **Out of Memory:** Reduce batch size
- **Slow Training:** Check GPU utilization, verify data pipeline (avoid network volumes), consider pretokenization
- **Tokenizer Issues:** Verify vocabulary size, special tokens, and padding token setup

## 📎 Additional Resources

- [ModernBERT GitHub](https://github.com/answerdotai/ModernBERT)
- [HuggingFace ModernBERT](https://huggingface.co/answerdotai/ModernBERT-base)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)



