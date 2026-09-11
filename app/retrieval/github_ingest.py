import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from retrieval.chunking import chunk_text
from retrieval.embeddings import get_embedding
from retrieval.vector_store import collection


def ingest_github_notes():

    github_folder = "data/github"

    files = [
        file
        for file in os.listdir(github_folder)
        if file.endswith(".md")
    ]

    chunk_id = 100000

    for file_name in files:

        file_path = os.path.join(
            github_folder,
            file_name
        )

        print(f"Processing: {file_name}")

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            text = file.read()

        chunks = chunk_text(text)

        for chunk in chunks:

            embedding = get_embedding(chunk)

            collection.add(
                ids=[f"github_chunk_{chunk_id}"],
                documents=[chunk],
                embeddings=[embedding],
                metadatas=[
                    {
                        "source": "github",
                        "file": file_name
                    }
                ]
            )

            chunk_id += 1

    print("GitHub notes ingested successfully.")