# src/adapters/MysqlMicroAdapter.py
from core.models import SensorData
from app.core.ports import MicroInterface
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from http.client import HTTPException
from typing import Optional
import subprocess
import requests

class MongoAdapter(MicroInterface):
    def __init__(self):
        try:
            self.client = MongoClient("mongodb+srv://jean:root@bd2.evaabnw.mongodb.net/")
            self.db = self.client['SMC']
            self.collection = self.db['Microcontrolador']
        except PyMongoError as e:
            print(f"Error connecting to MongoDB: {e}")
            raise

    #Cerrando la conexion
    def __del__(self):
        if hasattr(self, 'client'):
            self.client.close()


#------------------------------------------Metodos para el microcontrolador------------------------------
    def save_sensor_data(self, humedad: float, humedad_relativa: float, temperatura: float):
        try:
            nuevo_dato = SensorData(
                humedad=humedad,
                humedad_relativa=humedad_relativa,
                temperatura=temperatura
            )
            self.session.add(nuevo_dato)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Error al guardar los datos del sensor: {str(e)}")
        finally:
            self.session.close()

    def collect_sensor_data(self):
        try:
            response = requests.get("http://192.168.39.129/data")
            response.raise_for_status()  # Lanza un error si el estado no es 200
            data = response.json()
            return data
        except requests.RequestException as e:
            raise Exception(f"Error al recolectar datos del sensor: {str(e)}")
            
        

