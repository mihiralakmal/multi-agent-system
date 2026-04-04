from fastapi import APIRouter
from backend.api.schema import QueryRequest
from backend.graph.workflow import app as graph_app


router = APIRouter()

SESSION_STATE = {}

@router.post("/query")
def query(req: QueryRequest):
    state = {
        "query": req.query,
        "trace": [],
        "tool_results": [],
        "approved": False
    }

    result = graph_app.invoke(state)

    SESSION_STATE["latest"] = result

    return result


@router.post("/approve")
def approve():
    state = SESSION_STATE.get("latest")
    state["approved"] = True

    result = graph_app.invoke(state)
    return result


@router.get("/trace")
def trace():
    return SESSION_STATE.get("latest", {}).get("trace", [])