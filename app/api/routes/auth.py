from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import AuthService, AuthenticationError
from app.core.database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=TokenResponse)
def login(
    login_request: LoginRequest,
    db: Session = Depends(get_db),
):
    try:
        token = AuthService.login(
            db=db,
            email=login_request.email,
            password=login_request.password,
        )
        return TokenResponse(access_token=token)

    except AuthenticationError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        )
