from app.services.search_adapter import search_api

def search_web(query: str):
    return search_api(query)