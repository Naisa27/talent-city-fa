import typing
from datetime import datetime

from sqlalchemy import String, DateTime, text, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import BaseTalentCity

if typing.TYPE_CHECKING:
    from src.models import RolesOrm


class UsersOrm(BaseTalentCity):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column(String(250))
    first_name: Mapped[str] = mapped_column(String(250))
    patronimic: Mapped[str | None] = mapped_column(String(250))
    city: Mapped[str | None] = mapped_column(String(250))
    email: Mapped[str] = mapped_column(String(250), unique=True)
    phone: Mapped[str] = mapped_column(String(15))
    hashed_password: Mapped[str] = mapped_column(String(250))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("NOW()"))
    isBlocked: Mapped[bool] = mapped_column(Boolean, server_default=text("FALSE"))
    blocked_at: Mapped[datetime | None] = mapped_column(DateTime)
    isActive: Mapped[bool] = mapped_column(Boolean, server_default=text("TRUE"))
    active_at: Mapped[datetime | None] = mapped_column(DateTime)
    disactive_at: Mapped[datetime | None] = mapped_column(DateTime)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, server_onupdate=text("NOW()"))

    # roles: Mapped[list["RolesOrm"]] = relationship(
    #     back_populates="UsersOrm",
    #     secondary="users_roles",
    # )
