from datetime import datetime

from sqlalchemy import String, Text, DateTime, Boolean, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column

from src.database import BaseTalentCity


class ArticlesOrm(BaseTalentCity):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(250))
    article_theme_id: Mapped[int] = mapped_column(ForeignKey("article_themes.id"))
    article_body: Mapped[str | None] = mapped_column(Text)
    title_img: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=text("NOW()"))
    isPublish: Mapped[bool] = mapped_column(Boolean, server_default=text("FALSE"))
    publish_at: Mapped[datetime | None] = mapped_column(DateTime)
    unpublish_at: Mapped[datetime | None] = mapped_column(DateTime)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, server_onupdate=text("NOW()"))
    mark_for_del: Mapped[bool] = mapped_column(Boolean, server_default=text("FALSE"))
    deleted_at: Mapped[datetime | None] = mapped_column(DateTime)
