def run(state):
    if not state.get("approved", False):
        state["trace"].append("Waiting for human approval")
        return state

    state["trace"].append("Human approved output")
    return state