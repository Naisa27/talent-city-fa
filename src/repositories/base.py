import logging

from asyncpg import UniqueViolationError
from pydantic import BaseModel
from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from src.exceptions.base import AllreadyExistsException
from src.repositories.mappers.base import DataMapper


class BaseRepository:
    model = None
    mapper: DataMapper = None

    def __init__( self, session ):
        self.session = session

    async def get_filtered( self, *filter, **filter_by ):
        query = select( self.model ).filter(*filter).filter_by(**filter_by)
        result = await self.session.execute( query )
        return [self.mapper.map_to_domain_entity(row) for row in result.scalars().all()]

    async def get_all( self, *args, **kwargs ):
        return await self.get_filtered()

    async def get_one_or_none( self, **filter_by ):
        query = select( self.model ).filter_by(**filter_by)

        result = await self.session.execute( query )
        row = result.scalars().one_or_none()

        if not row:
            return None

        return self.mapper.map_to_domain_entity(row)

    async def get_one( self, **filter_by ):
        query = select( self.model ).filter_by(**filter_by)

        result = await self.session.execute( query )
        row = result.scalars().one()

        return self.mapper.map_to_domain_entity(row)

    async def get_not_none_filtered( self, column: str, **filter_by ):
        query = select(self.model).filter(self.model[column].is_not(None)).filter_by(**filter_by)
        result = await self.session.execute( query )
        return [self.mapper.map_to_domain_entity( row ) for row in result.scalars().all()]

    async def get_all_not_none( self ):
        return await self.get_not_none_filtered()

    async def add( self, data: BaseModel ):
        add_data_stmt = insert( self.model ).values( **data.model_dump() ).returning( self.model )
        # print(add_theme_stmt.compile(engine_talent_city, compile_kwargs={"literal_binds": True}))
        try:
            result = await self.session.execute( add_data_stmt )
            row = result.scalars().one()
        except IntegrityError as e:
            if isinstance( e.orig.__cause__, UniqueViolationError ):
                raise AllreadyExistsException from e
            else:
                raise e

        return self.mapper.map_to_domain_entity( row )

    async def add_bulk( self, data: list[BaseModel] ):
        add_data_stmt = insert( self.model ).values( [item.model_dump() for item in data] )
        await self.session.execute( add_data_stmt )

    async def update( self, data: BaseModel, exclude_unset: bool = False, **filter_by ) -> None:
        update_stmt = (
            update( self.model )
            .filter_by( **filter_by )
            .values( **data.model_dump( exclude_unset=exclude_unset ) )
        )
        # print(update_stmt.compile(compile_kwargs={"literal_binds": True}))
        await self.session.execute( update_stmt )

    async def delete( self, **filter_by ) -> None:
        delete_stmt = delete( self.model ).filter_by( **filter_by )
        await self.session.execute( delete_stmt )