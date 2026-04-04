# Multi-Agent AI System (LangGraph + RAG + Search + Reddit)

---

## Overview

This project demonstrates a **multi-agent AI system** built with a strong focus on **clean architecture and orchestration** using:

* 🔹 LangGraph state-machine orchestration
* 🔹 Hybrid RAG (Vector + Metadata filtering)
* 🔹 Internet Search Tool (API-based)
* 🔹 Linkedin Search 
* 🔹 Reddit Intelligence Agent
* 🔹 Human-in-the-loop approval checkpoint
* 🔹 Microservices architecture (Frontend ↔ Backend)

---

# Architecture Diagram

```
                                                      User
                                                       │
                                                Frontend (Flask)
                                                       │
                                                FastAPI Backend
                                                       │
                                            LangGraph Orchestrator
                                                       │
                                   ┌───────────────────┼───────────────────┐
                                   │                   │                   │
                                  Planner Node     Executor Node     Verifier Node
                                                       │
                                   ┌───────────────┬───────────────┬───────────────┐
                                   │               │               │               │
                               RAG Tool      Search Tool     Reddit Tool    LinkedIn Tool
                             (Vector + Meta)
                                                       │
                                              Human Checkpoint Node
                                                       │
                                                  Final Output
```

---

# Prerequisites

Make sure you have installed:

* Docker
* Docker Compose
* Python 3.10+ (for local run without Docker)

---

# Environment Setup

## 1. Clone Repository

```bash
git https://github.com/mihiralakmal/multi-agent-system.git
cd \Multi-Agent-AI
```

---

## 2. Create `.env` File

```bash
cp .env.example .env
```

Update values:

```
LLM_MODEL=gpt-4o-mini
EMBEDDING_MODEL=text-embedding-3-small

SEARCH_API_KEY=your_key
REDDIT_CLIENT_ID=your_id
REDDIT_SECRET=your_secret
LINKEDIN_ACCESS_TOKEN=your_token
OPEN_API_KEY=your-key
```

---

# Run with Docker (Recommended)

## Build and Start Services

```bash
docker-compose up --build
```

---

## Services

| Service  | URL                        |
| -------- | -------------------------- |
| Frontend | http://localhost:3000      |
| Backend  | http://localhost:8000      |
| Swagger  | http://localhost:8000/docs |

---

# API Usage (Swagger)

Open in browser:

```
http://localhost:8000/docs
```

You will see the following endpoints:

* `/query` → Submit user query
* `/approve` → Approve draft response
* `/trace` → View execution trace

---

## 1. Query API

**POST /query**

### Request

```json
{
  "query": "software engineer"
}
```

### Response

```json
{
  "draft": "Draft answer...",
  "trace": [
    "Planner created execution plan",
    "Executor used LangChain tools",
    "Verifier approved draft",
    "Waiting for human approval"
  ]
}
```

---

## 2. Approve API (Human-in-the-loop)

**POST /approve**

### Response

```json
{
  "final": "Verified: Combined answer generated from tools",
  "approved": true,
  "trace": [
    "Planner created execution plan",
    "Executor used LangChain tools",
    "Verifier approved draft",
    "Waiting for human approval",
    "Planner created execution plan",
    "Executor used LangChain tools",
    "Verifier approved draft",
    "Human approved output"
  ]
}
```

---

## 3. Trace API

**GET /trace**

Returns full execution state including:

* Planner created execution plan",
* Executor used LangChain tools",
* Verifier approved draft",
* Waiting for human approval",
* Planner created execution plan",
* Executor used LangChain tools",
* Verifier approved draft",
* Human approved output"


---

# Run Without Docker (Optional)

## ▶ Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## ▶ Frontend

```bash
cd frontend
pip install flask requests
python app.py
```

---

# Access the Application

## Backend (Swagger UI)

```
http://localhost:8000/docs
```

---

## Frontend UI

```
http://localhost:3000
```

Features:

* Enter query
* View draft response
* See tool execution trace
* Approve response
* View final answer

---

# Example Queries

* "Compare LangGraph vs LangChain"
* "Latest AI trends in 2026"
* "What do Reddit users think about OpenAI models?"
* "Explain RAG architecture with real-world use cases"

---

# Observability

The system provides:

* Execution trace per request
* Node-level visibility (Planner, Executor, Verifier)
* Tool usage transparency
* Debug-friendly responses

---

# Design Decisions

##  Orchestration

* Implemented using LangGraph state machine
* Explicit flow:
  **Planner → Executor → Verifier → Human → Final**
* No hidden agent loops

##  Memory

* Short-term → Graph state
* Long-term → File-based storage (extensible to DB)

##  Tools

* Fully decoupled adapters
* Easily replaceable APIs

##   Model Agnostic

* Controlled via `.env`
* Supports swapping:

  * OpenAI
  * Local LLMs
  * Other providers

---

# Future Improvements

* Real LLM-based planner (instead of mock)
* Streaming responses
* Redis / DB-backed memory
* Kubernetes deployment
* Observability (Prometheus + Grafana)
* Authentication & rate limiting

---

# Conclusion

This project demonstrates:

* Clean architecture
* True multi-agent orchestration
* Human-in-the-loop workflow
* Production-ready extensible design

---

