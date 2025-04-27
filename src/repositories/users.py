from fastapi import HTTPException
from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import selectinload, joinedload

from src.models import UsersOrm
from src.repositories.base import BaseRepository
from src.schemas.users import User, UserWithHashedPassword, UserWithRels


class UsersRepository(BaseRepository):
    model = UsersOrm
    schema = User

    async def get_user_with_hashed_password(self, email: EmailStr):
        query = (
            select( self.model )
            .options(joinedload(self.model.roles))
            .filter_by( email=email, mark_for_del = False, isActive = True )
        )
        result = await self.session.execute( query )
        try:
            row = result.unique().scalars().one()
        except NoResultFound as e:
            raise HTTPException( status_code=404, detail="User not found" )

        user_with_roles = UserWithHashedPassword.model_validate( row )

        # передаём только id ролей при залогинивании
        user_with_roles.roles = [ role.id for role in user_with_roles.roles]

        return user_with_roles

    async def get_one_or_none_with_roles( self, **filter_by ):
        query = (
            select( self.model )
            .options( joinedload( self.model.roles ) )
            .filter_by(**filter_by)
        )

        result = await self.session.execute( query )
        row = result.unique().scalars().one_or_none()

        if not row:
            return None

        return UserWithRels.model_validate(row)
