from datetime import datetime

from sqlalchemy import ForeignKey, DateTime, text
from sqlalchemy.orm import Mapped, mapped_column

from src.database import BaseTalentCity


class ArticlesImagesOrm(BaseTalentCity):
    __tablename__ = "articles_images"

    id: Mapped[int] = mapped_column(primary_key=True)
    article_id: Mapped[int] = mapped_column(ForeignKey("articles.id"))
    image_id: Mapped[int] = mapped_column(ForeignKey("images.id"))
    created_at: Mapped[datetime] = mapped_column( DateTime, server_default=text( "NOW()" ) )
