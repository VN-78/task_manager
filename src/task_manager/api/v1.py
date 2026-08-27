from fastapi import APIRouter

router = APIRouter()

@router.post("/")
def add_new_task():
    pass

@router.get("/")
def fetch_all_tasks():
    pass

@router.put(f"/{id}")
def update_task():
    pass

@router.delete(f"/{id}")
def delete_task():
    pass