from pydantic import BaseModel
from datetime import datetime


class Film(BaseModel):
    title: str
    director: str
    year: int
    genre: str
    rating: float
    country: str
    created_at: datetime = None
    update_at: datetime = None
