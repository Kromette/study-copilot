from studycopilot.generation.prompt import build_mcq_prompt
from studycopilot.retrieval.schema import RetrievedChunk


context = [
    RetrievedChunk(
        text="Amino acids are the building blocks of proteins. They play a crucial role in enzyme function.",
        source="cours.pdf",
        page=1,
        score=0.9,
        document_id="doc1",
        chunk_id=0,
        chunk_index_in_page=0,
    )
]

user_question = "What do amino acids do?"

prompt = build_mcq_prompt(user_question, context)
print(prompt)
