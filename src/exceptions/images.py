from src.exceptions.base import TalentCityHTTPException


class ImagesAllreadyExistsHTTPException(TalentCityHTTPException):
    status_code = 409
    detail = "Такое изображение уже существует"
    