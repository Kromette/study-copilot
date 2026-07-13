from sentence_transformers import SentenceTransformer


MODEL_NAME = "BAAI/bge-small-en-v1.5"


model = SentenceTransformer(MODEL_NAME)


def embed(text: str) -> list[float]:
    """
    Convert text into an embedding vector.
    """

    embedding = model.encode(
        text,
        normalize_embeddings=True
    )

    return embedding.tolist()