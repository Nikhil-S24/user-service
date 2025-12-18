from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, Field


# -------------------------------------------------------------------
# Create User Schema
# -------------------------------------------------------------------

class CreateUserRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    email: EmailStr
    primary_mobile: str = Field(..., min_length=10, max_length=15)
    secondary_mobile: Optional[str] = Field(None, min_length=10, max_length=15)

    aadhaar: str = Field(..., min_length=12, max_length=12)
    pan: str = Field(..., min_length=10, max_length=10)

    date_of_birth: date
    place_of_birth: str = Field(..., max_length=255)

    current_address: str = Field(..., max_length=512)
    permanent_address: str = Field(..., max_length=512)

    password: str = Field(..., min_length=8)


# -------------------------------------------------------------------
# Update User Schema (PATCH)
# -------------------------------------------------------------------

class UpdateUserRequest(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    primary_mobile: Optional[str] = Field(None, min_length=10, max_length=15)
    secondary_mobile: Optional[str] = Field(None, min_length=10, max_length=15)

    place_of_birth: Optional[str] = Field(None, max_length=255)
    current_address: Optional[str] = Field(None, max_length=512)
    permanent_address: Optional[str] = Field(None, max_length=512)


# -------------------------------------------------------------------
# User Response Schema
# -------------------------------------------------------------------

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    primary_mobile: str
    secondary_mobile: Optional[str]

    aadhaar: str
    pan: str

    date_of_birth: date
    place_of_birth: str

    current_address: str
    permanent_address: str

    role: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# -------------------------------------------------------------------
# Paginated Response Schema
# -------------------------------------------------------------------

class PaginatedUserResponse(BaseModel):
    items: List[UserResponse]
    total: int
    page: int
    size: int
