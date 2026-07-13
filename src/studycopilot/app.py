import streamlit as st
from pathlib import Path

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

    st.success("Document saved!")