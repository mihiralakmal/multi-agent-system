from langgraph.graph import StateGraph
from backend.graph.state import GraphState

from backend.graph.nodes.planner import run as planner
from backend.graph.nodes.executor import run as executor
from backend.graph.nodes.verifier import run as verifier
from backend.graph.nodes.human_checkpoint import run as human

workflow = StateGraph(GraphState)

workflow.add_node("planner", planner)
workflow.add_node("executor", executor)
workflow.add_node("verifier", verifier)
workflow.add_node("human", human)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "executor")
workflow.add_edge("executor", "verifier")
workflow.add_edge("verifier", "human")

app = workflow.compile()