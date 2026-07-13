from dataclasses import dataclass


@dataclass
class RetrievedChunk:

    text: str

    source: str

    page: int

    score: float

    document_id: str

    chunk_id: int

    chunk_index_in_page: int

    @property
    def citation(self) -> str:
        return f"{self.source} - page {self.page}"