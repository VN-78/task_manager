from fastapi import FastAPI

from src.task_manager.api import v1_router


def create_app() -> FastAPI:

    app = FastAPI(title="Task_manager", version="0.0.1", description="task manager app")

    # Attach the api v1
    app.include_router(v1_router, prefix="/api/v1")

    return app


app = create_app()

@app.get("/")
def health():
    return {"Working"}
