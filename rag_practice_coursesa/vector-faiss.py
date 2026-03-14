import numpy as np
from openai import OpenAI
import faiss
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def user_query(query):
    messages: list[dict[str, str]] = [
        {"role": "system", "content": "You are a helpful AI engineer."},
        {"role": "user", "content": {query}}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-oss:20b",
            messages=messages
        )
        print(response.choices[0].message.content)
    except Exception as e:
        print("Error:", e)


def get_embedding(text: str) -> np.ndarray:
    """
    Generate embedding vector from text and return numpy array.
    :param text:
    :return:
    """
    response = client.embeddings.create(
        model="nomic-embed-text:latest",
        input=text
    )

    embedding = response.data[0].embedding

    return np.array(embedding, dtype=np.float32)

def get_embeddings(texts: list[str]) -> np.ndarray:
    """
    Generate embedding vectors for a list of texts.

    :param texts: list of input strings
    :return: numpy matrix (n_texts, embedding_dimension)
    """

    response = client.embeddings.create(
        model="nomic-embed-text:latest",
        input=texts
    )
    embeddings = [item.embedding for item in response.data]

    return np.array(embeddings, dtype=np.float32)

def inspect_vectors(vectors: np.ndarray):
    print("Vector type:", type(vectors))
    print("Matrix shape:", vectors.shape)

    print("Number of vectors:", vectors.shape[0])
    print("Vector dimension:", vectors.shape[1])

    print("\nSample vector:")
    print(vectors[0][:10])  # first 10 values


def main():
    #user_query("Explain event-driven architecture");
    text = "We have two apples in a bucket"
    text1 = "What do we have in bucket?"

    texts = [
        "Event driven architecture with Kafka",
        "Microservices communication patterns",
        "What is the weather today?",
        "Vector databases for AI applications"
    ]

    vectors = get_embeddings(texts)

    inspect_vectors(vectors)

    query_vector1 = get_embedding(text)
    query_vector2 = get_embedding(text1)

    print(f"Type: {type(query_vector1)}")
    # This will output the number of dimensions of the embedding
    print(f"Vector shape 1 {query_vector1.shape}")
    print(f"vector dimension {query_vector1.shape[0]}")
    #get size of each index vector
    dimension1 = len(query_vector1)
    print(f"Size of dimension {dimension1}")

    dimension2 = len(query_vector2)

    # create index for FAISS from a size of each index vector
    faiss_index = faiss.IndexFlatL2(dimension1) #L2 distance
    embeddings1 = np.array([query_vector1],dtype='float32')
    faiss_index.add(embeddings1)
    print(f"Index contains {faiss_index.ntotal} vectors (elements)")
    query_vector2 = np.array([query_vector2],dtype='float32')
    distances, indices = faiss_index.search(query_vector2, 1) # Find the closest match
    print(f"Closest match found at index {indices[0][0]} with distances: {distances[0][0]}")
    #Retrieve the actual documents based on the return indices
    for i in indices[0]:
        print(f"matched doc {i}")

    # embeddings2 = np.array([vector2], dtype='float32')
    # faiss_index.add(embeddings2)
    # print(f"Index contains {faiss_index.ntotal} vectors (elements)")
    # print(f"Vector shape 2 {vector2.shape}")


if __name__ == "__main__":
    main()
