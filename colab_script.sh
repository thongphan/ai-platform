#!/bin/bash
echo "--- Starting DevOps Deployment on Colab ---"

# Set Paths
BASE_DIR="/content/RAG-system"
IMAGE_FILE="$BASE_DIR/llama_api_deploy.tar"
APP_NAME="llama-api-app"

# 1. Initialize udocker
if ! command -v udocker &> /dev/null; then
    echo "[INFO] Installing udocker..."
    pip install udocker &> /dev/null
    udocker --allow-root install &> /dev/null
fi

# 2. Hard Cleanup (Important for fresh starts)
echo "[INFO] Cleaning up old containers/images..."
udocker --allow-root rm -f api_service &> /dev/null
udocker --allow-root rmi $APP_NAME &> /dev/null

# 3. Load the Image
echo "[INFO] Loading image (this may take a moment)..."
udocker --allow-root load -i "$IMAGE_FILE"

# 4. Create and Run in Background
echo "[INFO] Creating container..."
udocker --allow-root create --name=api_service $APP_NAME

echo "[INFO] Starting FastAPI server..."
# Note: we use -p 8000:8000 to match your EXPOSE 8000 in Dockerfile
nohup udocker --allow-root run -e ENV=colab -p 8000:8000 api_service > "$BASE_DIR/api_logs.txt" 2>&1 &

echo "--- Deployment Complete ---"
echo "View logs at: $BASE_DIR/api_logs.txt"