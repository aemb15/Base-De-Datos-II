import sys
import os
dirname = os.path.dirname("proyecto")
sys.path.append(dirname)
sys.path.append(dirname + "/db_models/")
#sys.path.append("/home/andres/Escritorio/proyecto/")
#sys.path.append(dirname + "/db_models/")

print(sys.path)
from pymongo import MongoClient
from bson.objectid import ObjectId
from config_vars import MONGODB_CONNECTION

class cancha:
    #def __init__(self):
    print("Connecting to MongoDB")
    client = MongoClient(MONGODB_CONNECTION)
    db = client['Turno']  # Nombre de la base de datos
    collection = db['cancha']  # Nombre de la Collecion en MongoDB
    print("Connection established")

    @classmethod
    def insertar_cancha(cls, nombre, tipo_superficie, disponibilidad):
        """
        Agregar una nueva cancha a la colección.
        """
        cancha_data = {
            "nombre": nombre,
            "tipo_superficie": tipo_superficie,
            "disponibilidad": disponibilidad
        }
        result = cls.collection.insert_one(cancha_data)
        print(f"Cancha agregada con ID: {result.inserted_id}")

    @classmethod
    def consultar_cancha(cls, nombre):
        """
        Busca una cancha por su nombre.
        """
        return cls.collection.find_one({"nombre": nombre})
    
    @classmethod
    def consultar_canchas(cls):
        """
        Obtener todas las canchas de la colección.
        """
        canchas = list(cls.collection.find({}))
        return canchas

    