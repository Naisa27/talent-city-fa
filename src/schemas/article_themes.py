from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ArticleThemeAdd(BaseModel):
    theme: str
    description: str | None = None


class ArticleTheme(ArticleThemeAdd):
    id: int
    created_at: datetime
    isActive: bool
    disactive_at: datetime | None = None
    mark_for_del: bool
    deleted_at: datetime | None = None
    update_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class ArticleThemePatch(BaseModel):
    theme: str | None = None
    description: str | None = None


class ArticleThemeDel(BaseModel):
    mark_for_del: bool
    deleted_at: datetime
    isActive: bool
    disactive_at: datetime
    update_at: datetime
    