from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    description: str
    price: float


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/product/")
def getProduct():
    return {"message": "consulta producte", "state": 200}


@app.get("/product/{id}")
def getProductById(id: int):
    return {"message": f"consulta producte {id}"}


@app.post("/product/")
def createProduct(prod: Product):
    return {"message": f"el nom és {prod.name}"}


@app.put("/product/")
def updateProduct():
    return {"message": f"post"}


@app.delete("/product/")
def deleteProduct():
    return {"message": f"post"}
