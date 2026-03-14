"""
Semantic Search Pipeline

Query
  │
  ▼
Embedding
  │
  ▼
Vector search Top-K
  │
  ▼
Re-ranking (optional)
  │
  ▼
Top context
  │
  ▼
LLM response
"""

import numpy as np
import faiss
from infrastructure.clients.ollama_client import OllamaClient


MODEL_NAME = "nomic-embed-text:latest"


documents = [
    "Event driven architecture using Kafka",
    "Microservices communicate via asynchronous events",
    "Airflow is used for workflow orchestration",
    "Vector databases enable semantic search",
    "Kafka streams process real time events"
]


# -----------------------------
# Embedding Service
# -----------------------------
def get_embeddings(texts: list[str]) -> np.ndarray:
    """
    Generate embeddings for a list of texts.
    Returns numpy array (N, dimension) float32.
    """

    client = OllamaClient.get_client()

    response = client.embeddings.create(
        model=MODEL_NAME,
        input=texts
    )

    vectors = [item.embedding for item in response.data]

    return np.asarray(vectors, dtype=np.float32)


# -----------------------------
# Build Vector Index
# -----------------------------
def build_index(vectors: np.ndarray) -> faiss.IndexFlatL2:
    """
    Create FAISS index from embedding vectors.
    """

    if vectors.dtype != np.float32:
        vectors = vectors.astype("float32")

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(vectors)

    return index


# -----------------------------
# Search Function
# -----------------------------
def semantic_search(
        query: str,
        index: faiss.IndexFlatL2,
        documents: list[str],
        k: int = 3
):
    """
    Run semantic search and return ranked results.
    """

    query_vector = get_embeddings([query])

    distances, indices = index.search(query_vector, k)

    results = []

    for rank, idx in enumerate(indices[0]):

        results.append({
            "rank": rank + 1,
            "distance": float(distances[0][rank]),
            "document": documents[idx]
        })

    return results


# -----------------------------
# Pipeline Execution
# -----------------------------

# Step 1: embed documents
doc_vectors = get_embeddings(documents)

print("Embedding shape:", doc_vectors.shape)
print()

# Step 2: build vector index
index = build_index(doc_vectors)

# Step 3: query
query = "How do microservices communicate with events?"

results = semantic_search(
    query=query,
    index=index,
    documents=documents,
    k=3
)

# Step 4: print results
print("Query:", query)
print()

for r in results:

    print("Rank:", r["rank"])
    print("Distance:", r["distance"])
    print("Document:", r["document"])
    print()