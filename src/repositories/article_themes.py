from sqlalchemy import select, func

from src.models.article_themes import ArticleThemesOrm
from src.repositories.base import BaseRepository
from src.schemas.article_themes import ArticleTheme


class ArticleThemesRepository(BaseRepository):
    model = ArticleThemesOrm
    schema = ArticleTheme

    async def get_all(
            self,
            theme,
            limit,
            offset,
        ) -> list[ArticleTheme]:
        query = select(ArticleThemesOrm).filter(self.model.mark_for_del == False, self.model.isActive == True)

        if theme:
            query = query.filter(func.lower(ArticleThemesOrm.theme).contains(theme.strip().lower()))

        query = (
            query
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(query)

        return [ArticleTheme.model_validate(item, from_attributes=True) for item in result.scalars().all()]
