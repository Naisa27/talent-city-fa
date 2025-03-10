from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ArticleThemesAdd(BaseModel):
    theme: str
    description: str | None = None


class ArticleThemes(ArticleThemesAdd):
    id: int
    created_at: datetime
    isActive: bool
    active_at: datetime | None = None
    disactive_at: datetime | None = None
    update_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class ArticleThemesPatch(BaseModel):
    theme: str | None = None
    description: str | None = None

    