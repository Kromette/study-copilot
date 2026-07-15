from pathlib import Path

import streamlit as st


from studycopilot.ingestion.pipeline import ingest_document
from studycopilot.retrieval.search import search
from studycopilot.generation.service import generate_quiz


UPLOAD_DIR = Path(
    "data/uploads"
)

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)

DEBUG_MODE = st.sidebar.checkbox(
    "🔍 Enable debug mode",
    value=False,
)

st.set_page_config(
    page_title="StudyCopilot"
)


st.title(
    "🧠 StudyCopilot"
)


# -------------------------
# Session state
# -------------------------

if "document_id" not in st.session_state:
    st.session_state.document_id = None


if "filename" not in st.session_state:
    st.session_state.filename = None


if "quiz" not in st.session_state:
    st.session_state.quiz = None

if "debug" not in st.session_state:
    st.session_state.debug = {}


# -------------------------
# Upload
# -------------------------

uploaded_file = st.file_uploader(
    "Upload your course",
    type=["pdf", "docx"],
)


if uploaded_file:


    # nouveau document
    if (
        st.session_state.filename
        != uploaded_file.name
    ):


        destination = (
            UPLOAD_DIR
            /
            uploaded_file.name
        )


        with open(
            destination,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )


        st.success(
            "Document uploaded!"
        )


        with st.spinner(
            "Indexing document..."
        ):

            document_id = ingest_document(
                destination
            )


        st.session_state.document_id = document_id

        st.session_state.filename = uploaded_file.name

        st.session_state.quiz = None


        st.success(
            "Document indexed successfully!"
        )



    # -------------------------
    # Preview
    # -------------------------

    from studycopilot.ingestion.loaders import load_document


    document = load_document(
        UPLOAD_DIR / uploaded_file.name
    )


    if isinstance(document, list):

        text = "\n\n".join(
            page["text"]
            for page in document
        )

    else:

        text = document.text


    with st.expander("📄 Preview document"):

        st.write(
            f"**Filename:** {uploaded_file.name}"
        )

        st.write(
            f"**Characters:** {len(text):,}"
        )

        st.text_area(
            "Extracted text",
            value=text[:2000],
            height=300,
        )


    # -------------------------
    # Generate quiz
    # -------------------------


    query = st.text_input(
        "Topic",
        placeholder="e.g. Amino acids"
    )


    generate = st.button(
        "Generate quiz",
        disabled=(
            not query
            or st.session_state.document_id is None
        )
    )


    if generate:


        with st.spinner(
            "Searching relevant content..."
        ):

            chunks = search(
                query=query,
                top_k=5,
            )

            st.session_state.debug["query"] = query

            st.session_state.debug["retrieved_chunks"] = chunks


        with st.spinner(
            "Generating quiz..."
        ):


            st.session_state.quiz = generate_quiz(
                user_question=query,
                retrieved_chunks=chunks,
                nb_questions=5,
            )



# -------------------------
# Display infos in debug mode
# -------------------------

if DEBUG_MODE and chunks:

    with st.expander(
        "🔎 Retrieval debug"
    ):

        st.write(
            "Query:",
            st.session_state.debug["query"]
        )


        for i, chunk in enumerate(chunks):

            st.markdown(
                f"""
                ### Chunk {i+1}

                Score: {chunk.score}

                Source: {chunk.source}

                Page: {chunk.page}

                Id: {chunk.chunk_id}
                """
            )

            st.text(
                chunk.text
            )

            st.divider()

# -------------------------
# Display quiz
# -------------------------
   
quiz = st.session_state.quiz


if quiz:


    st.divider()

    st.header(
        "Your quiz"
    )


    for i, question in enumerate(
        quiz.questions
    ):


        st.subheader(
            f"Question {i+1}"
        )


        st.write(
            question.question
        )


        st.radio(
            "Choose one answer",
            question.options,
            key=f"question_{i}",
        )



        if st.button(
            "Show answer",
            key=f"answer_{i}"
        ):


            user_answer = st.session_state[
                f"question_{i}"
            ]


            correct_answer = (
                question.options[
                    question.correct_answer_index
                ]
            )


            if user_answer == correct_answer:

                st.success(
                    "Correct!"
                )

            else:

                st.error(
                    f"Correct answer: {correct_answer}"
                )


            st.info(
                question.explanation
            )