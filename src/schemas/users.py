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
    roles_ids: list[int] | None = [4] # 4 - default user


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
    disactive_at: datetime | None = None
    mark_for_del: bool
    deleted_at: datetime | None = None
    update_at: datetime | None = None

    model_config = ConfigDict( from_attributes=True )


class UserWithHashedPassword(User):
    hashed_password: str


class UserRequestLogin(BaseModel):
    email: EmailStr
    password: str


class UserPatchRequest(BaseModel):
    last_name: str | None = None
    first_name: str | None = None
    patronimic: str | None = None
    city: str | None = None
    email: str | None = None
    phone: str | None = None
    isBlocked: bool | None = None
    isActive: bool | None = None
    mark_for_del: bool | None = None
    roles_ids: list[int] | None = []


class UserPatch(BaseModel):
    last_name: str | None = None
    first_name: str | None = None
    patronimic: str | None = None
    city: str | None = None
    email: str | None = None
    phone: str | None = None
    isBlocked: bool | None = None
    blocked_at: datetime | None = None
    isActive: bool | None = None
    disactive_at: datetime | None = None
    mark_for_del: bool | None = None
    deleted_at: datetime | None = None
    updated_at: datetime | None = None
