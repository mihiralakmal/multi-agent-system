from typing import TypedDict, List, Optional, Dict

class GraphState(TypedDict):
    query: str
    session_id: str

    draft_answer: Optional[str]
    final_answer: Optional[str]

    retrieved_docs: List[dict]
    search_results: List[dict]
    reddit_results: List[dict]

    requires_approval: bool
    approved: bool

    trace: List[dict]