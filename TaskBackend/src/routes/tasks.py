from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.middleware.auth import get_current_user
from src.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from src.services.task_service import (
    complete_task,
    create_task,
    delete_task,
    get_task,
    get_tasks,
    update_task
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post(
    "",
    response_model=TaskResponse
)
def create(
    task_data: TaskCreate,
    request: Request,
    db: Session = Depends(get_db)
):
    user_id = get_current_user(request)

    return create_task(
        db,
        user_id,
        task_data
    )


@router.get(
    "",
    response_model=list[TaskResponse]
)
def get_all(
    request: Request,
    db: Session = Depends(get_db)
):
    user_id = get_current_user(request)

    return get_tasks(
        db,
        user_id
    )


@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
def get_one(
    task_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    user_id = get_current_user(request)

    return get_task(
        db,
        task_id,
        user_id
    )


@router.put(
    "/{task_id}",
    response_model=TaskResponse
)
def update(
    task_id: int,
    task_data: TaskUpdate,
    request: Request,
    db: Session = Depends(get_db)
):
    user_id = get_current_user(request)

    return update_task(
        db,
        task_id,
        user_id,
        task_data
    )


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    task_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    user_id = get_current_user(request)

    delete_task(
        db,
        task_id,
        user_id
    )


@router.patch(
    "/{task_id}/complete",
    response_model=TaskResponse
)
def complete(
    task_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    user_id = get_current_user(request)

    return complete_task(
        db,
        task_id,
        user_id
    )