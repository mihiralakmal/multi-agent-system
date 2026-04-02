import uuid
from app.graph.state import GraphState
from app.agents.rag_agent import rag_planner, rag_executor
from app.agents.search_agent import search_agent
from app.agents.reddit_agent import reddit_agent
from app.agents.verifier import verify_answer

# simple in-memory store (replace with Redis/DB in real system)
STATE_DB = {}

def run_graph(query: str):
    session_id = str(uuid.uuid4())

    state: GraphState = {
        "query": query,
        "session_id": session_id,
        "retrieved_docs": [],
        "search_results": [],
        "reddit_results": [],
        "draft_answer": None,
        "final_answer": None,
        "requires_approval": False,
        "approved": False,
        "trace": []
    }

    # 1. Planner
    state = rag_planner(state)

    # 2. Retrieval (RAG tool)
    state = rag_executor(state)

    # 3. Optional tools
    state = search_agent(state)
    state = reddit_agent(state)

    # 4. Draft generation
    state = verify_answer(state)
    state["requires_approval"] = True

    STATE_DB[session_id] = state

    return {
        "session_id": session_id,
        "draft": state["draft_answer"],
        "trace": state["trace"],
        "requires_approval": True
    }


def approve_graph(session_id: str):
    state = STATE_DB.get(session_id)

    if not state:
        return {"error": "invalid session"}

    state["approved"] = True
    state["requires_approval"] = False

    state["final_answer"] = state["draft_answer"]

    return {
        "final_answer": state["final_answer"]
    }


def get_trace(session_id: str):
    return STATE_DB.get(session_id, {}).get("trace", [])