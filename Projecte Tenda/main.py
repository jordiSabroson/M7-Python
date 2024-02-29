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
def getProductById(prod: Product):
    try:
        product_data = productDB.getProductById(prod.product_id)
        return {"ID": f"{product_data['product_id']}", "Nom": f"{product_data['name']}", "Descripció": f"{product_data['description']}", "Companyia": f"{product_data['company']}", "Preu": f"{product_data['price']}", "Unit": f"{product_data['unit']}"}
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
