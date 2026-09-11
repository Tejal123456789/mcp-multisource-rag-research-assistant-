import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app.retrieval.embeddings import get_embedding
from app.retrieval.vector_store import collection

query = "How can language models use external knowledge?"

query_embedding = get_embedding(query)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

print(results["documents"])