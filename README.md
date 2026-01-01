# Welcome!

[![arXiv](https://img.shields.io/badge/arXiv-2512.23065-b31b1b.svg)](https://arxiv.org/abs/2512.23065)
[![Hugging Face](https://img.shields.io/badge/🤗-Model-yellow.svg)](https://huggingface.co/boun-tabilab/TabiBERT)
[![Benchmark](https://img.shields.io/badge/Benchmark-TabiBench-purple)](https://huggingface.co/collections/boun-tabilab/tabibench)
[![Code license](https://img.shields.io/badge/License-Apache%202.0-green.svg)](https://www.apache.org/licenses/LICENSE-2.0)
<!-- [![GitHub Repo stars](https://img.shields.io/github/stars/boun-tabi-LMG/TabiBERT)](https://github.com/boun-tabi-LMG/TabiBERT/stargazers) -->

This is the research repository for TabiBERT and TabiBench, focused on pre-training, inference, and fine-tuning procedures. 
Please visit to the TabiBERT [model card](https://huggingface.co/boun-tabilab/TabiBERT) on HuggingFace, to utilize the model; and the TabiBench [collection](https://huggingface.co/collections/boun-tabilab/tabibench) for the good quality Turkish NLP evaluation benchmarks. 

*TabiBERT and TabiBench are built by [Tabilab](https://tabilab.cmpe.bogazici.edu.tr/) in collaboration with [VNGRS](https://vngrs.com/).*

## Table of Contents
* [Project Structure](#project-structure)
* [TabiBERT](#tabibert)
   * [Training](#training)  
   * [Evaluation](#evaluation)  
* [TabiBench](#tabibench)
* [License](#license)  
* [Citation](#citation)  

---

## Project Structure

This repository includes full pipelines for **pretraining**, **inference**, and **fine-tuning**.

```
TabiBERT/
├── pretraining/                # Pre-training configurations
├── finetuning/                 # Fine-tuning scripts for downstream tasks
├── inference/                  # Inference pipeline and checkpoint evaluation tools
```

*Please refer to the READMEs under the corresponding directories, to gain insight into how to pretrain, finetune or infer on TabiBERT.*

---

## TabiBERT

**TabiBERT** is a modernized encoder-only Transformer model (BERT-style) based on the [ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) architecture.
TabiBERT is pre-trained on **1 trillion tokens from scratch** with a native context length of up to 8,192 tokens. 

### Training

* **Architecture**: Encoder-only, Pre-Norm Transformer with GeGLU activations.
* **Sequence Length**: Pre-trained up to 1,024 tokens, then extended to 8,192 tokens.
* **Data**: 86 billion tokens from a union corpus (Turkish; plus English, code with English commentary, and math in English; ~13% non-Turkish).
* **Optimizer**: StableAdamW with trapezoidal LR scheduling and 1-sqrt decay.
* **Hardware**: Trained on **8x H100 GPUs**.

#### Pre-training Data

TabiBERT has been **pre-trained on 86 billion tokens** of diverse data, primarily:

- A large-scale **Turkish corpus** covering literature, news, social media, Wikipedia, and academic 
texts.  
- **English text**, **code with English commentary**, and **math problems in English** — together making up about **13% non-Turkish** tokens.  

### Evaluation

TabiBERT was comprehensively evaluated on **[TabiBench](#tabibench)**, a benchmark consisting of **28 datasets** spanning **8 task categories**. 
The model achieves state-of-the-art performance among Turkish models, with a total average score of **77.58**, 
surpassing the previous best Turkish model by **1.62 points**.

The hyper-parameter and fine-tuning codes will be published here soon.

#### Evaluation Methodology

Systematic hyperparameter tuning was performed for all model-task pairs with the following search space:
| Parameter | Values |
|-----------|--------|
| Learning Rate | 5e-6, 1e-5, 2e-5, 3e-5 |
| Weight Decay | 1e-5, 1e-6 |
| Batch Size | 16, 32 |
| Epochs | Up to 10, with early stopping |

---

## TabiBench

**TabiBench** is a comprehensive evaluation benchmark, developed to address the lack of standardized evaluation benchmarks in Turkish NLP research. 
TabiBench provides a unified framework for assessing the performance of Turkish language models across a diverse set of downstream tasks. 
The benchmark is curated by combining high-quality existing Turkish NLP datasets with newly created and translated datasets, ensuring comprehensive coverage of various NLP capabilities.
All datasets included in TabiBench undergo rigorous quality assessment based on three key criteria: 

1. clear patterns between input text and output labels,
2. mutually exclusive labels ensuring each example belongs to only one class, and
3. clear and consistently applied annotation guidelines to guarantee label reliability. 

This manual quality assessment ensures that the evaluation benchmarks reflect realistic and meaningful downstream applications. 
To support reproducibility and fair comparison, TabiBench implements a consistent data split generation methodology across all datasets, standardizing train, validation, and test splits where needed. 
The benchmark is publicly available on [HuggingFace](https://huggingface.co/collections/boun-tabilab/tabibench) and covers eight major task categories: 
Text Classification (4 datasets), Token Classification (4 datasets), Semantic Textual Similarity (2 datasets), Natural Language Inference (2 datasets), Question Answering (2 datasets), Information Retrieval (6 datasets), Code Retrieval (4 datasets), and Academic Understanding Tasks (4 datasets).

---

## License

Released under the **Apache 2.0** license.

## Citation

```
@misc{Türker2025Tabibert,
      title={TabiBERT: A Large-Scale ModernBERT Foundation Model and Unified Benchmarking Framework for Turkish}, 
      author={Melikşah Türker and Asude Ebrar Kızıloğlu and Onur Güngör and Susan Üsküdarlı},
      year={2025},
      eprint={2512.23065},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2512.23065}, 
}
```

## Contributing
Contributions are welcome!
Feel free to open issues or submit Pull Requests 💡