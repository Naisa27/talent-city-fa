from fastapi import APIRouter, Body, Query

from src.api.dependencies import UserIdDep, PaginationDep
from src.database import async_session_maker_talent_city
from src.repositories.articles import ArticlesRepository
from src.schemas.articles import ArticleAdd, ArticleRequestAdd

router = APIRouter(prefix="/articles", tags=["Статьи"])


@router.post("", summary="Добавить статью")
async def create_article(
    user_id: UserIdDep,
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
    _article_data = ArticleAdd(
        user_id=user_id, **article_data.model_dump()
    )
    async with async_session_maker_talent_city() as session:
        article = await ArticlesRepository(session).add(_article_data)

        await session.commit()

    return {"status": "OK", "data": article}


@router.get("", summary="Получение списка статей")
async def get_articles(
    pagination: PaginationDep,
    title: str | None = Query(None, description="Заголовок статьи"),
    article_theme_id: int | None = Query(None, description="ID темы статьи"),
    article_body: str | None = Query(None, description="Содержание статьи"),
    author: int | None = Query(None, description="ID автора статьи"),
):
    async with async_session_maker_talent_city() as session:
        return await ArticlesRepository(session).get_all(
            title=title,
            article_theme_id=article_theme_id,
            article_body=article_body,
            author=author,
            limit=pagination.per_page,
            offset=(pagination.page - 1) * pagination.per_page
        )
