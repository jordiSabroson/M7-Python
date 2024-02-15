from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/product/")
def read_root():
    return {"message": "consulta producte"}


@app.get("/product/{id}")
def getProductById(id: int):
    return {"message": f"consulta producte {id}"}
