from fastapi import APIRouter
from app.graph.orchestrator import run_graph, approve_graph, get_trace

router = APIRouter()

@router.post("/query")
def query(payload: dict):
    return run_graph(payload["query"])

@router.post("/approve")
def approve(payload: dict):
    return approve_graph(payload["session_id"])

@router.get("/trace/{session_id}")
def trace(session_id: str):
    return get_trace(session_id)