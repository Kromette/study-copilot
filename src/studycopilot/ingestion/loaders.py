from pathlib import Path

import fitz  # PyMuPDF
from docx import Document


SUPPORTED_EXTENSIONS = {".pdf", ".docx"}


def load_document(file_path: Path) -> str:
    """
    Load a supported document and return its text.

    Args:
        file_path: Path to the document.

    Returns:
        Extracted text.

    Raises:
        ValueError: If the file extension is not supported.
    """

    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        return _load_pdf(file_path)

    if suffix == ".docx":
        return _load_docx(file_path)

    raise ValueError(f"Unsupported file type: {suffix}")


def _load_docx(file_path: Path) -> str:
    """Extract text from a Word document."""

    document = Document(file_path)

    paragraphs = [
        paragraph.text.strip()
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    ]

    return "\n".join(paragraphs)


def _load_pdf(file_path: Path) -> str:
    """Extract text from a PDF."""

    text = []

    with fitz.open(file_path) as pdf:
        for page in pdf:
            page_text = page.get_text()

            if page_text:
                text.append(page_text)

    return "\n".join(text)