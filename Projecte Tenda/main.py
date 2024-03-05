from fastapi import FastAPI, File, UploadFile
from db import productDB
from model.Product import Product

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hola": "Bondia"}


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


@app.put("/product/{id}")
def updateProduct(id, prod: Product):
    modificat = productDB.modifyProduct(id, prod)
    return modificat


@app.delete("/product/{id}")
def deleteProduct(id):
    eliminat = productDB.deleteProduct(id)
    return eliminat


@app.get("/productAll/")
def getAllProducts():
    retorn = productDB.getAllProducts()
    return retorn


@app.post("/loadProducts")
async def loadProducts(file: UploadFile):
    fitxer = productDB.loadProducts(file)
    return fitxer
