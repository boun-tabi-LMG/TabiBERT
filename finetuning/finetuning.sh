pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124

echo "Requirements are installed"
pip install -r requirements.txt

pip install flash-attn==2.7.4.post1 --no-build-isolation

pip install -U "huggingface_hub[cli]"

export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

pip install transformers -U
pip install 'accelerate>=0.26.0'
pip install sentence_transformers
# pip install --upgrade typing_extensions