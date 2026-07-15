from studycopilot.retrieval.qdrant_client import client
from studycopilot.retrieval.collections import COLLECTION_NAME



def get_document_by_hash(
    file_hash: str,
):

    result = client.scroll(
        collection_name=COLLECTION_NAME,

        scroll_filter={
            "must": [
                {
                    "key": "file_hash",
                    "match": {
                        "value": file_hash
                    }
                }
            ]
        },

        limit=1,
    )


    points, _ = result


    if not points:
        return None


    return points[0].payload["document_id"]