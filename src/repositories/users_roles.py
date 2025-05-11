from sqlalchemy import select, delete, insert

from src.models import UsersRolesOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mappers import UserRoleDataMapper


class UsersRolesRepository(BaseRepository):
    model = UsersRolesOrm
    mapper = UserRoleDataMapper

    async def set_user_role( self, user_id: int, role_ids: list[int] ) -> None:
        current_role_ids_from_db_query = (
            select(self.model.role_id)
            .filter_by(user_id=user_id)
        )

        res = await self.session.execute( current_role_ids_from_db_query )
        current_role_ids_from_db: list[int] = res.scalars().all()
        ids_to_delete: list[int] = list(set(current_role_ids_from_db) - set(role_ids))
        ids_to_insert: list[int] = list(set(role_ids) - set(current_role_ids_from_db))

        if ids_to_delete:
            del_m2m_roles_stmt = (
                delete(self.model)
                .filter(
                    self.model.user_id == user_id,
                    self.model.role_id.in_(ids_to_delete)
                )
            )
            await self.session.execute(del_m2m_roles_stmt)

        if ids_to_insert:
            insert_m2m_roles_stmt = (
                insert(self.model)
                .values([{"user_id": user_id, "role_id": id} for id in ids_to_insert])
            )
            await self.session.execute(insert_m2m_roles_stmt)

