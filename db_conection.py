from pymongo import MongoClient
from pymongo.errors import PyMongoError

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            try:
                cls._instance.client = MongoClient("mongodb+srv://jean:root@bd2.evaabnw.mongodb.net/")
                cls._instance.db = cls._instance.client['SMC']
                cls._instance.collection = cls._instance.db['User']
                print("Conexión a MongoDB establecida exitosamente.")
            except PyMongoError as e:
                print(f"Error conectando a MongoDB: {e}")
                raise
        return cls._instance

    def close(self):
        """Cierra la conexión a la base de datos."""
        if hasattr(self, 'client'):
            self.client.close()
            print("Conexión a MongoDB cerrada exitosamente.")
