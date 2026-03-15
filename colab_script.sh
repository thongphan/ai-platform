#!/bin/bash

#!chmod +x colab_script.sh
#!bash colab_script.sh

echo "Starting AI Platform..."

# clone repo if not exists
if [ ! -d "ai-platform" ]; then
  git clone https://github.com/thongphan/ai-platform.git
fi

cd ai-platform

echo "Pull latest code"
git pull origin main

echo "Install dependencies"
pip install -r requirements.txt

echo "Set environment"
export ENV=colab

echo "Start FastAPI"
nohup uvicorn app.app:app --host 0.0.0.0 --port 8000 &

echo "Start Cloudflare tunnel"
wget -q https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
chmod +x cloudflared-linux-amd64

./cloudflared-linux-amd64 tunnel --url http://localhost:8000