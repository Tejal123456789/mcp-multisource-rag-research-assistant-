import ollama

def generate_answer(context: str, question: str) -> str:

    prompt = f"""
    You are a helpful research assistant.

    Context:
    {context}

    Question:
    {question}

    Answer the question using only the provided context.
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

    return response["message"]["content"]

def compare_documents(
    document_1: str,
    document_2: str
) -> str:

    prompt = f"""
    Compare the following two research papers.

    Paper 1:
    {document_1}

    Paper 2:
    {document_2}

    Provide:

    1. Main topic of paper 1
    2. Main topic of paper 2
    3. Similarities
    4. Differences
    5. Overall summary
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

    return response["message"]["content"]