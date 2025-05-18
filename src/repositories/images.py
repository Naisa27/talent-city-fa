from src.models import ImagesOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import ImageDataMapper


class ImagesRepository(BaseRepository):
    model = ImagesOrm
    mapper = ImageDataMapper

