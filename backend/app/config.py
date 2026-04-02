import os

class Config:
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

    VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./vector_db")

    REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", "")
    REDDIT_SECRET = os.getenv("REDDIT_SECRET", "")

    SEARCH_API_KEY = os.getenv("SEARCH_API_KEY", "")