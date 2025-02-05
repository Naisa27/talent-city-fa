from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import settings

engine_talent_city = create_async_engine(settings.DB_TALENT_CITY_URL)

async_session_maker_talent_city = async_sessionmaker(bind=engine_talent_city, expire_on_commit=False)


class BaseTalentCity(DeclarativeBase):
    pass
