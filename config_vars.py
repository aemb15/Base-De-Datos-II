import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# URI de conexión a MongoDB Atlas
#MONGODB_CONNECTION = os.getenv('MONGODB_URI')
MONGODB_CONNECTION = "mongodb+srv://BaseDeDatosll:95519794@basededatosll.o8imfl1.mongodb.net/?retryWrites=true&w=majority&appName=BaseDeDatosll"

# Puedes crear el cliente MongoClient aquí si lo deseas
client = MongoClient(MONGODB_CONNECTION, server_api=ServerApi('1'))

print("")
print(client)
print("")
"""
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



try:

    #Obtener la cadena de conexion desde la variable de entorno
    uri = "mongodb+srv://BaseDeDatosll:<95519794>@basededatosll.o8imfl1.mongodb.net/?retryWrites=true&w=majority&appName=BaseDeDatosll"

    #Crear cliente con Server API versión 1
    client = MongoClient(uri,server_api=ServerApi('1'))
    #documents = collection.find()
    #print(documents)
    print("Conexion exitosa")
    client.close()

except Exception as e:
    raise("Error de conexion",e)

"""