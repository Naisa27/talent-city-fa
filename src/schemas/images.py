from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ImageAdd(BaseModel):
    name: str | None = None
    path: str

    model_config = ConfigDict( from_attributes=True )


class Image(BaseModel):
    id: int
    name: str | None = None
    path: str
    created_at: datetime
    isActive: bool
    mark_for_del: bool
    deleted_at: datetime | None = None
    updated_at: datetime | None = None
    disactive_at: datetime | None = None

    model_config = ConfigDict( from_attributes=True )

