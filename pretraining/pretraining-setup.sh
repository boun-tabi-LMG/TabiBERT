echo "Cloning ModernBERT"
git clone https://github.com/AnswerDotAI/ModernBERT.git
cd ModernBERT
git checkout pretraining_documentation

echo "Requirements are installed"
pip install -r requirements.txt

echo "Installing transformers"
pip install transformers
pip install --upgrade transformers

echo "Installing nvitop"
pip install nvitop

echo "Installing torch-optimi"
pip install torch-optimi 

echo "Installing numba"
pip install numba

echo "Installing wheel"
pip install wheel

echo "Installing flash_attn"
pip install "flash_attn==2.6.3" --no-build-isolation

pip install mosaicml-streaming
echo "Ready to start training"

echo "Logging in to Hugging Face:"
huggingface-cli login
