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


class ArticleRequestPatch(BaseModel):
    title: str | None = None
    article_theme_id: int | None = None
    article_body: str | None = None
    title_img: str | None = None
    isPublish: bool | None = None


class ArticlePatch(ArticleRequestPatch):
    publish_at: datetime | None = None
    unpublish_at: datetime | None = None
    updated_at: datetime


class ArticleDel(BaseModel):
    mark_for_del: bool
    deleted_at: datetime
    isPublish: bool
    unpublish_at: datetime
    updated_at: datetime


class ArticleRestore(BaseModel):
    mark_for_del: bool
    deleted_at: datetime | None = None
    updated_at: datetime
