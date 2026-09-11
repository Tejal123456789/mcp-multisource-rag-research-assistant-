def choose_source(question: str) -> str:

    question = question.lower()

    github_keywords = [
        "github",
        "notes",
        "self-rag",
        "benefits"
    ]

    for keyword in github_keywords:

        if keyword in question:

            return "github"

    return "pdf"