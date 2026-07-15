from studycopilot.retrieval.schema import RetrievedChunk


def build_mcq_prompt(
    user_question: str,
    context: list[RetrievedChunk],
    nb_questions: int = 1,
) -> str:
    """
    Build a prompt for generating MCQs from retrieved RAG context.
    """


    formatted_context = "\n\n".join(
        [
            f"""
--- CONTEXT CHUNK {i+1} ---
Relevance score: {chunk.score}
Source: {chunk.source}
Page: {chunk.page}

Content:
{chunk.text}
"""
            for i, chunk in enumerate(context)
        ]
    )


    prompt = f"""
ROLE:
You are an expert science teacher creating high-quality exam-style
multiple-choice questions for students.


TASK:
Generate {nb_questions} MCQ(s) ONLY about the requested topic.


========================
REQUESTED TOPIC
========================

{user_question}


========================
CONTEXT USAGE RULES
========================

You are provided with retrieved document chunks.

IMPORTANT:
- The chunks are ranked by relevance score.
- The first chunks are usually more relevant than later chunks.
- Some chunks may be partially or completely unrelated to the requested topic.
- The requested topic may correspond to a chapter title, section title, or concept name. Prefer chunks containing this exact terminology.

You MUST:
- Use ONLY information from chunks directly related to the requested topic.
- Ignore unrelated chunks.
- Never create questions from another chapter, section, or subject.
- Never combine unrelated concepts to create a question.
- Never use external knowledge.


========================
QUESTION QUALITY RULES
========================

Each generated question must:

- Directly test knowledge about the requested topic.
- Not be about titles or headings.
- Be answerable using ONLY the selected context.
- Have one and only one correct answer.
- Be suitable for exam revision.
- Avoid vague questions.
- Avoid questions requiring information not present in the context.


Before generating each question, internally verify:

1. Is this question about the requested topic (not the title or header)?
2. Can the answer be found explicitly in the context?
3. Am I using only relevant chunks?


If any answer is NO, discard the question and generate another one.


========================
OUTPUT REQUIREMENTS
========================

Return ONLY valid JSON.

No markdown.
No explanation outside JSON.


Return exactly {nb_questions} objects.


Each object must contain:

- question: string
- options: exactly 4 strings
- correct_option_index: integer from 0 to 3
- explanation: maximum 30 words
- references: list containing source and page


JSON schema:

[
  {{
    "question": "...",
    "options": [
      "...",
      "...",
      "...",
      "..."
    ],
    "correct_option_index": 0,
    "explanation": "...",
    "references": [
      {{
        "source": "filename.pdf",
        "page": 1
      }}
    ]
  }}
]


========================
RETRIEVED CONTEXT
========================

{formatted_context}


========================
FINAL CHECK
========================

Before returning the JSON:

- Verify every question relates to:
"{user_question}"

- Remove any question related to another topic.

- If the context is insufficient, return:

{{
    "error": "insufficient_context"
}}

Return only JSON.
"""

    return prompt