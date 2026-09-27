from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.task import Task


class TaskRepository:

    def create_task(
        self,
        db: Session,
        task: Task
    ):
        db.add(task)
        db.commit()
        db.refresh(task)

        return task

    def get_tasks(
        self,
        db: Session,
        user_id: int
    ):
        statement = select(Task).where(
            Task.user_id == user_id
        )

        return db.scalars(statement).all()

    def get_task_by_id(
        self,
        db: Session,
        task_id: int,
        user_id: int
    ):
        statement = select(Task).where(
            Task.id == task_id,
            Task.user_id == user_id
        )

        return db.scalar(statement)

    def update_task(
        self,
        db: Session,
        task: Task
    ):
        db.commit()
        db.refresh(task)

        return task

    def delete_task(
        self,
        db: Session,
        task: Task
    ):
        db.delete(task)
        db.commit()

    def complete_task(
        self,
        db: Session,
        task: Task
    ):
        task.completed = True

        db.commit()
        db.refresh(task)

        return task