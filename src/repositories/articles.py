from sqlalchemy import select, func

from src.models.articles import ArticlesOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ArticleDataMapper
from src.schemas.articles import Article


class ArticlesRepository(BaseRepository):
    model = ArticlesOrm
    mapper = ArticleDataMapper

    async def get_all(
            self,
            title,
            article_theme_id,
            article_body,
            author_id,
            limit,
            offset,
        ) -> list[Article]:
        query = select(self.model)

        if title:
            query = query.filter(func.lower(self.model.title).contains(title.strip().lower()))

        if article_body:
            query = query.filter(func.lower(self.model.article_body).contains({article_body.strip().lower()}))

        if article_theme_id:
            query = query.filter(self.model.article_theme_id == article_theme_id)

        if author_id:
            query = query.filter(self.model.user_id == author_id)

        query = (
            query
            .filter(self.model.mark_for_del == False)
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(query)

        return [self.mapper.map_to_domain_entity(item) for item in result.scalars().all()]


    async def get_deleted(
        self,
        author_id,
        limit,
        offset
    ) -> list[Article]:
        query = (
            select( self.model )
            .filter(
                self.model.mark_for_del == True,
                self.model.user_id == author_id
            )
            .limit( limit )
            .offset( offset )
        )
        result = await self.session.execute(query)

        return [self.mapper.map_to_domain_entity(item) for item in result.scalars().all()]
