def choose_task(question: str):

    question = question.lower()

    if "compare" in question:
        return "compare"

    return "ask"
