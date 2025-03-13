from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ArticleRequestAdd(BaseModel):
    title: str
    article_theme_id: int
    article_body: str | None = None
    title_img: str | None = None

    model_config = ConfigDict(from_attributes=True)


class ArticleAdd(ArticleRequestAdd):
    user_id: int

    model_config = ConfigDict(from_attributes=True)


class Article(ArticleAdd):
    id: int
    user_id: int
    created_at: datetime
    isPublish: bool
    publish_at: datetime | None = None
    unpublish_at: datetime | None = None
    updated_at: datetime | None = None
    mark_for_del: bool = False
    deleted_at: datetime | None = None
