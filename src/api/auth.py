from fastapi import APIRouter, Body
from passlib.context import CryptContext

from src.database import async_session_maker_talent_city
from src.repositories.users import UsersRepository
from src.schemas.users import UserRequestAdd, UserAdd

router = APIRouter(prefix='/auth', tags=['Аутентификация и авторизация'])


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/register', summary="Регистрация пользователя")
async def register(
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
    hashed_password = pwd_context.hash(data.password)
    new_user_data = UserAdd(
        last_name=data.last_name,
        first_name=data.first_name,
        patronimic=data.patronimic,
        city=data.city,
        email=data.email,
        phone=data.phone,
        hashed_password=hashed_password
    )
    async with async_session_maker_talent_city() as session:
        await UsersRepository(session).add(new_user_data)
        await session.commit()

    return {"status": "OK"}


@router.post('/login')
async def login():
    ...


@router.get('/me')
async def get_me():
    ...


@router.post('/logout')
async def logout():
    ...
