# src/adapters/MysqlMicroAdapter.py
from core.models import SensorData
from app.core.ports import MongoInterface
from pymongo import MongoClient
from pymongo.errors import PyMongoError
import requests

class MongoAdapter(MongoInterface):
    def __init__(self):
        try:
            self.client = MongoClient(
                "mongodb+srv://jean:root@bd2.evaabnw.mongodb.net/"
            )
            self.db = self.client["Agricultura_Precision"]
            self.collection = self.db["Data"]
        except PyMongoError as e:
            print(f"Error connecting to MongoDB: {e}")
            raise

    #Cerrando la conexion
    def __del__(self):
        if hasattr(self, 'client'):
            self.client.close()



    #Metodo para guardar la data obtenida por el microcontrolador
    def save_sensor_data(self, data: SensorData):
        try:
            micro_data = data.dict(by_alias=True)
            result = self.collection.insert_one(micro_data)
            if result:
                return "Se han guardado los datos correctamente"
            else:
                return "No se pudieron guardar los datos, verifique los tipos"
        except PyMongoError as e:
            raise Exception(f"Fallo la conexion a la BD: {str(e)}")

        
    #Metodo para recolectar los datos del microcontrolador
    def collect_sensor_data(self):
        try:
            response = requests.get("http://192.168.39.199/data")
            response.raise_for_status()  # Lanza un error si el estado no es 200
            data = response.json()
            return data
        except requests.RequestException as e:
            raise Exception(f"Error al recolectar datos del sensor: {str(e)}")
        


        
            
        

