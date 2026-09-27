import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from src.database.database import Base, engine
from src.models.task import Task
from src.models.user import User
from src.routes.auth import router as auth_router
from src.routes.tasks import router as task_router

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    description="REST API for Task Management Application",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY")
)

app.include_router(auth_router)
app.include_router(task_router)


@app.get("/")
def home():
    return {
        "message": "Task Management API is running"
    }