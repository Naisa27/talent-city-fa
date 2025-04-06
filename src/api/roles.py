from fastapi import APIRouter, Body

from src.api.dependencies import DBDep, UserIdDep
from src.database import async_session_maker_talent_city
from src.repositories.roles import RolesRepository
from src.schemas.roles import RoleAdd, RolePatch

router = APIRouter(prefix="/roles", tags=['Справочник ролей пользователей'])

@router.post("", summary="Добавление новой роли в справочник")
async def create_role(
    db: DBDep,
    user_id: UserIdDep,
    role_data: RoleAdd = Body(
        openapi_examples = {
            "1": {
                "summary": "Первая",
                "value": {
                    "title": "admin",
                    "description": "самый главный, всё можно",
                    "level": 1
                },
            },
            "2": {
                "summary": "Вторая",
                "value": {
                    "title": "autor",
                    "description": "может писать статьи",
                    "level": 100
                }
            },
        }
    )
):
    role = await db.roles.add(role_data)
    await db.commit()

    return {"status": "OK", "data": role}


@router.get("", summary="Получение списка ролей")
async def get_roles(
    db: DBDep,
    user_id: UserIdDep,
):
    roles = await db.roles.get_all()
    return {"status": "OK", "data": roles}


@router.patch("/{id}", summary="Изменение роли в справочнике")
async def update_role(
    role_id: int,
    db: DBDep,
    user_id: UserIdDep,
    role_data: RolePatch = Body(
    openapi_examples = {
            "1": {
                "summary": "для id = 1",
                "value": {
                    "title": "administrator",
                    "level": 1
                },
            },
            "2": {
                "summary": "для id = 2",
                "value": {
                    "description": "может добавлять свои статьи",
                    "level": 500
                }
            },
        }
    )
):
    await db.roles.update(role_data, exclude_unset = True, id = role_id)
    await db.commit()
    return {"status": "OK"}


@router.delete("/{id}", summary="Удаление роли из справочника")
async def delete_role(
    role_id: int,
    db: DBDep,
    user_id: UserIdDep,
):
    await db.roles.delete(id = role_id)
    await db.commit()
    return {"status": "OK"}
