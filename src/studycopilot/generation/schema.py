from dataclasses import dataclass


@dataclass
class MCQQuestion:

    question: str

    options: list[str]

    correct_answer_index: int

    explanation: str

@dataclass
class Quiz:

    questions: list[MCQQuestion]