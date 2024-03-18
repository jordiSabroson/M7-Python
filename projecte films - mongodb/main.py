from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def welcome():
    return {"Hola": "que tal"}


@app.get("/films/")
def getFilms():
    return {}
