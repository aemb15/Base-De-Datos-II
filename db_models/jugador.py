import sys
import os
dirname = os.path.dirname("proyecto")
sys.path.append(dirname)
sys.path.append(dirname + "/db_models/")
#sys.path.append("/home/andres/Escritorio/proyecto/")
#sys.path.append(dirname + "/db_models/")

#print(sys.path)
from pymongo import MongoClient
from bson.objectid import ObjectId
from config_vars import MONGODB_CONNECTION



class jugador:
    #def __init__(self):
    print("Cargando configuracion de jugador")
    client = MongoClient(MONGODB_CONNECTION)
    db = client['Turno']  # Replace with your database name
    collection = db['jugador']  # Collection name in MongoDB
    print("Configuracion finalizada")
            
    #collection = db['jugador'] #Coleccion jugador dentro de la base de datos

    @classmethod
    def insertar_jugador(cls, nombre, telefono):
        """
        Insertar un nuevo documento jugador con nombre y telefono
        """
        jugador_data = {
            "nombre": nombre, 
            "telefono": telefono
        }
        result = cls.collection.insert_one(jugador_data)
        return result.inserted_id
    

    @classmethod
    def consultar_jugador(cls, jugador_id):
        """
        Obtener un documento del jugador por su ID
        """
        jugador = cls.collection.find_one({"_id": ObjectId(jugador_id)})
        return jugador
    

    @classmethod
    def consultar_jugadores(cls):
        """
        Obtener todos los documentos de los jugadores
        """
        jugador = list(cls.collection.find())
        return jugador
    
    @classmethod
    def consultar_por_nombre_jugador(cls, nombre):
        """
        Obtener un documento de jugador por su nombre
        """
        jugador = cls.collection.find_one({"nombre": nombre})
        return jugador
    
    @classmethod
    def actualizar_jugador(cls, jugador_id, nombre=None, telefono=None):
        """
        Actualizar un documento jugador por su ID
        """
        update_data = {}
        if nombre:
            update_data["nombre"] = nombre
        if telefono:
            update_data["telefono"] = telefono
        
        result = cls.collection.update_one({"_id":ObjectId(jugador_id)},{"$set": update_data})
        return result.modified_count

