from src.models import RolesOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import RoleDataMapper


class RolesRepository(BaseRepository):
    model = RolesOrm
    mapper = RoleDataMapper
