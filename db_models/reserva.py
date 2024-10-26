import sys
import os
dirname = os.path.dirname("proyecto")
sys.path.append(dirname)
sys.path.append(dirname + "/db_models/")


print(sys.path)
from pymongo import MongoClient
from bson.objectid import ObjectId
from config_vars import MONGODB_CONNECTION
from db_models.disponibilidad import disponibilidad
from db_models.jugador import jugador

class reserva:

    print("Connecting to MongoDB")
    client = MongoClient(MONGODB_CONNECTION)
    db = client['Turno']  # Nombre de la base de datos
    collection = db['reserva']  # Nombre de la Collecion en MongoDB
    collection_jugador = db['jugador']
    collection_disponibilidad = db['disponibilidad']
    print("Connection established")

    @classmethod
    def insertar_reserva(cls, _id, idJugador, idDisponibilidad, estadoPago):
        """
        Agregar una nueva reserva
        """
        jugador_dato = cls.collection_jugador.find_one({"_id": idJugador})
        # Verificar que la disponibilidad esté en estado 'disponible'
        disponibilidad_dato = cls.collection_disponibilidad.find_one(
            {"_id": idDisponibilidad, "estadoCancha": "disponible"}
        )
        
        # Si hay disponibilidad, proceder a insertar la reserva
        reserva_data = {
            "_id": _id,
            "nombreJugador": jugador_dato["nombre"], 
            "telefono": jugador_dato["telefono"],
            "nombreCancha": disponibilidad_dato["nombre"],
            "fecha": disponibilidad_dato["fecha"],
            "hora": disponibilidad_dato["hora"],
            "estadoPago": estadoPago
        }
        
        resultado = cls.collection.insert_one(reserva_data)
        return resultado.inserted_id



    @classmethod
    def consultar_reserva_id(cls, _id):
        """
        Obtener la reserva por ID
        """
        return cls.collection.find_one({"_id": _id})


    @classmethod
    def consultar_reservas(cls):
        """
        Obtener todas las reservas
        """
        return list(cls.collection.find({}))
    

    @classmethod
    def consultar_reserva__estado(cls, estadoPago):
        """
        Obtener la reserva por el estado
        """

        reserva_datos = cls.collection.find({"estadoPago": estadoPago})
        for reserva in reserva_datos:
            print(f"ID: {reserva['_id']}, Nombre Jugador: {reserva['nombreJugador']},telefono: {reserva['telefono']},Nombre Cancha: {reserva['nombreCancha']},hora: {reserva['hora']},estado de pago: {reserva['estadoPago']}")

    
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
    

    @classmethod
    def actualizar_reserva(cls,_id, idJugador = None,idDisponibilidad = None,estadoPago = None):
        """
        Actualizar una disponibilidad
        """
        update_data = {}
        if idJugador:
            update_data["idJugador"] = idJugador
        if idDisponibilidad:
            update_data["idDisponibilidad"] = idDisponibilidad
        if estadoPago:
            update_data["estadoPago"] = estadoPago

        resultado = cls.collection.update_one({"_id":_id},{"$set": update_data})
        return resultado.modified_count
