from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.user import User


class UserRepository:

    def create_user(
        self,
        db: Session,
        user: User
    ):
        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    def get_user_by_email(
        self,
        db: Session,
        email: str
    ):
        statement = select(User).where(
            User.email == email
        )

        return db.scalar(statement)

    def get_user_by_id(
        self,
        db: Session,
        user_id: int
    ):
        statement = select(User).where(
            User.id == user_id
        )

        return db.scalar(statement)