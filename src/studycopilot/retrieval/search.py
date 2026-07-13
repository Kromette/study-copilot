from studycopilot.retrieval.schema import RetrievedChunk
from studycopilot.retrieval.collections import COLLECTION_NAME
from studycopilot.retrieval.qdrant_client import client
from studycopilot.embeddings.models import embed_query



def search(query, top_k=5):

    query_vector = embed_query(query)


    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k
    )


    chunks=[]


    for point in results.points:

        chunks.append(
            RetrievedChunk(
                text=point.payload["text"],
                source=point.payload["source"],
                page=point.payload["page"],
                score=point.score,
                document_id=point.payload["document_id"],
                chunk_id=point.payload["chunk_id"],
                chunk_index_in_page=point.payload["chunk_index_in_page"]
            )
        )


    return chunks