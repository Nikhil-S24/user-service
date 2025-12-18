from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import require_admin
from app.core.database import get_db
from app.schemas.user import (
    CreateUserRequest,
    UpdateUserRequest,
    UserResponse,
    PaginatedUserResponse,
)
from app.services.user_service import (
    UserService,
    UserNotFoundError,
    UserAlreadyExistsError,
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_admin)],
)
def create_user(
    request: CreateUserRequest,
    db: Session = Depends(get_db),
):
    try:
        user = UserService.create_user(db, request)
        return user

    except UserAlreadyExistsError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        )


@router.patch(
    "/{user_id}",
    response_model=UserResponse,
    dependencies=[Depends(require_admin)],
)
def update_user(
    user_id: int,
    request: UpdateUserRequest,
    db: Session = Depends(get_db),
):
    try:
        user = UserService.update_user(db, user_id, request)
        return user

    except UserNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )


@router.get(
    "",
    response_model=PaginatedUserResponse,
    dependencies=[Depends(require_admin)],
)
def get_users(
    page: int = 0,
    size: int = 10,
    db: Session = Depends(get_db),
):
    users, total = UserService.get_users(db, page, size)

    return PaginatedUserResponse(
        items=users,
        total=total,
        page=page,
        size=size,
    )
