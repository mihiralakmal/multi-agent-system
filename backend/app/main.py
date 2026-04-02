from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Multi-Agent AI System")

app.include_router(router)