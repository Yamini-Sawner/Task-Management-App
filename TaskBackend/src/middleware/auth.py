from fastapi import HTTPException, Request, status


def get_current_user(request: Request):

    user_id = request.session.get("user_id")

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please login first"
        )

    return user_id