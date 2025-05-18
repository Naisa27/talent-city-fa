import json
from datetime import datetime

from fastapi import APIRouter, Body, Query
from fastapi_cache.decorator import cache

from src.api.dependencies import PaginationDep, DBDep, UserIdDep
from src.init import redis_manager
from src.schemas.article_themes import ArticleThemePatch, ArticleThemeAdd, ArticleThemeDel
from src.tasks.tasks import test_task
from src.utils.usefull import datetime_serialize

router = APIRouter(prefix="/article_themes", tags=["Справочник тем статей"])


@router.post("", summary="Добавление темы статьи")
async def create_article_theme(
    db: DBDep,
    user_id: UserIdDep,
    article_theme_data: ArticleThemeAdd = Body(
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
    theme = await db.articleThemes.add(article_theme_data)
    await db.commit()

    test_task.delay()

    return {"status": "OK", "data": theme}


@router.get("/{theme_id}", summary="Получение конкретной темы статьи")
async def get_article_theme(
    theme_id: int,
    user_id: UserIdDep,
    db: DBDep,
):
    return await db.articleThemes.get_one_or_none(id=theme_id, mark_for_del = False)


@router.get("", summary="Получение списка тем статей")
@cache(expire=10)
async def get_article_themes(
    pagination: PaginationDep,
    user_id: UserIdDep,
    db: DBDep,
    theme: str | None = Query(None, description="Тема статьи"),
):
    # articleThemes_from_cache = await redis_manager.get("articleThemes")
    #
    # if not articleThemes_from_cache:
    #     print("==== Идём в БД ====")
    #     articleThemes = await db.articleThemes.get_all(
    #         theme=theme,
    #         limit=pagination.per_page,
    #         offset=(pagination.page - 1) * pagination.per_page
    #     )
    #     articleThemes_schemas: list[dict] = [f.model_dump() for f in articleThemes]
    #     articleThemes_json = json.dumps(articleThemes_schemas, default=datetime_serialize)
    #     await redis_manager.set( "articleThemes", articleThemes_json, 10 )
    #
    #     return articleThemes
    # else:
    #     print("==== Идём в кэш ====")
    #     articleThemes_dicts = json.loads(articleThemes_from_cache)
    #     return  articleThemes_dicts
    print( "==== Идём в БД ====" )
    return await db.articleThemes.get_all(
        theme=theme,
        limit=pagination.per_page,
        offset=(pagination.page - 1) * pagination.per_page
    )


@router.patch("/{theme_id}", summary="Редактирование темы статьи")
async def update_article_theme(
    theme_id: int,
    user_id: UserIdDep,
    article_theme_data: ArticleThemePatch,
    db: DBDep,
):
    print(f"{article_theme_data}")
    await db.articleThemes.update( article_theme_data, exclude_unset = True, id=theme_id )
    await db.commit()
    return {"status": "OK" }


@router.delete(
    "/{theme_id}",
    summary="Удаление темы статьи",
    description="<h2>Удаление темы статьи помечает её как удалённую, но не удаляет из БД</h2>",
)
async def delete_article_theme(
    theme_id: int,
    user_id: UserIdDep,
    db: DBDep,
):
    article_theme_data = ArticleThemeDel(
        mark_for_del=True,
        deleted_at=datetime.now(),
        isActive=False,
        disactive_at=datetime.now(),
        update_at=datetime.now()
    )
    # print(f"{article_theme_data}")
    await db.articleThemes.update( article_theme_data, id=theme_id )
    await db.commit()
    return { "status": "OK" }
