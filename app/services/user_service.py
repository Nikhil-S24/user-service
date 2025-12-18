from typing import List, Tuple

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserNotFoundError(Exception):
    pass


class UserAlreadyExistsError(Exception):
    pass


class UserService:
    @staticmethod
    def create_user(db: Session, data) -> User:
        """
        Create a new user with hashed password.
        """
        try:
            user = User(
                name=data.name,
                email=data.email,
                primary_mobile=data.primary_mobile,
                secondary_mobile=data.secondary_mobile,
                aadhaar=data.aadhaar,
                pan=data.pan,
                date_of_birth=data.date_of_birth,
                place_of_birth=data.place_of_birth,
                current_address=data.current_address,
                permanent_address=data.permanent_address,
                password_hash=hash_password(data.password),
                role="USER",
            )

            return UserRepository.create(db, user)

        except IntegrityError:
            db.rollback()
            raise UserAlreadyExistsError(
                "User with given email, Aadhaar, or PAN already exists"
            )

    @staticmethod
    def update_user(
        db: Session,
        user_id: int,
        data,
    ) -> User:
        """
        Update mutable fields of a user.
        """
        user = UserRepository.get_by_id(db, user_id)
        if not user:
            raise UserNotFoundError("User not found")

        # Update only provided fields (PATCH semantics)
        for field, value in data.dict(exclude_unset=True).items():
            setattr(user, field, value)

        return UserRepository.update(db, user)

    @staticmethod
    def get_users(
        db: Session,
        page: int,
        size: int,
    ) -> Tuple[List[User], int]:
        return UserRepository.get_paginated(db, page, size)
