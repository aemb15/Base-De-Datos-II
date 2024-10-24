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
