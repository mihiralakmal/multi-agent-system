from app.tools.reddit_tool import fetch_reddit

def reddit_agent(state):
    results = fetch_reddit(state["query"])
    state["reddit_results"] = results
    state["trace"].append({"step": "reddit", "results": len(results)})
    return state