from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.schemas.user import UserCreate, UserLogin, UserResponse
from src.services.auth_service import login_user, register_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    return register_user(
        db,
        user_data
    )


@router.post(
    "/login",
    response_model=UserResponse
)
def login(
    user_data: UserLogin,
    request: Request,
    db: Session = Depends(get_db)
):
    user = login_user(
        db,
        user_data
    )

    request.session["user_id"] = user.id

    return user


@router.post("/logout")
def logout(request: Request):

    request.session.clear()

    return {
        "message": "Logged out successfully"
    }