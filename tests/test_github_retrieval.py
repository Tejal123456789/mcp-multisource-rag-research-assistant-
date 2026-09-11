import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app.retrieval.retriever import retrieve

query = "How can we improve a RAG pipeline?"

results = retrieve(query)

for idx, result in enumerate(results, start=1):
    print(f"\nResult {idx}:\n")
    print(result)