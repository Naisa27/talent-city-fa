from sqlalchemy import select, func

from src.models.article_themes import ArticleThemesOrm
from src.repositories.base import BaseRepository


class ArticleThemesRepository(BaseRepository):
    model = ArticleThemesOrm

    async def get_all(
            self,
            theme,
            limit,
            offset,
        ):
        query = select(ArticleThemesOrm)

        if theme:
            query = query.filter(func.lower(ArticleThemesOrm.theme).contains({theme.strip().lower()}))

        query = (
            query
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(query)
        return result.scalars().all()
