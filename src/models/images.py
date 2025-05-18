from datetime import datetime

from sqlalchemy import String, DateTime, text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.database import BaseTalentCity


class ImagesOrm(BaseTalentCity):
    __tablename__ = "images"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int] = mapped_column(String(250))
    path: Mapped[str] = mapped_column(String(250))
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("NOW()"))
    isActive: Mapped[bool] = mapped_column(Boolean, server_default=text("TRUE"))
    mark_for_del: Mapped[bool] = mapped_column( Boolean, server_default=text( "FALSE" ) )
    deleted_at: Mapped[datetime | None] = mapped_column( DateTime )
    updated_at: Mapped[datetime | None] = mapped_column( DateTime )
    disactive_at: Mapped[datetime | None] = mapped_column( DateTime )
