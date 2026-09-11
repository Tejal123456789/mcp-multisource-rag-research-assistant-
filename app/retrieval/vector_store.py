import chromadb

client = chromadb.PersistentClient(
    path="vector_store/chromadb"
)

collection = client.get_or_create_collection(
    name="research_papers"
)

print("Collection created:", collection.name)