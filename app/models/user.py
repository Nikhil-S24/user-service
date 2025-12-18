from sqlalchemy import (
    Column,
    String,
    Date,
    DateTime,
    Boolean,
    Enum,
    func,
    Index,
)
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)

    name = Column(String(255), nullable=False)

    email = Column(String(255), nullable=False, unique=True, index=True)

    primary_mobile = Column(String(15), nullable=False)

    secondary_mobile = Column(String(15), nullable=True)

    aadhaar = Column(String(12), nullable=False, unique=True)

    pan = Column(String(10), nullable=False, unique=True)

    date_of_birth = Column(Date, nullable=False)

    place_of_birth = Column(String(255), nullable=False)

    current_address = Column(String(512), nullable=False)

    permanent_address = Column(String(512), nullable=False)

    password_hash = Column(String(255), nullable=False)

    role = Column(
        Enum("ADMIN", "USER", name="user_role"),
        nullable=False,
        default="USER",
    )

    is_deleted = Column(Boolean, nullable=False, default=False)

    deleted_at = Column(DateTime, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    __table_args__ = (
        Index("idx_users_active", "is_deleted"),
    )
