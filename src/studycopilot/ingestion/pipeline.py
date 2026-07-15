from pathlib import Path
import uuid

from studycopilot.utils.hash import compute_file_hash
from studycopilot.retrieval.documents import get_document_by_hash

from studycopilot.ingestion.loaders import load_document
from studycopilot.ingestion.chunking import create_chunks
from studycopilot.retrieval.indexing import index_chunks

def normalize_document(document):
    """
    Convert loaded documents into a common page-based format.

    PDF:
        already page structured

    DOCX:
        converted into a single page
    """

    # PDF case
    if isinstance(document, list):

        return document


    # DOCX case
    return [
        {
            "text": document.text,
            "page": 1,
            "source": document.filename,
            "total_pages": 1,
        }
    ]


def ingest_document(
    file_path: Path,
):

    file_hash = compute_file_hash(
        file_path
    )


    existing_document = get_document_by_hash(
        file_hash
    )


    if existing_document:

        return existing_document



    document_id = str(
        uuid.uuid4()
    )


    document = load_document(
        file_path
    )


    pages = normalize_document(
        document
    )


    chunks = create_chunks(
        pages,
        document_id=document_id,
        file_hash=file_hash,
    )


    index_chunks(
        chunks
    )


    return document_id