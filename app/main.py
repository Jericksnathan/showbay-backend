from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import engine, SessionLocal
from app.models import Base
from app.schemas import TaskCreate, TaskUpdate, TaskResponse
from app import crud
from app.external_api import fetch_external_summary

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Task Manager API is running"}


@app.post("/tasks", response_model=TaskResponse, status_code=201)
async def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    summary = await fetch_external_summary()
    return crud.create_task(db, task, summary)


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(
    task_id: UUID,
    db: Session = Depends(get_db)
):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task_api(
    task_id: UUID,
    task_update: TaskUpdate,
    db: Session = Depends(get_db)
):
    task = crud.update_task(db, task_id, task_update)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task_api(
    task_id: UUID,
    db: Session = Depends(get_db)
):
    task = crud.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
