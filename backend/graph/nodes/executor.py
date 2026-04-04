from backend.tools import ALL_TOOLS

def run(state):
    query = state["query"]
    results = []

    for tool in ALL_TOOLS:
        result = tool.invoke(query)
        results.append({
            "tool": tool.name,
            "output": result
        })

    state["tool_results"] = results
    state["draft"] = "Combined answer generated from tools"
    state["trace"].append("Executor used LangChain tools")

    return state