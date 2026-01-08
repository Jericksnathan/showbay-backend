from sqlalchemy.orm import Session
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate
from uuid import UUID


def create_task(db: Session, task: TaskCreate, summary: str):
    db_task = Task(
        title=task.title,
        description=task.description,
        external_summary=summary
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_task(db: Session, task_id: UUID):
    return db.query(Task).filter(Task.id == task_id).first()


def update_task(db: Session, task_id: UUID, task_update: TaskUpdate):
    db_task = get_task(db, task_id)
    if not db_task:
        return None

    if task_update.title is not None:
        db_task.title = task_update.title
    if task_update.description is not None:
        db_task.description = task_update.description

    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: UUID):
    db_task = get_task(db, task_id)
    if not db_task:
        return None

    db.delete(db_task)
    db.commit()
    return db_task
