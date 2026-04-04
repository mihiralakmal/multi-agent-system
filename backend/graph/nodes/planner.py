def run(state):
    query = state["query"]

    state["plan"] = f"""
    1. Use RAG for knowledge retrieval
    2. Use Search if needed
    3. Use Reddit insights
    4. Combine and generate draft
    """

    state["trace"].append("Planner created execution plan")
    return state