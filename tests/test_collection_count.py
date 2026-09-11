import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from app.retrieval.vector_store import collection

results = collection.get()

print("Total documents:", len(results["documents"]))
print("Total metadata:", len(results["metadatas"]))

for meta in results["metadatas"][-10:]:
    print(meta)