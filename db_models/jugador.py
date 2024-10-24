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
    print("")
    print(db.list_collection_names())
    print("")
    print(collection)
    print("Configuracion finalizada")
            
    #collection = db['jugador'] #Coleccion jugador dentro de la base de datos

    @classmethod
    def insertar_jugador(cls, _id, nombre, telefono):
        """
        Insertar un nuevo documento jugador con nombre y telefono
        """
        jugador_data = {
            "_id":_id,
            "nombre": nombre, 
            "telefono": telefono
        }
        #result = cls.collection.insert_one({"nombre":nombre,"telefono":telefono})
        result = cls.collection.insert_one(jugador_data)
        return result
        #return result.inserted_id
        #cls.collection.insert_one(jugador_data)
        #cls.collection.insert_one(jugador_data)

    

    @classmethod
    def consultar_jugador(cls, _id):
        """
        Obtener un documento del jugador por su ID
        """
        jugador = cls.collection.find_one({"_id": _id})
        return jugador
    
    
    @classmethod
    def consultar_jugadores(cls):
        """
        Obtener todos los documentos de los jugadores
        """
        jugador = list(cls.collection.find())
        return jugador
    

    '''
    @classmethod
    def consultar_jugadores(self):
        """
        Obtener todos los documentos de los jugadores
        """
        for jugador in self.collection.find():
            print(jugador)
        #jugador = list(cls.collection.find())
        #return jugador
    '''
    
    @classmethod
    def consultar_por_nombre_jugador(cls, nombre):
        """
        Obtener un documento de jugador por su nombre
        """
        #for jugador in cls.collection.find_one({"nombre": nombre}):
        #    print(jugador)
        jugador = csl.collection.find_one({"nombre": nombre})
        return jugador
    
    @classmethod
    def consultar_jugador_por_telefono(cls, telefono):
        """
        Obtener un jugador por su número de teléfono.
        """
        jugador = cls.collection.find_one({"telefono": telefono})
        return jugador

    @classmethod
    def actualizar_jugador(cls, _id, nombre=None, telefono=None):
        """
        Actualizar un documento jugador por su ID
        """
        update_data = {}
        if nombre:
            update_data["nombre"] = nombre
        if telefono:
            update_data["telefono"] = telefono
        
        result = cls.collection.update_one({"_id":_id},{"$set": update_data})
        return result.modified_count

