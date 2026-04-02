import os
def get_llm():
    return os.getenv("LLM_MODEL", "mock-llm")