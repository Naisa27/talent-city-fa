from pydantic import BaseModel


class ArticleThemes(BaseModel):
    theme: str
    description: str | None = None


class ArticleThemesPatch(BaseModel):
    theme: str | None = None
    description: str | None = None

    