from typing import Optional

from pydantic import BaseModel

class SensorData(BaseModel):
    temperatura: float
    humedad_aire: float
    humedad_suelo: float

class PromptRequest(BaseModel):
    prompt: str 

#Esquema para datos de entrada del metodo calcular agua en litros
class AguaRequest(BaseModel):
    area: float
    temperatura: float
    humedad_aire: float
    humedad_suelo: float

   


