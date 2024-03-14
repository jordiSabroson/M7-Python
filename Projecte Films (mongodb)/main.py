from fastapi import FastApi

app = FastApi()


@app.get("/")
def welcome():
    return {"Hola": "quetal"}
