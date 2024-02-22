from fastapi import FastAPI
from db import productDB
from model.Product import Product

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/product/")
def getProduct():
    productDB.consulta()
    return {"message": "consulta producte", "state": 200}


@app.get("/product/{id}")
def getProductById(prod: Product):
    return {"ID": f"{prod.id}", "Nom": f"{prod.name}", "Descripció": f"{prod.description}", "Preu": f"{prod.price}", "Unit: ": f"{prod.unit}"}


@app.post("/product/")
def createProduct(prod: Product):
    insertat = productDB.insert_product(prod)
    return insertat


@app.put("/product/")
def updateProduct():
    return {"message": f"post"}


@app.delete("/product/")
def deleteProduct():
    return {"message": f"post"}
