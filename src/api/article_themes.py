from fastapi import APIRouter, Body, Query
from sqlalchemy import insert, select, func

from src.api.dependencies import PaginationDep
from src.database import async_session_maker_talent_city, engine_talent_city
from src.models.article_themes import ArticleThemesOrm
from src.repositories.article_themes import ArticleThemesRepository
from src.schemas.article_themes import ArticleThemes
router = APIRouter(prefix='/article_themes', tags=['Темы статей'])


@router.post('/', summary="Добавление темы статьи")
async def create_article_theme( article_theme_data: ArticleThemes = Body(
    openapi_examples = {
        "1": {
            "summary": "Первая",
            "value": {
                "theme": "Развитие памяти",
                "description": "мнемотехники",
            }
        },
        "2": {
            "summary": "Вторая",
            "value": {
                "theme": "Здоровье",
                "description": "техники для здоровья",
            }
        },
    }),
):
    async with async_session_maker_talent_city() as session:
        theme = await ArticleThemesRepository(session).add(article_theme_data)

        await session.commit()

    return {"status": "OK", "data": theme}


@router.get('/', summary="Получение списка тем статей")
async def get_article_themes(
    pagination: PaginationDep,
    theme: str | None = Query(None, description="Тема статьи"),
):
    async with async_session_maker_talent_city() as session:
        return await ArticleThemesRepository(session).get_all(
            theme=theme,
            limit=pagination.per_page,
            offset=(pagination.page - 1) * pagination.per_page
        )

