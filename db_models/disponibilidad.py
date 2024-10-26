import sys
import os
dirname = os.path.dirname("proyecto")
sys.path.append(dirname)
sys.path.append(dirname + "/db_models/")


from pymongo import MongoClient
from bson.objectid import ObjectId
from config_vars import MONGODB_CONNECTION
from db_models.cancha import cancha

class disponibilidad:
    print("Connecting to MongoDB")
    client = MongoClient(MONGODB_CONNECTION)
    db = client['Turno']  # Nombre de la base de datos
    collection = db['disponibilidad']  # Nombre de la Collecion en MongoDB
    collection2 = db['cancha'] 
    print("Connection established")

 
    @classmethod
    def insertar_disponibilidad(cls,_id, _idCancha,fecha,hora,estadoCancha):
        
        cancha_info = cls.collection2.find_one({"_id": _idCancha})
        disponibilidad_data = {
            "_id": _id,
            "fecha": fecha,
            "hora": hora,
            "estadoCancha": estadoCancha,
            "nombre": cancha_info["nombre"],
            "tipo_superficie": cancha_info["tipo_superficie"]
        }
        resultado = cls.collection.insert_one(disponibilidad_data)
        return resultado.inserted_id
    

    @classmethod
    def consultar_disponibilidad_hora(cls, hora):
        """
        Obtener la disponibilidad de la cancha
        """
        return cls.collection.find_one({"hora": hora})


    @classmethod
    def consultar_disponibilidad__estado(cls, estadoCancha):
        """
        Obtener la disponibilidad de la cancha por el estado
        """
        return cls.collection.find_one({"estadoCancha": estadoCancha})


    @classmethod
    def consultar_disponibilidad(cls):
        """
        Obtener todas las disponibilidad de la colección.
        """
        return list(cls.collection.find({}))
    

    @classmethod
    def actualizar_disponibilidad(cls,_id, _idCancha = None,fecha = None,hora = None,estadoCancha = None):
        """
        Actualizar una disponibilidad
        """
        update_data = {}
        if _idCancha:
            update_data["_idCancha"] = _idCancha
        if fecha:
            update_data["fecha"] = fecha
        if hora:
            update_data["hora"] = hora
        if estadoCancha:
            update_data["estadoCancha"] = estadoCancha

        resultado = cls.collection.update_one({"_id":_id},{"$set": update_data})
        return resultado.modified_count
