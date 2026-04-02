## Design Explanation ##

## Orchestration Decisions
The system uses LangGraph to implement a state-machine-based orchestration that ensures clear and deterministic 
execution rather than relying on simple linear chains. The workflow is structured into Planner, Executor, Verifier, 
and Human Checkpoint nodes. The Planner interprets the user query and defines the execution plan, 
while the Executor handles tool calling, including hybrid RAG retrieval, internet search, and Reddit intelligence. 
The Verifier refines and validates the draft response to maintain quality. Before generating the final output, 
the Human Checkpoint pauses execution and requires explicit user approval. This approach provides strong traceability, 
controlled flow, and flexibility to extend the pipeline by adding or modifying nodes.

## Memory Design
The system incorporates both short-term and long-term memory to support efficient processing. Short-term memory is 
maintained within the LangGraph state, storing the current query, execution plan, tool outputs, draft responses, 
and trace information, enabling context-aware reasoning within a session. Long-term memory is implemented using a 
persistent storage mechanism such as a file-based JSON store, which can be extended to databases like Redis or PostgreSQL. 
This separation ensures fast in-session operations while preserving historical data for future reference, learning, or 
auditing.

## Extensibility Considerations:
The architecture is designed to be modular and loosely coupled, allowing easy extension and scalability. 
All external functionalities, such as retrieval, search, and Reddit analysis, are implemented as independent tools, 
making it simple to integrate new tools without modifying the core orchestration logic. The system is model-agnostic, 
with LLMs and embedding models configurable via environment variables, enabling seamless switching between 
different providers. The retrieval layer is abstracted to support multiple vector databases like Chroma, Qdrant, 
or Weaviate. Additionally, the microservices separation between frontend and backend allows independent deployment and 
scaling, while the graph-based orchestration makes it easy to introduce new nodes or capabilities with minimal
impact on the existing system.
