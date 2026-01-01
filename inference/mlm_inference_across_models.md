# MLM Inference Results

We conducted masked language modeling (MLM) [inference](./mlm_inference_across_models.py) experiments using token-level masking to evaluate the performance of several Turkish BERT models. The models tested include three uncased BERT variants (Artiwise ModernBERT, YTU BERT, and DBMDZ BERTurk) along with our own TabiBERT model in both cased and uncased versions. For each dataset, we sampled 2,500 examples and performed two inference runs, reporting the averaged accuracy scores below. The highest accuracy for each row is highlighted in bold.

Dataset            | Mask | Artiwise ModernBERT | YTU BERT  | DBMDZ BERTurk   | TabiBERT-uncased |TabiBERT-cased   
------------------ | ---- | ------------------- | --------- | --------------- | --------------------- | ----
Biomedical Dataset |  5%  | 57.48               | 49.60     | **62.48**       | 54.38                 | 58.03 
Biomedical Dataset | 10%  | 54.82               | 47.29     | **59.46**       | 51.99                 | 54.15                 
Biomedical Dataset | 15%  | 51.41               | 44.57     | **56.93**       | 48.68                 | 50.98 
QA Dataset         | 5%   | 73.82               | 61.16     | 78.66           | 78.51                 | **80.08**                
QA Dataset         | 10%  | 70.95               | 58.70     | 76.09           | 76.14                 | **77.64**                 
QA Dataset         | 15%  | 69.09               | 56.35     | 73.88           | 74.08                 | **75.39**                 
Review Dataset     | 5%   | 59.02               | 45.72     | 61.63           | 61.60                 | **62.12** 
Review Dataset     | 10%  | 55.95               | 43.57     | 58.81           | 59.13                 | **59.54**      
Review Dataset     | 15%  | 53.12               | 41.53     | **56.38**       | 56.36                 | 56.31                 

