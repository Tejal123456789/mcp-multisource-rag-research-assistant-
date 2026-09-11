import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app.retrieval.chunking import chunk_text
from app.retrieval.embeddings import get_embedding
from app.retrieval.vector_store import collection

sample_text = """
Retrieval Augmented Generation improves answer quality.
Language models can use external knowledge.
""" * 100

chunks = chunk_text(sample_text)

for i, chunk in enumerate(chunks):

    embedding = get_embedding(chunk)

    collection.add(
        ids=[f"chunk_{i}"],
        documents=[chunk],
        embeddings=[embedding]
    )

print("Chunks stored:", len(chunks))