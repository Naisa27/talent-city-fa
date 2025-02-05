from datetime import datetime

from sqlalchemy import String, Text, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from src.database import BaseTalentCity


class ArticlesOrm(BaseTalentCity):
    __tablename__ = "articles"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250))
    article_body: Mapped[str] = mapped_column(Text)
    title_img: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    isPublish: Mapped[bool] = mapped_column(Boolean, default=False)
    publish_at: Mapped[datetime] = mapped_column(DateTime)
    unpublish_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)
    mark_for_del: Mapped[bool] = mapped_column(Boolean, default=False)
    deleted_at: Mapped[datetime] = mapped_column(DateTime)
