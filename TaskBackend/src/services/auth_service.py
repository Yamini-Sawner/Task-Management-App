from fastapi import HTTPException, status
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from src.models.user import User
from src.repositories.user_repository import UserRepository
from src.schemas.user import UserCreate, UserLogin

password_hash = PasswordHash.recommended()

user_repository = UserRepository()


def register_user(
    db: Session,
    user_data: UserCreate
):
    existing_user = user_repository.get_user_by_email(
        db,
        user_data.email
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hashed_password = password_hash.hash(
        user_data.password
    )

    user = User(
        name=user_data.name,
        email=user_data.email,
        password=hashed_password
    )

    return user_repository.create_user(
        db,
        user
    )


def login_user(
    db: Session,
    user_data: UserLogin
):
    user = user_repository.get_user_by_email(
        db,
        user_data.email
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not password_hash.verify(
        user_data.password,
        user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    return user