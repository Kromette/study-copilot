from studycopilot.retrieval.schema import RetrievedChunk

def build_mcq_prompt(user_question: str, context: list[RetrievedChunk], nb_questions: int = 1) -> str:
    """
    Build a prompt for generating a multiple-choice question (MCQ) based on the user's question and context.

    Args:
        user_question (str): The user's question.
        context (list[RetrievedChunk]): The context or information to base the MCQ on.
        nb_questions (int): The number of questions to generate.

    Returns:
        str: A formatted prompt string for generating an MCQ.
    """
    prompt = f"""
ROLE: Expert science teacher
You are an expert science teacher who writes clear, exam-style multiple-choice questions (MCQs) for revision.

OBJECTIVE:
Generate {nb_questions} MCQ(s) that address the user's request: {user_question}

CONTEXT:
Use ONLY information contained in the provided context: {context}
Do NOT invent facts or use external knowledge beyond the context.

REQUIREMENTS (mandatory):
- Output must be valid JSON and NOTHING else (no explanation outside JSON).
- Return a JSON list with exactly {nb_questions} question object(s).
- Provide exactly 4 options in the "options" list for each question.
- Indicate the correct option by the 0-based integer field "correct_option_index".
- Include a short "explanation" (<=30 words) that cites how the context supports the answer.
- Include "references": a list of objects with keys "source" and "page" referencing the context entries used.

OUTPUT SCHEMA (exact keys required):
[{{"question": "<string>", "options": ["<str>", "<str>", "<str>", "<str>"], "correct_option_index": <int 0-3>, "explanation": "<string up to 30 words>", "references": [{{"source":"<filename>","page":<int>}}]}}]

EXAMPLE (for illustration only - your output must be JSON exactly like the schema):
User question: "Ask le about the functions of amino acids."
Context: [RetrievedChunk(source='cours.pdf', page=1, text='Amino acids are the building blocks of proteins. They play a crucial role in various biological processes.')]
Output: [{{"question": "What is a primary function of amino acids?", "options": ["Building blocks of proteins", "Main energy storage molecules", "Structural lipids", "Digestive enzymes"], "correct_option_index": 0, "explanation": "Amino acids are described as building blocks of proteins in the provided context.", "references": [{{"source":"cours.pdf","page":1}}]}}]

If the context does not contain enough information to answer the user question, return exactly:
{{"error": "insufficient_context"}}

Return only the JSON list that matches the schema above.
    """

    return prompt