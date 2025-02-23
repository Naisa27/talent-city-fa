from datetime import datetime

from pydantic import BaseModel, ConfigDict


class RolesAdd(BaseModel):
    title: str
    description: str | None = None
    level: int

    model_config = ConfigDict( from_attributes=True )


class Roles(RolesAdd):
    id: int
    created_at: datetime
    isActive: bool
    active_at: datetime | None = None
    disactive_at: datetime | None = None
    update_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class RolesPatch(BaseModel):
    title: str | None = None
    description: str | None = None
    level: int | None = None


