from typing import List, Optional, Tuple

from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    @staticmethod
    def get_by_email(db: Session, email: str) -> Optional[User]:
        return (
            db.query(User)
            .filter(User.email == email, User.is_deleted == False)
            .first()
        )

    @staticmethod
    def get_by_id(db: Session, user_id: int) -> Optional[User]:
        return (
            db.query(User)
            .filter(User.id == user_id, User.is_deleted == False)
            .first()
        )

    @staticmethod
    def create(db: Session, user: User) -> User:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def update(db: Session, user: User) -> User:
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_paginated(
        db: Session,
        page: int,
        size: int,
    ) -> Tuple[List[User], int]:
        query = db.query(User).filter(User.is_deleted == False)

        total = query.count()

        users = (
            query
            .offset(page * size)
            .limit(size)
            .all()
        )

        return users, total
