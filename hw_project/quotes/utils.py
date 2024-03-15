from pymongo import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb+srv://Valerii:Peremoga2024@cluster1.3egn3sy.mongodb.net/?retryWrites=true&w=majority"

def get_mongodb():
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.hw
    return db
