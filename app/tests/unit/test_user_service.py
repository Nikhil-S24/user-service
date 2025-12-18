import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.user import Base
from app.services.user_service import UserService
from app.schemas.user import CreateUserRequest

DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)


def test_create_user_success(db):
    data = CreateUserRequest(
        name="Test User",
        email="test@example.com",
        primary_mobile="9876543210",
        secondary_mobile=None,
        aadhaar="123456789012",
        pan="ABCDE1234F",
        date_of_birth="2000-01-01",
        place_of_birth="Chennai",
        current_address="Current Address",
        permanent_address="Permanent Address",
        password="Strong123",
    )

    user = UserService.create_user(db, data)

    assert user.id is not None
    assert user.email == "test@example.com"
    assert user.password_hash != "Strong123"
