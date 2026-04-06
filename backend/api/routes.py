from fastapi import APIRouter, HTTPException
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


# @router.post("/approve")
# def approve():
#     state = SESSION_STATE.get("latest")
#     state["approved"] = True
#
#     result = graph_app.invoke(state)
#     return result

@router.post("/approve")
def approve():
    """
    Human-in-the-loop approval endpoint.
    Retrieves stored state, marks as approved,
    and resumes LangGraph execution.
    """

    # 1. Get previous state
    state = SESSION_STATE.get("latest")

    if not state:
        raise HTTPException(status_code=400, detail="No pending workflow found")

    # 2. Update approval flag
    state["approved"] = True
    state["trace"].append("Human approved the draft")

    # 3. Re-run graph (continues from checkpoint)
    result = graph_app.invoke(state)

    # 4. Store updated state
    SESSION_STATE["latest"] = result

    # 5. Return final response
    return {
        "message": "Approved and execution completed",
        "final": result.get("final"),
        "trace": result.get("trace")
    }


@router.get("/trace")
def trace():
    return SESSION_STATE.get("latest", {}).get("trace", [])