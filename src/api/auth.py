from fastapi import APIRouter, Body, HTTPException, Response

from src.api.dependencies import UserIdDep, DBDep
from src.schemas.users import UserRequestAdd, UserAdd, UserRequestLogin
from src.schemas.users_roles import UserRoleAdd
from src.services.auth import AuthService

router = APIRouter(prefix='/auth', tags=['Аутентификация и авторизация'])


@router.post('/register', summary="Регистрация пользователя")
async def register(
    db: DBDep,
    data: UserRequestAdd = Body(
        openapi_examples={
            "1": {
                "summary": "Первый",
                "value": {
                    "last_name": "Иванов",
                    "first_name": "Иван",
                    "patronimic": "Иванович",
                    "city": "Москва",
                    "email": "ivanov@mail.ru",
                    "phone": "9991234567",
                    "password": "123456"
                }
            },
            "2": {
                "summary": "Второй",
                "value": {
                    "last_name": "Петров",
                    "first_name": "Петр",
                    "patronimic": "Петрович",
                    "city": "Санкт-Петербург",
                    "email": "petrov@mail.ru",
                    "phone": "9997654321",
                    "password": "654321"
                }
            }
        }
    ),
):
    hashed_password = AuthService().hash_password(data.password)
    new_user_data = UserAdd(
        last_name=data.last_name,
        first_name=data.first_name,
        patronimic=data.patronimic,
        city=data.city,
        email=data.email,
        phone=data.phone,
        hashed_password=hashed_password
    )
    user = await db.users.add(new_user_data)

    users_roles_data = [UserRoleAdd(user_id=user.id, role_id=role_id) for role_id in data.roles_ids]
    await db.users_roles.add_bulk(users_roles_data)
    await db.commit()

    return {"status": "OK"}


@router.post('/login', summary="Залогинивание пользователя")
async def login(
    response: Response,
    db: DBDep,
    data: UserRequestLogin = Body(
        openapi_examples={
            "1": {
                "summary": "Первый",
                "value": {
                    "email": "ivanov@mail.ru",
                    "password": "123456"
                },
            },
            "2": {
                "summary": "Второй",
                "value": {
                    "email": "petrov@mail.ru",
                    "password": "654321"
                },
            },
        },
    ),
):
    user = await db.users.get_user_with_hashed_password(email=data.email)

    if not user:
        raise HTTPException(status_code=401, detail="Пользователь не зарегистрирован")

    if not AuthService().verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Неверный пароль")

    access_token = AuthService().create_access_token({"user_id": user.id, "roles": user.roles})
    response.set_cookie("access_token", access_token)

    return {"access_token": access_token}


@router.get('/me', summary="Получить данные залогиненного пользователя")
async def get_me(
    user_id: UserIdDep,
    db: DBDep
):
    user = await db.users.get_one_or_none_with_roles(id=user_id)
    return user


@router.post('/logout', summary="Выход. Разлогинивание пользователя")
async def logout(
    response: Response,
):
    response.delete_cookie("access_token")
    return {"status": "OK"}
