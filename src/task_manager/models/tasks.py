from typing import Literal

from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    priority_weight: int
    due_hours_left: float
    status: Literal["PENDING", "BLOCKED", "COMPLETED"]
    depends_on_id: int
