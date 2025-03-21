from pydantic import BaseModel
from sqlalchemy import select, insert, update, delete


class BaseRepository:
    model = None
    schema: BaseModel = None

    def __init__( self, session ):
        self.session = session

    async def get_filtered( self, *filter, **filter_by ):
        query = select( self.model ).filter(*filter).filter_by(**filter_by)
        result = await self.session.execute( query )
        return [self.schema.model_validate(row) for row in result.scalars().all()]

    async def get_all( self, *args, **kwargs ):
        return await self.get_filtered()

    async def get_one_or_none( self, **filter_by ):
        query = select( self.model ).filter_by(**filter_by)
        result = await self.session.execute( query )
        row = result.scalars().one_or_none()

        if not row:
            return None

        return self.schema.model_validate(row)

    async def add( self, data: BaseModel ):
        add_data_stmt = insert( self.model ).values( **data.model_dump() ).returning( self.model )
        # print(add_theme_stmt.compile(engine_talent_city, compile_kwargs={"literal_binds": True}))
        result = await self.session.execute( add_data_stmt )
        row = result.scalars().one()
        return self.schema.model_validate( row )

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