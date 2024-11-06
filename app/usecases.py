from app.adapters.Mongo_Adapter import MongoAdapter
from app.core.models import SensorData, AguaRequest
from app.adapters.Gemini_Adapter import GeminiAdapter
from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AgriculturaPrecisionService:
    def __init__(self, mongo_adapter: MongoAdapter, gemini_adapter: GeminiAdapter):
        self.mongo_adapter = mongo_adapter
        self.gemini_adapter = gemini_adapter


    def __del__(self):
        if hasattr(self, "client"):
            self.client.close()


    #Metodo para colectar los datos de los sensores
    def get_sensor_data(self):
        try:
            sensor_data_json = self.mongo_adapter.collect_sensor_data()
            return sensor_data_json
        except Exception as e:
            raise Exception(f"Error al procesar los datos del sensor: {str(e)}")
        
    #Metodo para guardar la data del ESP32
    def save_sensor_data(self, data: SensorData):
        data_save = self.mongo_adapter.save_sensor_data(data)
        if data_save is None:
            return "Los campos no pueden ser nulos."
        if data_save:
            return "Los datos se han guardado exitosamente"
        return "Error al guardar los datos"
        

    #Metodo para obtener recomendaciones
    def process_prompt(self, prompt: str):
        try:
            response = self.gemini_adapter.process_prompt(prompt)
            return response
        except Exception as e:
            raise Exception(f"Error al procesar el prompt en Gemini: {str(e)}")
        

    #Metodo para calcular la cantidad de agua en litros    
    def calcular_cantidad_agua(self, data:AguaRequest):
        try:
            print("Datos recibidos para calcular:", data)
            area = data.area
            temperatura = data.temperatura
            humedad_aire = data.humedad_aire
            humedad_suelo = data.humedad_suelo
            res = area * ((0.1*temperatura) - (0.05* (humedad_aire/100)) + (10*(1-(humedad_suelo/100))))
            return res
        except Exception as e:
            raise Exception(f"Error al calcular la cantidad de agua en litros")
           

        

