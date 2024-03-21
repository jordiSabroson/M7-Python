from pymongo import MongoClient


def client():
    try:
        return MongoClient("mongodb://localhost:27017/").films
    except Exception as e:
        return {"status": -1, "error": f'{e}'}
