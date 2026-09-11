import ollama


def choose_source_llm(question: str) -> str:

    prompt = f"""
    You are a source routing assistant.

    Choose ONLY ONE source.

    Sources:

    pdf:
    - Research papers
    - Large Language Models
    - Semantic Search
    - RAG papers
    - Academic content

    github:
    - Personal notes
    - Self-RAG
    - Benefits of RAG
    - Personal documentation

    github_repo:
    - GraphRAG repository
    - GraphRAG architecture
    - GraphRAG indexing
    - Local search
    - Global search
    - Repository documentation

    Rules:

    If the question is about:
    - GraphRAG architecture
    - GraphRAG indexing
    - local search
    - global search

    Return:
    github_repo

    If the question is about:
    - benefits of RAG
    - Self-RAG
    - improving a RAG pipeline

    Return:
    github

    Otherwise return:
    pdf

    Return ONLY one word:

    pdf
    github
    github_repo

    Question:
    {question}
    """

    response = ollama.chat(
        model="phi4-mini:3.8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"].strip().lower()