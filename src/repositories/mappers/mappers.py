from src.models import ArticleThemesOrm
from src.repositories.mappers.base import DataMapper
from src.schemas.article_themes import ArticleTheme


class ArticleThemesDataMapper(DataMapper):
    db_model = ArticleThemesOrm
    schema = ArticleTheme
