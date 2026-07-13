from qdrant_client.models import (
    VectorParams,
    Distance
)

from studycopilot.retrieval.qdrant_client import client


COLLECTION_NAME = "course_documents"


def create_collection():

    collections = [
        c.name
        for c in client.get_collections().collections
    ]

    if COLLECTION_NAME not in collections:

        client.create_collection(

            collection_name=COLLECTION_NAME,

            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )