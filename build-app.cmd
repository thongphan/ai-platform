# 1. Create a specialized builder that supports flat exports
docker buildx create --name colab_builder --use

# 2. Build and Export directly to the TAR file
# This is the ONLY way to guarantee no 'index.json' on modern Windows Docker
docker buildx build `
  --platform linux/amd64 `
  --provenance=false `
  --output type=docker,dest=llama_api_deploy.tar `
  -t llama-api-app .

# 3. Remove the builder (Cleanup)
docker buildx rm colab_builder