from src.models.articles import ArticlesOrm
from src.repositories.base import BaseRepository


class ArticlesRepository(BaseRepository):
    model = ArticlesOrm