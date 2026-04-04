from langchain.tools import tool
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os

VECTOR_DB_PATH = "vector_db"

_vector_store = None
_embeddings = None


def get_embeddings():
    """Lazy load embeddings to avoid startup crash"""
    global _embeddings

    if _embeddings is None:
        _embeddings = OpenAIEmbeddings(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    return _embeddings


def get_vector_store():
    """Lazy load FAISS vector DB"""
    global _vector_store

    if _vector_store is None:
        _vector_store = FAISS.load_local(
            VECTOR_DB_PATH,
            get_embeddings(),
            allow_dangerous_deserialization=True
        )

    return _vector_store


@tool
def rag_tool(query: str):
    """
    Performs RAG (Retrieval Augmented Generation) over FAISS vector database
    and returns relevant documents.
    """

    vector_store = get_vector_store()

    # Step 1: similarity search
    docs = vector_store.similarity_search(query, k=3)

    # Step 2: format results
    results = [
        {
            "content": doc.page_content,
            "metadata": doc.metadata
        }
        for doc in docs
    ]

    # Step 3: return structured response
    return {
        "query": query,
        "results": results,
        "source": "faiss_vector_db"
    }