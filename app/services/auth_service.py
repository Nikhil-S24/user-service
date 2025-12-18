from sqlalchemy.orm import Session

from app.core.security import verify_password, create_access_token
from app.models.user import User


class AuthenticationError(Exception):
    """Raised when authentication fails."""
    pass


class AuthService:
    @staticmethod
    def login(db: Session, email: str, password: str) -> str:
        """
        Authenticate a user using email and password.
        Returns JWT access token if successful.
        """
        user = (
            db.query(User)
            .filter(User.email == email, User.is_deleted == False)
            .first()
        )

        if not user:
            raise AuthenticationError("Invalid email or password")

        if not verify_password(password, user.password_hash):
            raise AuthenticationError("Invalid email or password")

        token = create_access_token(
            subject=user.email,
            role=user.role
        )

        return token
