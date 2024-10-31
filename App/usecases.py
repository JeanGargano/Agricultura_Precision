from app.adapters.Mongo_Adapter import MongoAdapter
import json
from app.core import models
import google.generativeai as genai
import os

from app.adapters.Gemini_Adapter import GeminiAdapter


class AgriculturaPrecisionService:
    def __init__(self, mongo_adapter: MongoAdapter, gemini_adapter: GeminiAdapter):
        self.mongo_adapter = mongo_adapter
        self.gemini_adapter = gemini_adapter


    #Metodo para colectar los datos de los sensores
    def get_sensor_data(self):
        try:
            sensor_data_json = self.mongo_adapter.collect_sensor_data()
            return sensor_data_json
        except Exception as e:
            raise Exception(f"Error al procesar los datos del sensor: {str(e)}")
        

    #Metodo para obtener recomendaciones
    def process_prompt(self, prompt: str):
        try:
            response = self.gemini_adapter.process_prompt(prompt)
            return response
        except Exception as e:
            raise Exception(f"Error al procesar el prompt en Gemini: {str(e)}")
        

    #Metodo para calcular la cantidad de agua en litros    
    def calcular_cantidad_agua(self, data:models.SensorData):
        try:
            temperatura = data.temperatura
            humedadR = data.humedad_R
            humedad = data.humedad
            res = ((temperatura/10) + ((100-humedadR)/100) + ((70-humedad)/100)) * 0.75
            return "La cantidad de agua que necesita el cultivos es: ", res,"litros"
        except Exception as e:
            raise Exception(f"Error al calcular la cantidad de agua en litros: {str(e)}")
