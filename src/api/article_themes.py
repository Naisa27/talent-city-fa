from fastapi import APIRouter, Body, Query

from src.api.dependencies import PaginationDep
from src.database import async_session_maker_talent_city
from src.repositories.article_themes import ArticleThemesRepository
from src.schemas.article_themes import ArticleThemesPatch, ArticleThemesAdd

router = APIRouter(prefix="/article_themes", tags=["Темы статей"])


@router.post("", summary="Добавление темы статьи")
async def create_article_theme( article_theme_data: ArticleThemesAdd = Body(
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


@router.get("/{theme_id}", summary="Получение конкретной темы статьи")
async def get_article_theme(theme_id: int):
    async with async_session_maker_talent_city() as session:
        return await ArticleThemesRepository(session).get_one_or_none(id=theme_id)


@router.get("", summary="Получение списка тем статей")
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


# @router.put('/{theme_id}', summary="Редактирование темы статьи")
# async def update_article_theme(
#     theme_id: int,
#     article_theme_data: ArticleThemes,
# ):
#     async with async_session_maker_talent_city() as session:
#         await ArticleThemesRepository( session ).update( article_theme_data, id=theme_id )
#         await session.commit()
#     return {"status": "OK" }


@router.patch("/{theme_id}", summary="Редактирование темы статьи")
async def update_article_theme(
    theme_id: int,
    article_theme_data: ArticleThemesPatch,
):
    async with async_session_maker_talent_city() as session:
        await ArticleThemesRepository( session ).update( article_theme_data, exclude_unset = True, id=theme_id )
        await session.commit()
    return {"status": "OK" }


@router.delete("/{theme_id}", summary="Удаление темы статьи")
async def delete_article_theme(
    theme_id: int,
):
    async with async_session_maker_talent_city() as session:
        await ArticleThemesRepository( session ).delete( id=theme_id )
        await session.commit()
    return {"status": "OK" }
