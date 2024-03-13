from pydantic import BaseModel


class Product(BaseModel):
    # Atributs de l'objecte Product que utilitzarem per a fer els inserts
    name: str
    description: str
    company: str
    price: float
    units: int
    subcategory_id: int
