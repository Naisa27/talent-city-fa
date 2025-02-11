from fastapi import APIRouter, Body, Query
from sqlalchemy import insert, select, func

from src.api.dependencies import PaginationDep
from src.database import async_session_maker_talent_city, engine_talent_city
from src.models.article_themes import ArticleThemesOrm
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
        add_theme_stmt = insert(ArticleThemesOrm).values(**article_theme_data.model_dump())
        # print(add_theme_stmt.compile(engine_talent_city, compile_kwargs={"literal_binds": True}))
        await session.execute(add_theme_stmt)
        await session.commit()

    return {"status": "OK"}


@router.get('/', summary="Получение списка тем статей")
async def get_article_themes(
    pagination: PaginationDep,
    theme: str | None = Query(None, description="Тема статьи"),
):
    async with async_session_maker_talent_city() as session:
        query = select(ArticleThemesOrm)

        if theme:
            query = query.filter(func.lower(ArticleThemesOrm.theme).contains({theme.strip().lower()}))

        query = (
            query
            .limit(pagination.per_page)
            .offset((pagination.page - 1) * pagination.per_page)
        )
        result = await session.execute(query)
        themes = result.scalars().all()
        return themes

