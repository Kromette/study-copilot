from qdrant_client import QdrantClient

from studycopilot.config import settings


client = QdrantClient(
    url=settings.qdrant_url
)