from fastapi import APIRouter

router = APIRouter(prefix='/auth', tags=['Аутентификация и авторизация'])


@router.post('/register')
async def register():
    ...


@router.post('/login')
async def login():
    ...


@router.get('/me')
async def get_me():
    ...


@router.post('/logout')
async def logout():
    ...
