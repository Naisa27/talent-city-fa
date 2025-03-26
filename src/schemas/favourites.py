from pydantic import BaseModel, ConfigDict


class FavouriteArticle(BaseModel):
    article_id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)