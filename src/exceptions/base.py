from fastapi import HTTPException


class TalentCityException(Exception):
    detail = "Неожиданная ошибка"

    def __init__(self, *args, **kwargs):
        super().__init__(self.detail, *args, **kwargs)


class TalentCityHTTPException(HTTPException):
    status_code = 500
    detail = None

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class AllreadyExistsException(TalentCityException):
    detail = "Такой объект уже существует"




