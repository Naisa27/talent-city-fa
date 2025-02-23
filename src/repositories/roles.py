from src.models import RolesOrm
from src.repositories.base import BaseRepository
from src.schemas.roles import Roles


class RolesRepository(BaseRepository):
    model = RolesOrm
    schema = Roles
