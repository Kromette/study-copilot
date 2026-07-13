from pathlib import Path

from studycopilot.ingestion.loaders import _load_pdf
from studycopilot.ingestion.chunking import create_chunks

from studycopilot.retrieval.collections import create_collection
from studycopilot.retrieval.indexing import index_chunks


import uuid


document_id = str(uuid.uuid4())


pages = _load_pdf(
    "data/uploads/cours.pdf"
)


chunks = create_chunks(
    pages,
    document_id=document_id
)


print(
    f"{len(chunks)} chunks created"
)


create_collection()


index_chunks(
    chunks
)


print("Indexation completed")