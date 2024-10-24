import sys
import os
dirname = os.path.dirname("proyecto")
sys.path.append(dirname)
sys.path.append(dirname + "/db_models/")


from pymongo import MongoClient
from bson.objectid import ObjectId
from config_vars import MONGODB_CONNECTION

class cancha:
    print("Connecting to MongoDB")
    client = MongoClient(MONGODB_CONNECTION)
    db = client['Turno']  # Nombre de la base de datos
    collection = db['cancha']  # Nombre de la Collecion en MongoDB
    print("Connection established")

    @classmethod
    def insertar_cancha(cls, _id, nombre, tipo_superficie):
        """
        Agregar una nueva cancha a la colección.
        """
        cancha_data = {
            "_id": _id,
            "nombre": nombre,
            "tipo_superficie": tipo_superficie,
        }
        return cls.collection.insert_one(cancha_data)



    @classmethod
    def consultar_cancha_por_nombre(cls, nombre):
        """
        Obtener una cancha por su nombre.
        """
        return cls.collection.find_one({"nombre": nombre})
    

    @classmethod
    def consultar_cancha_por_id(cls, _id):
        """
        Obtener una cancha por id
        """
        return cls.collection.find_one({"_id":_id})
    

    @classmethod
    def consultar_cancha_por_tipoSuperficie(cls, tipo_superficie):
        """
        Obtener una lista de cancha por tipo de superficie
        """
        canchas_sinteticas = cls.collection.find({"tipo_superficie": tipo_superficie})
        for cancha in canchas_sinteticas:
            print(f"ID: {cancha['_id']}, Nombre: {cancha['nombre']}, Tipo de Superficie: {cancha['tipo_superficie']}")

    


    @classmethod
    def consultar_canchas(cls):
        """
        Obtener todas las canchas de la colección.
        """
        return list(cls.collection.find({}))
    

    @classmethod
    def actualizar_cancha(cls, _id, nombre = None, tipo_superficie = None):
        """
        Actualizar una cancha
        """
        update_data = {}
        if nombre:
            update_data["nombre"] = nombre
        if tipo_superficie:
            update_data["tipo_superficie"] = tipo_superficie

        resultado = cls.collection.update_one({"_id":_id},{"$set": update_data})
        return resultado.modified_count


    