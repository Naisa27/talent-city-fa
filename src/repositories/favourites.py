from sqlalchemy import select

from src.models import FavouritesOrm
from src.repositories.base import BaseRepository
from src.schemas.favourites import FavouriteArticle


class FavouritesRepository(BaseRepository):
    model = FavouritesOrm
    schema = FavouriteArticle

    async def get_not_none( self, **filter_by ):
        query = select(self.model).filter(self.model.article_id.is_not(None)).filter_by(**filter_by)
        result = await self.session.execute( query )
        return [self.schema.model_validate( row ) for row in result.scalars().all()]


