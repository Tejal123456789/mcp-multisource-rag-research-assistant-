import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from app.retrieval.pdf_retriever import retrieve_pdf

results = retrieve_pdf(
    query="What is Retrieval Augmented Generation?",
    pdf_name="paper7.pdf"
)

for idx, result in enumerate(results, start=1):

    print(f"\nResult {idx}:\n")
    print(result)
