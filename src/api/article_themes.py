from datetime import datetime

from fastapi import APIRouter, Body, Query

from src.api.dependencies import PaginationDep, DBDep
from src.database import async_session_maker_talent_city
from src.repositories.article_themes import ArticleThemesRepository
from src.schemas.article_themes import ArticleThemesPatch, ArticleThemesAdd, ArticleThemesDel

router = APIRouter(prefix="/article_themes", tags=["Темы статей"])


@router.post("", summary="Добавление темы статьи")
async def create_article_theme(
    db: DBDep,
    article_theme_data: ArticleThemesAdd = Body(
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
    theme = await db.ArticleThemes.add(article_theme_data)

    await db.commit()

    return {"status": "OK", "data": theme}


@router.get("/{theme_id}", summary="Получение конкретной темы статьи")
async def get_article_theme(
    theme_id: int,
    db: DBDep,
):
    return await db.ArticleThemes.get_one_or_none(id=theme_id, mark_for_del = False)


@router.get("", summary="Получение списка тем статей")
async def get_article_themes(
    pagination: PaginationDep,
    db: DBDep,
    theme: str | None = Query(None, description="Тема статьи"),
):
    return await db.ArticleThemes.get_all(
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
    db: DBDep,
):
    print(f"{article_theme_data}")
    await db.ArticleThemes.update( article_theme_data, exclude_unset = True, id=theme_id )
    await db.commit()
    return {"status": "OK" }


@router.delete(
    "/{theme_id}",
    summary="Удаление темы статьи",
    description="<h2>Удаление темы статьи помечает её как удалённую, но не удаляет из БД</h2>",
)
async def delete_article_theme(
    theme_id: int,
    db: DBDep,
):
    article_theme_data = ArticleThemesDel(
        mark_for_del=True,
        deleted_at=datetime.now(),
        isActive=False,
        disactive_at=datetime.now(),
        updated_at=datetime.now()
    )

    await db.ArticleThemes.update( article_theme_data, id=theme_id )
    await db.commit()
    return { "status": "OK" }
