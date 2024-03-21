from Model.Film import Film
from db import db_conf
from datetime import datetime
from bson import ObjectId


def get_films():
    try:
        # Objecte amb la conexió a la BBDD
        conn = db_conf.client()

        # Variable amb la col·lecció films
        collection = conn.films

        # Variable que emmagatzema tots els elements de la col·lecció films amb el mètode find()
        all_films = collection.find()

        # Convertir els documents en diccionari
        films_data = [film.copy() for film in all_films]
        for film in films_data:
            film["_id"] = str(film["_id"])

        return {"status": 1, "data": films_data}
    except Exception as e:
        return {"status": -1, "missatge": f'{e}'}


def get_film_by_id(id):
    try:
        conn = db_conf.client()
        collection = conn.films

        # Transformar l'ObjectId a string
        object_id = ObjectId(id)

        # Query per buscar l'element amb l'id especificada en forma de string
        one_film = collection.find_one(object_id)

        # Transformar l'ObjectId a string per poder imprimir-lo per pantalla
        one_film["_id"] = str(one_film["_id"])

        if one_film is None:
            return {"status": -1, "missatge": "pel·lícula no trobada"}

        return {"status": 1, "data": one_film}
    except Exception as e:
        return {"status": -1, "missatge": f'{e}'}


def create_film(nou_film: Film):
    try:
        conn = db_conf.client()
        collection = conn.films

        # Ajustar la data a la del moment de creació
        nou_film.created_at = datetime.now()

        # Transformar el nou objecte a diccionari
        film_dict = nou_film.model_dump()

        # Executar la query d'insert de l'objecte a la bbdd
        collection.insert_one(film_dict)

        # Transformar l'ObjectId a string
        film_dict["_id"] = str(film_dict["_id"])

        return {"status": 1, "data": film_dict}
    except Exception as e:
        return {"status": -1, "missatge": f'{e}'}


def update_film(id, film: Film):
    try:
        conn = db_conf.client()
        collection = conn.films

        object_id = ObjectId(id)

        query = collection.update_one({"_id": object_id}, {"$set": film})

        # Comprovar si la query ha sigut efectuada
        if query.modified_count == 0:
            return {"status": -1, "missatge": "La pel·lícula no s'ha trobat o els canvis no s'han efectuat"}

        # Variable que emmagatzema l'element actualitzat
        updated_film = collection.find_one(object_id)
        updated_film["_id"] = str(updated_film["_id"])

        return {"status": 1, "data": updated_film}
    except Exception as e:
        return {"status": -1, "missatge": f'{e}'}


def delete_film(id):
    try:
        conn = db_conf.client()
        collection = conn.films

        object_id = ObjectId(id)

        query = collection.delete_one({"_id": object_id})

        # Comprovar si la query ha sigut efectuada
        if query.deleted_count == 0:
            return {"status": -1, "missatge": "La pel·lícula no s'ha trobat"}

        return {"status": 1, "data": "Pel·lícula eliminada correctament"}
    except Exception as e:
        return {"status": -1, "missatge": f'{e}'}


# def base():
#     try:
#         conn = db_conf.client()
#         collection = conn.films
#         return {"status": 1, "data": "a"}
#     except Exception as e:
#         return {"status": -1, "missatge": f'{e}'}
