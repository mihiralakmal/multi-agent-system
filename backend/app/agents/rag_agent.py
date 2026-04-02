from app.tools.retrieval_tool import retrieve_docs

def rag_planner(state):
    state["trace"].append({"step": "planner", "action": "decide retrieval"})
    return state


def rag_executor(state):
    docs = retrieve_docs(state["query"])
    state["retrieved_docs"] = docs
    state["trace"].append({"step": "retrieval", "docs": len(docs)})
    return state