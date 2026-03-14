FROM python:3.11-slim

# DevOps Environment Setup
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    ENV=colab \
    PYTHONPATH=/app

WORKDIR /app

# 1. Install dependencies (Layer 1)
COPY rag_practice_coursesa.txt .
RUN pip install --no-cache-dir -r rag_practice_coursesa.txt

# 2. Copy code (Layer 2)
COPY . .

# 3. Fix potential import issues
RUN touch app/__init__.py

EXPOSE 8000

# 4. Start FastAPI
# Using the module path relative to WORKDIR /app
CMD ["uvicorn", "app.fastapi:app", "--host", "0.0.0.0", "--port", "8000"]