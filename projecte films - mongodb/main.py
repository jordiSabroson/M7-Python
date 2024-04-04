from fastapi import FastAPI
from Controller import filmDB
from Model.Film import Film
from fastapi import Query

app = FastAPI()

@app.get("/")
def welcome():
    return {"Hola": "que tal"}

# Get de tots els films que pot rebre paràmetres per ordenar la resposta
@app.get("/films/")
def get_films(field: str = Query(None, description="Camp per ordenar (title, director, year)"),
              order: str = Query(None, description="Ordre (asc, desc)"),
              limit: int = Query(None, description="Límite de registros (1-100)")):
    return filmDB.get_films(field, order, limit)

# Get dels films per la seva id del mongo
@app.get("/film/{id}")
def get_film_by_id(id):
    return filmDB.get_film_by_id(id)

# Post per crear films
@app.post("/film")
def create_film(film: Film):
    nou_film = filmDB.create_film(film)
    nou_film["data"]["_id"] = str(nou_film["data"]["_id"])
    return nou_film

# Put per modificar un film segons la seva id
@app.put("/film/{id}")
def update_film(id, film: Film):
    return filmDB.update_film(id, film.model_dump())

# Delete per esborrar un film segons la seva id
@app.delete("/film/{id}")
def delete_film(id):
    return filmDB.delete_film(id)

# Consulta avançada que utilitza els query parameters per filtrar per gènere
@app.get("/film_genre")
def get_film(genre: str = Query(None, description="Gènere de la pel·lícula")):
    return filmDB.consulta_genre(genre)
