import sys
import os
dirname = os.path.dirname(__file__)
sys.path.append(dirname)
sys.path.append(dirname + "/db_models/")

from pymongo import MongoClient
from bson.objectid import ObjectId
from config_vars import MONGODB_CONNECTION

from db_models.jugador import jugador
from db_models.cancha import cancha
from db_models.disponibilidad import disponibilidad
from db_models.reserva import reserva

class turnoDAO:
        #def __init__(self):
    print("Connecting to MongoDB")
    client = MongoClient(MONGODB_CONNECTION)
    #db = client['Turno']  # Nombre de la base de datos
    #collection = db['jugador']  # Nombre de la Collecion en MongoDB
    print("Connection established")

    #a partir de aca los metodos de dao consumiendo los metodos de las clases importadas.

    def test(self):
        print("Hola mundo")

    #jugador
    '''
    def get_jugador(self,jugador_id=None, nombre=None, telefono=None):
        """
        Obtener jugadores de la base de datos en función de varios atributos.
        """
        if jugador_id is not None:
            jugador_data = jugador.consultar_jugador(jugador_id=jugador_id)
        elif nombre is not None:
            jugador_data = jugador.consultar_por_nombre_jugador(nombre=nombre)
        elif telefono is not None:
            jugador_data = jugador.consultar_jugador_por_telefono(telefono=telefono)
        else:
            jugador_data = jugador.consultar_jugadores()
        
        return jugador_data

    '''
        
    def get_jugador(self,jugador_id=None, nombre=None, telefono=None):
        """
        Obtener jugadores de la base de datos en función de varios atributos.
        """
        if jugador_id is not None:
            return jugador.consultar_jugador(jugador_id)
        elif nombre is not None:
            return jugador.consultar_por_nombre_jugador(nombre)
        elif telefono is not None:
            return jugador.consultar_jugador_por_telefono(telefono)
        else:
            return jugador.consultar_jugadores()
        

    #cancha
    def get_cancha(self,cancha_id=None, nombre = None, tipo_superficie = None):
        """
        Obtener canchas de la base de datos en función de varios atributos.
        """
        if cancha_id is not None:
            return cancha.consultar_cancha_por_id(cancha_id)
        elif nombre is not None:
            return cancha.consultar_cancha_por_nombre(nombre)
        elif tipo_superficie is not None:
            return cancha.consultar_cancha_por_tipoSuperficie(tipo_superficie)
        else:
            return cancha.consultar_canchas()

    #disponibilidad
    def get_disponibilidad(self,disponibilidad_id = None, hora = None, estadoCancha = None):

        if hora is not None:
            return disponibilidad.consultar_disponibilidad_hora(hora)
        if estadoCancha is not None:
            return disponibilidad.consultar_disponibilidad__estado(estadoCancha)
        else:
            return disponibilidad.consultar_disponibilidad()