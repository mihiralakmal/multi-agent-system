from typing import TypedDict, List, Dict, Any

class GraphState(TypedDict):
    query: str
    plan: str
    tool_results: List[Dict[str, Any]]
    draft: str
    final: str
    approved: bool
    trace: List[str]