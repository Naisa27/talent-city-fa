from src.exceptions.base import TalentCityHTTPException


class FavouriteArticleAllreadyExistsHTTPException(TalentCityHTTPException):
    status_code = 409
    detail = "Такая статья в избранном уже существует"

