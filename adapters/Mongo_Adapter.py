# src/adapters/MysqlMicroAdapter.py
from core.models import SensorData
from core.ports import MongoInterface
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
                return result
            else:
                return "Error al guardar los datos"
        except PyMongoError as e:
            raise Exception(f"Fallo la conexion a la BD: {str(e)}")

        
    def collect_sensor_data(self):
        try:
            response = requests.get("http://172.20.10.2/sensor-data")
            response.raise_for_status()
            data = response.json()
            return data
        except requests.RequestException as e:
            raise Exception(f"Error al recolectar datos del sensor: {str(e)}")
        
    def get_bd_data(self):
        cursor = self.collection.find({})
        bd_data = [
            {key: value for key, value in doc.items() if key != "_id"}  # Filtramos para excluir _id
            for doc in cursor
        ]
        return bd_data
        


        
            
        

