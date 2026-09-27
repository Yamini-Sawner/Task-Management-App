from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.models.task import Task
from src.repositories.task_repository import TaskRepository
from src.schemas.task import TaskCreate, TaskUpdate

task_repository = TaskRepository()


def create_task(
    db: Session,
    user_id: int,
    task_data: TaskCreate
):
    task = Task(
        title=task_data.title,
        description=task_data.description,
        user_id=user_id
    )

    return task_repository.create_task(
        db,
        task
    )


def get_tasks(
    db: Session,
    user_id: int
):
    return task_repository.get_tasks(
        db,
        user_id
    )


def get_task(
    db: Session,
    task_id: int,
    user_id: int
):
    task = task_repository.get_task_by_id(
        db,
        task_id,
        user_id
    )

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


def update_task(
    db: Session,
    task_id: int,
    user_id: int,
    task_data: TaskUpdate
):
    task = get_task(
        db,
        task_id,
        user_id
    )

    if task_data.title is not None:
        task.title = task_data.title

    if task_data.description is not None:
        task.description = task_data.description

    return task_repository.update_task(
        db,
        task
    )


def delete_task(
    db: Session,
    task_id: int,
    user_id: int
):
    task = get_task(
        db,
        task_id,
        user_id
    )

    task_repository.delete_task(
        db,
        task
    )


def complete_task(
    db: Session,
    task_id: int,
    user_id: int
):
    task = get_task(
        db,
        task_id,
        user_id
    )

    return task_repository.complete_task(
        db,
        task
    )