import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
from studycopilot.ingestion.loaders import load_document

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

st.set_page_config(page_title="StudyCopilot")

st.title("🧠 StudyCopilot")

uploaded_file = st.file_uploader(
    "Upload your course",
    type=["pdf", "docx"],
)

if uploaded_file:

    destination = UPLOAD_DIR / uploaded_file.name

    with open(destination, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Document uploaded successfully!")

    text = load_document(destination)

    st.metric(
        label="Number of characters",
        value=len(text),
    )

    st.subheader("Preview")
    st.text_area(
    "Preview",
    value=text[:1000],
    height=300,
)