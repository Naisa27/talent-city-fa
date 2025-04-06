from src.models import RolesOrm
from src.repositories.base import BaseRepository
from src.schemas.roles import Role


class RolesRepository(BaseRepository):
    model = RolesOrm
    schema = Role
