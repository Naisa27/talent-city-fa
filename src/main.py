import sys
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI

import uvicorn

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

# альтернативный путь к документации, если основной сильно тормозит или вообще не грузит
from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

# если не видит файлы в папке src
sys.path.append(str(Path(__file__).parent.parent))

from src.init import redis_manager


from src.api.auth import router as auth_router
from src.api.index import router as index_router
from src.api.users import router as users_router
from src.api.admin import router as admin_router
from src.api.article_themes import router as article_themes_router
from src.api.articles import router as articles_router
from src.api.roles import router as roles_router
from src.api.favourites import router as favourites_router
from src.api.images import router as images_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # При старте
    await redis_manager.connect()
    print("Starting up app")
    FastAPICache.init( RedisBackend( redis_manager.redis ), prefix="fastapi-cache" )
    yield
    await redis_manager.close()
    print("Finished app!")
    # При выключении/перезагрузке

app = FastAPI(
    title = "API - сайт Город талантов",
    docs_url=None,
    lifespan=lifespan,
)

app.include_router(auth_router)
app.include_router(index_router)
app.include_router(users_router)
app.include_router(admin_router)
app.include_router(article_themes_router)
app.include_router(articles_router)
app.include_router(roles_router)
app.include_router(favourites_router)
app.include_router(images_router)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title,
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
    )


# альтернативный путь к документации, если основной сильно тормозит или вообще не грузит
@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
