from pydantic import BaseModel


class UserRoleAdd(BaseModel):
    user_id: int
    role_id: int


class UserRole(UserRoleAdd):
    id: int
