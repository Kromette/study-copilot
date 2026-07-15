from dataclasses import dataclass


from dataclasses import dataclass


@dataclass
class DocumentChunk:
    text: str
    source: str
    chunk_id: int
    chunk_index_in_page: int
    document_id: str
    total_pages: int
    file_hash: str
    page: int | None = None