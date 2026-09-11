import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app.retrieval.chunking import chunk_text
from app.retrieval.embeddings import get_embedding

sample_text = """
Retrieval Augmented Generation improves answer quality.
Language models can use external knowledge.
""" * 100

chunks = chunk_text(sample_text)

print("Total Chunks:", len(chunks))

embedding = get_embedding(chunks[0])

print("Embedding Size:", len(embedding))