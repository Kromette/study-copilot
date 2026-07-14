from studycopilot.retrieval.search import search
from studycopilot.generation.service import generate_quiz

user_prompt = "Help me study amino acids"

chunks = search(user_prompt)

quiz = generate_quiz(
    user_question=user_prompt,
    retrieved_chunks=chunks,
)

print(quiz)