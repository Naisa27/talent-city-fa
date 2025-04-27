from datetime import datetime

from fastapi import APIRouter, Body

from src.api.dependencies import DBDep, UserIdDep
from src.schemas.users import UserPatchRequest, UserPatch, User
from src.schemas.users_roles import UserRoleAdd

router = APIRouter(prefix='/users', tags=['Пользователи'])


@router.patch(
    "/{user_id}",
    summary="Изменить данные пользователя",
    description="Изменение пользователей только в админке только администратором"
)
async def update_user(
    db: DBDep,
    admin_id: UserIdDep,
    user_id: int,
    user_data: UserPatchRequest = Body(
        openapi_examples={
            "1-": {
                "summary": "ivanov id=1",
                "value": {
                    "last_name": "Иванюк",
                    "first_name": "Вася",
                    "patronimic": "Исаакиевич",
                    "city": "Казань",
                    "email": "ivanuk@mail.ru",
                    "phone": "+79981234567",
                    "isBlocked": True,
                    "isActive": False,
                    "mark_for_del": True,
                    "roles_ids": [1, 2],
                }
            },
            "2-": {
                "summary": "petrov id=5",
                "value": {
                    "last_name": "Федоров",
                    "first_name": "Петя",
                    "patronimic": "Игоревич",
                    "city": "Владивосток",
                    "email": "fedya@mail.ru",
                    "phone": "+79981237654",
                    "isBlocked": True,
                    "isActive": False,
                    "mark_for_del": True,
                    "roles_ids": [1, 2],
                }
            }
        }
    )
):
    user_from_db: User = await db.users.get_one(id=user_id)

    data_dt: dict = {
        "updated_at": datetime.now(),
    }

    if user_data.isBlocked:
        data_dt["blocked_at"] = datetime.now()

    if not user_data.isActive and user_from_db.isActive:
        data_dt["disactive_at"] = datetime.now()
    elif user_data.isActive and not user_from_db.isActive:
        data_dt["disactive_at"] = None

    if user_data.mark_for_del:
        data_dt["deleted_at"] = datetime.now()

    _user_data = user_data.model_dump(exclude_unset=True)
    _user_data = UserPatch(**_user_data, **data_dt)
    await db.users.update(_user_data, exclude_unset=True, id=user_id)

    if "roles_ids" in _user_data:
        await db.users_roles.set_user_role( user_id=user_id, roles_ids=_user_data.roles_ids )

    await db.commit()

    return {"status": "OK"}
