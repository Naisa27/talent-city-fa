from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from src.models import UsersOrm
from src.repositories.base import BaseRepository
from src.schemas.users import User, UserWithHashedPassword


class UsersRepository(BaseRepository):
    model = UsersOrm
    schema = User

    async def get_user_with_hashed_password(self, email: EmailStr):
        query = select( self.model ).filter_by( email=email, mark_for_del = False, isActive = True )
        result = await self.session.execute( query )
        try:
            row = result.scalars().one()
        except NoResultFound as e:
            raise HTTPException( status_code=404, detail="User not found" )

        return UserWithHashedPassword.model_validate( row )
