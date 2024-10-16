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

class reserva:
    #def __init__(self):
    print("Connecting to MongoDB")
    client = MongoClient(MONGODB_CONNECTION)
    db = client['Turno']  # Nombre de la base de datos
    collection = db['jugador']  # Nombre de la Collecion en MongoDB
    print("Connection established")

    @classmethod
    def insertar_reserva(cls, idJugador, idCancha, fecha, horaInicio, horaFin, estado):
        """
        Agregar una nueva cancha a la colección.
        """
        reserva_data = {
            "idJugador" = ObjectId(idJugador),
            "idCnacha" = ObjectId(idCancha),
            "fecha" = fecha,
            "horaInicio" = horaInicio,
            "horaFin" = horaFin,
            "estado" = estado
        }
        result = cls.collection.insert_one(reserva_data)

    @classmethod
    def consultar_reserva(cls, reserva_id):
        """
        Obtener un documento de la reserva por su ID
        """
        reserva = cls.collection.find_one({"_id": ObjectId(reserva_id)})

    @classmethod
    def consultar_reservas(cls):
        """
        Obtener todos los documentos de las reservas
        """
        reservas = list(cls.collection.find())
        return reservas

    
    @classmethod
    def actualizar_reservas(cls, reserva_id, fecha, horaInicio, horaFin, estado):
        """
        Actualizar un documento reserva por su ID
        """
        update_data = {}
        if fecha:
            update_data["fecha"] = fecha
        if horaInicio:
            update_data["horaInicio"] = horaInicio
        if horaFin:
            update_data["horaFIn"] = horaFin
        if estado:
            update_data["estado"] = estado

        result = cls.collection.update_one({"_id":ObjectId(reserva_id)},{"$set": update_data})
        return result.modified_count
