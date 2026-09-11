from retrieval.embeddings import get_embedding
from retrieval.vector_store import collection


def retrieve_repo(
    query: str,
    n_results: int = 3
):

    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        where={
            "source": "github_repo"
        }
    )

    return results["documents"][0]