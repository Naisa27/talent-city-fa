from datetime import datetime

from sqlalchemy import String, Text, DateTime, Boolean, text
from sqlalchemy.orm import Mapped, mapped_column

from src.database import BaseTalentCity


class ArticleThemesOrm(BaseTalentCity):
    __tablename__ = "article_themes"

    id: Mapped[int] = mapped_column(primary_key=True)
    theme: Mapped[str] = mapped_column(String(250))
    description: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("NOW()"))
    isActive: Mapped[bool] = mapped_column(Boolean, server_default=text("TRUE"))
    active_at: Mapped[datetime | None] = mapped_column(DateTime)
    mark_for_del: Mapped[bool] = mapped_column(Boolean, server_default=text("FALSE"))
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime)
    update_at: Mapped[datetime | None] = mapped_column(DateTime, server_onupdate=text("NOW()"))