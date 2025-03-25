from fastapi import APIRouter, Body

from src.api.dependencies import DBDep
from src.database import async_session_maker_talent_city
from src.repositories.roles import RolesRepository
from src.schemas.roles import RolesAdd

router = APIRouter(prefix="/roles", tags=['Роли пользователей'])

@router.post("")
async def create_role(
    db: DBDep,
    role_data: RolesAdd = Body(
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
    role = await db.Roles.add(role_data)
    await db.commit()

    return {"status": "OK", "data": role}