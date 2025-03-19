import typing
from datetime import datetime

from sqlalchemy import String, DateTime, text, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import BaseTalentCity

if typing.TYPE_CHECKING:
    from src.models import UsersOrm


class RolesOrm(BaseTalentCity):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column( primary_key=True )
    title: Mapped[str] = mapped_column(String(250))
    description: Mapped[str | None] = mapped_column(String(250))
    level: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("NOW()"))
    isActive: Mapped[bool] = mapped_column(Boolean, server_default=text("TRUE"))
    active_at: Mapped[datetime | None] = mapped_column(DateTime)
    mark_for_del: Mapped[bool] = mapped_column(Boolean, server_default=text("FALSE"))
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, server_onupdate=text("NOW()"))

    # users: Mapped[list["UsersOrm"]] = relationship(
    #     back_populates="RolesOrm",
    #     secondary="users_roles",
    # )
