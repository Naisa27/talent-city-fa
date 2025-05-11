from src.models import ArticleThemesOrm, ArticlesOrm, FavouritesOrm, RolesOrm, UsersOrm, UsersRolesOrm
from src.repositories.mappers.base import DataMapper
from src.schemas.article_themes import ArticleTheme
from src.schemas.articles import Article
from src.schemas.favourites import FavouriteArticle
from src.schemas.roles import Role
from src.schemas.users import User, UserWithHashedPassword, UserWithRels
from src.schemas.users_roles import UserRole


class ArticleThemesDataMapper(DataMapper):
    db_model = ArticleThemesOrm
    schema = ArticleTheme


class ArticleDataMapper(DataMapper):
    db_model = ArticlesOrm
    schema = Article


class FavouriteDataMapper(DataMapper):
    db_model = FavouritesOrm
    schema = FavouriteArticle


class RoleDataMapper(DataMapper):
    db_model = RolesOrm
    schema = Role


class UserDataMapper(DataMapper):
    db_model = UsersOrm
    schema = User


class UserWithHashedPasswordDataMapper(DataMapper):
    db_model = UsersOrm
    schema = UserWithHashedPassword


class UserWithRelsDataMapper(DataMapper):
    db_model = UsersOrm
    schema = UserWithRels


class UserRoleDataMapper(DataMapper):
    db_model = UsersRolesOrm
    schema = UserRole
