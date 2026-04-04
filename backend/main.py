from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="Multi-Agent System")

app.include_router(router)