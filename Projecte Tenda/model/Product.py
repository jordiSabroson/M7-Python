from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    company: str
    price: float
    units: int
    subcategory_id: int
