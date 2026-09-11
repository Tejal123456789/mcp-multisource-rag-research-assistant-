import os

from app.retrieval.chunking import chunk_text
from app.retrieval.embeddings import get_embedding
from app.retrieval.vector_store import collection


def ingest_repository():

    repo_path = "data/github_repos/graphrag"

    chunk_id = 200000

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if not file.endswith(".md"):
                continue

            file_path = os.path.join(
                root,
                file
            )

            print(f"Processing: {file_path}")

            try:

                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    text = f.read()

                chunks = chunk_text(text)

                for chunk in chunks:

                    embedding = get_embedding(chunk)

                    collection.add(
                        ids=[
                            f"repo_chunk_{chunk_id}"
                        ],
                        documents=[chunk],
                        embeddings=[embedding],
                        metadatas=[
                            {
                                "source": "github_repo",
                                "repo": "graphrag",
                                "file": file
                            }
                        ]
                    )

                    chunk_id += 1

            except Exception as e:

                print(
                    f"Skipped {file}: {e}"
                )

    print(
        "Repository ingestion completed."
    )