from pathlib import Path

import streamlit as st
from studycopilot.ingestion.loaders import load_document
from studycopilot.generation.service import generate_quiz
from studycopilot.retrieval.search import search

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

    loaded_document = load_document(destination)

    if isinstance(loaded_document, list):
        text = "\n\n".join(page["text"] for page in loaded_document)
        filename = destination.name
    else:
        text = loaded_document.text
        filename = loaded_document.filename

    st.metric(
        label="Number of characters",
        value=len(text),
    )

    st.subheader("Preview")
    st.text_area(
        label=filename,
        value=text[:1000],
        height=300,
    )
    
    query = st.text_input(
        "Topic to generate questions about",
        placeholder="e.g. Amino acids"
    )

    if "quiz" not in st.session_state:
        st.session_state.quiz = None

    generate = st.button("Generate quiz")
    if generate and query:
        chunks = search(
            query=query,
            top_k=5,
        )

        st.session_state.quiz = generate_quiz(
            user_question=query,
            retrieved_chunks=chunks,
            nb_questions=5,
        )

    quiz = st.session_state.quiz
    if quiz is not None:
        for i, question in enumerate(quiz.questions):
            st.subheader(f"Question {i+1}")
            st.write(question.question)

            st.radio(
                "Choose one answer",
                question.options,
                key=f"q{i}",
            )

            if st.button("Show answers", key=f"show_answers_{i}"):
                user_answer = st.session_state.get(f"q{i}")
                correct = question.options[question.correct_answer_index]

                if user_answer == correct:
                    st.success("Correct!")
                else:
                    st.error(f"Correct answer: {correct}")

                st.info(question.explanation)