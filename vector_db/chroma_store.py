import chromadb

client = chromadb.PersistentClient(path="./vector_db/chroma_store")
collection = client.get_or_create_collection("docs")

def add_doc(id, text, metadata):
    collection.add(
        ids=[id],
        documents=[text],
        metadatas=[metadata]
    )

def search(query):
    return collection.query(query_texts=[query], n_results=3)