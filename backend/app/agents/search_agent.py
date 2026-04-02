from app.tools.search_tool import search_web

def search_agent(state):
    results = search_web(state["query"])
    state["search_results"] = results
    state["trace"].append({"step": "search", "results": len(results)})
    return state