from app.services.reddit_adapter import reddit_api

def fetch_reddit(query: str):
    return reddit_api(query)