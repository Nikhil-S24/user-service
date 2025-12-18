from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.core.security import decode_access_token

security = HTTPBearer()


def get_current_user_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> dict:
    """
    Validate JWT token and return decoded payload.
    """
    token = credentials.credentials

    try:
        payload = decode_access_token(token)
        return payload
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )


def require_admin(
    payload: dict = Depends(get_current_user_token),
):
    """
    Ensure the current user has ADMIN role.
    """
    if payload.get("role") != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required",
        )
