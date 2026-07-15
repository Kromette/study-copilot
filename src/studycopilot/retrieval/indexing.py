from qdrant_client.models import PointStruct
from studycopilot.retrieval.collections import COLLECTION_NAME
from studycopilot.retrieval.qdrant_client import client
from studycopilot.embeddings.models import embed_documents
import uuid


def index_chunks(chunks):

    texts = [
        chunk.text
        for chunk in chunks
    ]


    vectors = embed_documents(
        texts
    )

    points = []


    for chunk, vector in zip(
        chunks,
        vectors
    ):

        points.append(

            PointStruct(

                id=str(uuid.uuid4()),

                vector=vector,

                payload={
                    "text": chunk.text,
                    "source": chunk.source,
                    "document_id": chunk.document_id,
                    "page": chunk.page,
                    "chunk_id": chunk.chunk_id,
                    "chunk_index_in_page": chunk.chunk_index_in_page,
                    "total_pages": chunk.total_pages,
                    "file_hash": chunk.file_hash
                }
            )
        )


    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )