from datetime import datetime
from typing import Optional  # Import Optional for nullable fields

from pydantic import BaseModel

class FechaHora(BaseModel):
    fecha: datetime = datetime.now()  # Capture current datetime by default
    año: Optional[int] = None  # Make year optional for flexibility
    mes: Optional[int] = None  # Make month optional for flexibility
    dia: Optional[int] = None  # Make day optional for flexibility
    hora: Optional[int] = None  # Make hour optional for flexibility

    def __init__(self, **data):  # Override __init__ to handle optional fields
        super().__init__(**data)
        self.año = self.fecha.year if self.fecha else None
        self.mes = self.fecha.month if self.fecha else None
        self.dia = self.fecha.day if self.fecha else None
        self.hora = self.fecha.hour if self.fecha else None

class SensorData(BaseModel):
    temperatura: float
    humedad_aire: float
    humedad_suelo: float
    tiempo: FechaHora = FechaHora()  # Automatically create FechaHora on instance creation

class PromptRequest(BaseModel):
    prompt: str 

#Esquema para datos de entrada del metodo calcular agua en litros
class AguaRequest(BaseModel):
    area: float
    temperatura: float
    humedad_aire: float
    humedad_suelo: float

   


