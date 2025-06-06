from fastapi import APIRouter
from fastapi_cache.decorator import cache

from src.api.dependencies import UserIdDep, DBDep
from src.exceptions.base import AllreadyExistsException
from src.exceptions.favourites import FavouriteArticleAllreadyExistsHTTPException
from src.schemas.favourites import FavouriteArticle

router = APIRouter(prefix="/favourites", tags=["Избранное"])


@router.post("/articles/{article_id}", summary="Добавить статью в избранное")
async def add_article(
    article_id: int,
    user_id: UserIdDep,
    db: DBDep
):
    data = FavouriteArticle(user_id=user_id, article_id=article_id)
    try:
        await db.favourites.add(data)
        article = await db.articles.get_one_or_none(id=article_id)
        await db.commit()
    except AllreadyExistsException as e:
        raise FavouriteArticleAllreadyExistsHTTPException

    return {"status": "OK", "article": article}


@router.get("/articles", summary="Получить список избранных статей")
@cache(expire=10)
async def get_articles(
    db: DBDep,
):
    articles = await db.favourites.get_not_none()
    return articles


@router.get("/articles/me", summary="Получить список своих избранных статей")
@cache(expire=10)
async def get_my_articles(
    db: DBDep,
    user_id: UserIdDep
):
    articles = await db.favourites.get_not_none(user_id = user_id)
    return articles
