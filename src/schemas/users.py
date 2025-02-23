from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserRequestAdd(BaseModel):
    last_name: str
    first_name: str
    patronimic: str | None = None
    city: str | None = None
    email: EmailStr
    phone: str
    password: str


class UserAdd(BaseModel):
    last_name: str
    first_name: str
    patronimic: str | None = None
    city: str | None = None
    email: EmailStr
    phone: str
    hashed_password: str

    model_config = ConfigDict( from_attributes=True )


class User(BaseModel):
    id: int
    last_name: str
    first_name: str
    patronimic: str | None = None
    city: str | None = None
    email: EmailStr
    phone: str
    created_at: datetime
    isBlocked: bool
    blocked_at: datetime | None = None
    isActive: bool
    active_at: datetime | None = None
    disactive_at: datetime | None = None
    update_at: datetime | None = None

    model_config = ConfigDict( from_attributes=True )


class UserWithHashedPassword(User):
    hashed_password: str

class UserRequestLogin(BaseModel):
    email: EmailStr
    password: str
