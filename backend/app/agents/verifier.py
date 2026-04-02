def verify_answer(state):
    context = state["retrieved_docs"] + state["search_results"] + state["reddit_results"]

    answer = f"""
Based on combined sources:

Docs: {len(state['retrieved_docs'])}
Web: {len(state['search_results'])}
Reddit: {len(state['reddit_results'])}

Answer synthesis:
{state['query']} is addressed using hybrid RAG + search + Reddit signals.
"""

    state["draft_answer"] = answer
    state["trace"].append({"step": "verifier", "status": "draft_created"})
    return state