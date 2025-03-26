from src.repositories.article_themes import ArticleThemesRepository
from src.repositories.articles import ArticlesRepository
from src.repositories.favourites import FavouritesRepository
from src.repositories.roles import RolesRepository
from src.repositories.users import UsersRepository



class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.ArticleThemes = ArticleThemesRepository(self.session)
        self.Articles = ArticlesRepository(self.session)
        self.Roles = RolesRepository(self.session)
        self.Users = UsersRepository(self.session)
        self.Favourites = FavouritesRepository(self.session)

        return self

    async def __aexit__( self, *args ):
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

