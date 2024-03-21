from fastapi import FastAPI
from Controller import filmDB
from Model.Film import Film

app = FastAPI()


@app.get("/")
def welcome():
    return {"Hola": "que tal"}


@app.get("/films/")
def get_films():
    return filmDB.get_films()


@app.get("/film/{id}")
def get_film_by_id(id):
    return filmDB.get_film_by_id(id)


@app.post("/film")
def create_film(film: Film):
    nou_film = filmDB.create_film(film)
    nou_film["data"]["_id"] = str(nou_film["data"]["_id"])
    return nou_film


@app.put("/film/{id}")
def update_film(id, film: Film):
    return filmDB.update_film(id, film.model_dump())


@app.delete("/film/{id}")
def delete_film(id):
    return filmDB.delete_film(id)
