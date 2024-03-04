from fastapi import FastAPI
from db import productDB
from model.Product import Product

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/product/")
def getProduct():
    try:
        products_data = productDB.getProductes()
        return {"data": products_data}
    except Exception as e:
        return {"message": f"Error en la consulta de productes: {str(e)}", "state": 500}


@app.get("/product/{id}")
def getProductById(id):
    try:
        product_data = productDB.getProductById(id)
        return {"data": product_data}
    except Exception as e:
        return {"message": f"Error en la consulta de productes: {str(e)}", "state": 500}


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
