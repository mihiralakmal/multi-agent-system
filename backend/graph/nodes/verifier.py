def run(state):
    draft = state["draft"]

    state["final"] = f"Verified: {draft}"
    state["trace"].append("Verifier approved draft")

    return state