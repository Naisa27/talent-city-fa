from pydantic import EmailStr
from sqlalchemy import select

from src.models import UsersOrm
from src.repositories.base import BaseRepository
from src.schemas.users import User, UserWithHashedPassword


class UsersRepository(BaseRepository):
    model = UsersOrm
    schema = User

    async def get_user_with_hashed_password(self, email: EmailStr):
        query = select( self.model ).filter_by( email=email )
        result = await self.session.execute( query )
        row = result.scalars().one()

        return UserWithHashedPassword.model_validate( row )
