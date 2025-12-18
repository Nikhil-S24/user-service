from pydantic import BaseModel, EmailStr, Field


class LoginRequest(BaseModel):
    """
    Request body for login API.
    """
    email: EmailStr = Field(..., example="user@example.com")
    password: str = Field(..., min_length=8, example="StrongPassword123")


class TokenResponse(BaseModel):
    """
    Response body containing JWT access token.
    """
    access_token: str
    token_type: str = "bearer"
