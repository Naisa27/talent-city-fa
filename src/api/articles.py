from datetime import datetime

from fastapi import APIRouter, Body, Query

from src.api.dependencies import UserIdDep, PaginationDep, DBDep
from src.database import async_session_maker_talent_city
from src.repositories.articles import ArticlesRepository
from src.schemas.articles import ArticleAdd, ArticleRequestAdd, ArticleRequestPatch, ArticlePatch, ArticleDel, ArticleRestore

router = APIRouter(prefix="/articles", tags=["Статьи"])


@router.post("", summary="Добавить статью")
async def create_article(
    user_id: UserIdDep,
    db: DBDep,
    author_id: int | None = Query(default=None),
    article_data: ArticleRequestAdd = Body(
        openapi_examples={
            "1-": {
                "summary": "Первая",
                "value": {
                    "title": "Развитие памяти у детей",
                    "article_theme_id": 3,
                    "article_body": "Современные технологии развития памяти ребенка...",
                    "title_img": "https://cdn.pixabay.com/photo/2023/01/06/15/50/child-7694544_1280.jpg",
                }
            },
            "2-": {
                "summary": "Вторая",
                "value": {
                    "title": "Голографическая память",
                    "article_theme_id": 2,
                    "article_body": "Память на основе сферической матрицы...",
                }
            }
        }
    )
):
    # проверка, что пользователь либо автор статьи либо админ
    # если роль админ, то author_id - обязательно к заполнению, и именно его передаём в БД
    _article_data = ArticleAdd(
        user_id=user_id, **article_data.model_dump()
    )
    article = await db.Articles.add(_article_data)
    await db.commit()

    return {"status": "OK", "data": article}


@router.get("", summary="Получение списка статей с фильтрами для всех пользователей")
async def get_articles(
    pagination: PaginationDep,
    db: DBDep,
    title: str | None = Query(None, description="Заголовок статьи"),
    article_theme_id: int | None = Query(None, description="ID темы статьи"),
    article_body: str | None = Query(None, description="Содержание статьи"),
    author: int | None = Query(None, description="ID автора статьи"),
):
    return await db.Articles.get_all(
        title=title,
        article_theme_id=article_theme_id,
        article_body=article_body,
        author=author,
        limit=pagination.per_page,
        offset=(pagination.page - 1) * pagination.per_page
    )


@router.get("/me", summary="Получение списка только моих статей с фильтрами")
async def get_my_articles(
    user_id: UserIdDep,
    db: DBDep,
    pagination: PaginationDep,
    title: str | None = Query(None, description="Заголовок статьи"),
    article_theme_id: int | None = Query(None, description="ID темы статьи"),
    article_body: str | None = Query(None, description="Содержание статьи"),
):
    return await db.Articles.get_all(
        title=title,
        article_theme_id=article_theme_id,
        article_body=article_body,
        author=user_id,
        limit=pagination.per_page,
        offset=(pagination.page - 1) * pagination.per_page
    )


@router.get("/me/deleted", summary="Получение списка моих удалённых статей")
async def get_my_deleted_articles(
    user_id: UserIdDep,
    db: DBDep,
    pagination: PaginationDep,
):
    return await db.Articles.get_deleted(
        author=user_id,
        limit=pagination.per_page,
        offset=(pagination.page - 1) * pagination.per_page
    )


@router.post("/me/restore/{article_id}", summary="Восстановление удалённой статьи")
async def restore_my_deleted_article(
    article_id: int,
    user_id: UserIdDep,
    db: DBDep,
):
    # проверка, что пользователь либо автор статьи либо админ
    article_data = ArticleRestore(
        mark_for_del=False,
        deleted_at=None,
        updated_at=datetime.now()
    )
    await db.Articles.update( article_data, id=article_id )
    await db.commit()

    return {"status": "OK" }


@router.get("/{article_id}", summary="Получение конкретной статьи")
async def get_article(
    article_id: int,
    db: DBDep,
):
    return await db.Articles.get_one_or_none(id=article_id)


@router.patch("/{article_id}", summary="Редактирование статьи")
async def update_article(
    article_id: int,
    article_data: ArticleRequestPatch,
    user_id: UserIdDep,
    db: DBDep,
):
    # проверка, что пользователь либо автор статьи либо админ
    data_dt = {
        "updated_at": datetime.now(),
    }
    if article_data.isPublish:
        data_dt["publish_at"] = datetime.now()

    elif not article_data.isPublish:
        data_dt["unpublish_at"] = datetime.now()

    _article_data_dict = article_data.model_dump( exclude_unset=True )
    _article_data = ArticlePatch(**_article_data_dict, **data_dt)
    await db.Articles.update(_article_data, exclude_unset=True, id=article_id)
    await db.commit()

    return {"status": "OK" }


@router.delete(
    "/{article_id}",
    summary="Удаление статьи",
    description="<h2>Удаление статьи помечает её как удалённую, но не удаляет из БД</h2>",
)
async def delete_article(
    article_id: int,
    user_id: UserIdDep,
    db: DBDep,
):
    # проверка, что пользователь либо автор статьи либо админ
    article_data = ArticleDel(
        mark_for_del=True,
        deleted_at=datetime.now(),
        isPublish=False,
        unpublish_at=datetime.now(),
        updated_at=datetime.now()
    )
    await db.Articles.update(article_data, id=article_id)
    await db.commit()

    return {"status": "OK" }
