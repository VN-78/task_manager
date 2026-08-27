from fastapi import APIRouter

from src.task_manager.api.v1 import router as task_router

v1_router = APIRouter()
v1_router.include_router(task_router, prefix="/tasks", tags=["Tasks"])
