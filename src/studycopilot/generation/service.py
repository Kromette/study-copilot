import json

from studycopilot.generation.prompt import build_mcq_prompt
from studycopilot.generation.llm import generate
from studycopilot.generation.schema import Quiz, MCQQuestion


def generate_quiz(
    user_question: str,
    retrieved_chunks,
    nb_questions: int = 1,
) -> Quiz:
    """
    Generate a multiple-choice quiz from retrieved chunks.
    """

    prompt = build_mcq_prompt(
        user_question,
        retrieved_chunks,
        nb_questions
    )

    raw_response = generate(prompt)
    print("Raw response from LLM:", raw_response)  # Debugging line

    try:

        data = json.loads(raw_response)

    except json.JSONDecodeError:

        raise ValueError(
            "The LLM did not return valid JSON."
        )

    questions = []

    for question in data:

        questions.append(
            MCQQuestion(
                question=question["question"],
                options=question["options"],
                correct_answer_index=question["correct_option_index"],
                explanation=question["explanation"],
            )
        )

    return Quiz(
        questions=questions,
    )