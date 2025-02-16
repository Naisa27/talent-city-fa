from sqlalchemy import select, func

from src.models.article_themes import ArticleThemesOrm
from src.repositories.base import BaseRepository
from src.schemas.article_themes import ArticleThemes


class ArticleThemesRepository(BaseRepository):
    model = ArticleThemesOrm
    schema = ArticleThemes

    async def get_all(
            self,
            theme,
            limit,
            offset,
        ) -> list[ArticleThemes]:
        query = select(ArticleThemesOrm)

        if theme:
            query = query.filter(func.lower(ArticleThemesOrm.theme).contains({theme.strip().lower()}))

        query = (
            query
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(query)

        return [ArticleThemes.model_validate(item, from_attributes=True) for item in result.scalars().all()]
