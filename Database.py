__author__ = 'Kauser'

import pymongo


# Database Class

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    # metodos estaticos de la propia clase
    # estos metodos no necesitan retornar nada por que uno Inicializa = initialize() la base de datos LLamada 'fullstack',
    # en el servidor de MongoDB local.

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    # este metodo tambien no retorna , carga informacion en la base 'fullstack' en MongoDB

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    # en estos metodos como son de busqueda deben retornar el resultado de la query enviada

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)


