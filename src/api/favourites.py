from fastapi import APIRouter

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
        await db.Favourites.add(data)
        article = await db.Articles.get_one_or_none(id=article_id)
        await db.commit()
    except AllreadyExistsException as e:
        raise FavouriteArticleAllreadyExistsHTTPException

    return {"status": "OK", "article": article}
