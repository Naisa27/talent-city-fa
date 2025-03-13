from sqlalchemy import select, func

from src.database import engine_talent_city
from src.models.articles import ArticlesOrm
from src.repositories.base import BaseRepository
from src.schemas.articles import Article


class ArticlesRepository(BaseRepository):
    model = ArticlesOrm
    schema = Article

    async def get_all(
            self,
            title,
            article_theme_id,
            article_body,
            author,
            limit,
            offset,
        ) -> list[Article]:
        query = select(ArticlesOrm)

        if title:
            query = query.filter(func.lower(ArticlesOrm.title).contains(title.strip().lower()))

        if article_body:
            query = query.filter(func.lower(ArticlesOrm.article_body).contains({article_body.strip().lower()}))

        if article_theme_id:
            query = query.filter(ArticlesOrm.article_theme_id == article_theme_id)

        if author:
            query = query.filter(ArticlesOrm.user_id == author)

        query = (
            query
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(query)

        return [Article.model_validate(item, from_attributes=True) for item in result.scalars().all()]
