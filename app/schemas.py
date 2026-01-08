from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str
    external_summary: Optional[str]

    class Config:
        from_attributes = True  # Pydantic v2
