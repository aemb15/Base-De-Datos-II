import sys
import os
dirname = os.path.dirname("proyecto")
sys.path.append(dirname)
sys.path.append(dirname + "/db_models/")


from pymongo import MongoClient
from bson.objectid import ObjectId
from config_vars import MONGODB_CONNECTION
from cancha import cancha

class disponibilidad:
    print("Connecting to MongoDB")
    client = MongoClient(MONGODB_CONNECTION)
    db = client['Turno']  # Nombre de la base de datos
    collection = db['disponibilidad']  # Nombre de la Collecion en MongoDB
    collection2 = db['cancha']
    print("Connection established")

    def insertar_disponibilidad(cls, idCancha,fecha, hora, disponible):
        """
        Agregar una nueva disponibilidad a la coleccion
        """
        disponibilidad_data = ({
            "_id": _id,
            "canchaRef":{
                "$ref": "cancha",
                "$_id": ObjectId(_id)
            },
            "fecha": fecha,
            "hora": hora,
            "disponibilidad": disponible
        })
        resultado = cls.collection.insert_one(disponibilidad_data)