from src.models import FavouritesOrm
from src.repositories.base import BaseRepository
from src.schemas.favourites import FavouriteArticle


class FavouritesRepository(BaseRepository):
    model = FavouritesOrm
    schema = FavouriteArticle
