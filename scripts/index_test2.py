from studycopilot.retrieval.qdrant_client import client
from studycopilot.retrieval.collections import COLLECTION_NAME


points = client.scroll(
    collection_name=COLLECTION_NAME,
    limit=3,
)


for point in points[0]:
    print(point.payload)