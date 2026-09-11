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

from app.retrieval.repo_retriever import retrieve_repo

results = retrieve_repo(
    "What is GraphRAG?"
)

for idx, result in enumerate(results, start=1):

    print(f"\nResult {idx}:\n")
    print(result)