from pydantic import BaseModel


class Film(BaseModel):
    title: str
    director: str
    year: int
    genre: str
    rating: float
    country: str
    created_at: str
    update_at: str
