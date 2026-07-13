from sentence_transformers import SentenceTransformer

MODEL_NAME = "BAAI/bge-small-en-v1.5"

model = SentenceTransformer(MODEL_NAME)


def embed_documents(
    texts: list[str]
) -> list[list[float]]:

    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        batch_size=32
    )

    return embeddings.tolist()