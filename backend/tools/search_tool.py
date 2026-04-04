from langchain.tools import tool
from duckduckgo_search import DDGS

@tool
def search_tool(query: str):
    """
    Performs web search using DuckDuckGo and returns top results.
    """

    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append({
                "title": r.get("title"),
                "url": r.get("href"),
                "summary": r.get("body")
            })

    return {
        "query": query,
        "results": results
    }