# 🧠 StudyCopilot
## AI-powered Quiz Generator and Learning Assistant

## Overview

StudyCopilot is an AI learning assistant that transforms educational documents into personalized quizzes.

Users can upload documents (PDF, Word, Markdown), and the system automatically:

- extracts the content
- understands the document structure
- generates high-quality multiple-choice questions
- provides explanations for answers
- creates personalized revision sessions


The goal is to explore how Large Language Models can enhance learning through Retrieval-Augmented Generation (RAG), embeddings and AI agents.

---
## Installation

git clone https://github.com/username/study-copilot

cd study-copilot

uv sync

---

### 🚧 This project is a work in progress : roadmap

## Retrieval
- [ ] Tune chunk size and overlap
- [ ] Add metadata-based filtering (document, page, chapter)
- [ ] Implement Parent-Child Retrieval
- [ ] Explore Hybrid Search (semantic + keyword/BM25)
- [ ] Add retrieval reranking

## Generation
- [ ] Improve prompt engineering for topic-focused question generation
- [ ] Add support for multiple LLM providers (Ollama, OpenAI, Azure OpenAI, Anthropic)
- [ ] Generate adaptive quizzes based on difficulty level
- [ ] Generate flashcards in addition to MCQs

## Evaluation
- [ ] Build an evaluation dataset with expected retrieval results
- [ ] Measure retrieval quality (Recall@K, MRR, Precision@K)
- [ ] Evaluate generation quality (faithfulness, relevance, JSON validity)
- [ ] Compare prompts and embedding models with MLflow
- [ ] Integrate Ragas for automatic RAG evaluation

## Observability
- [ ] Integrate Langfuse for prompt tracing and monitoring
- [ ] Track latency and embedding generation time
- [ ] Track LLM token usage and inference cost

## Engineering
- [ ] Add unit and integration tests
- [ ] Improve project configuration and logging
- [ ] Add CI with GitHub Actions
- [ ] Containerize the application with Docker