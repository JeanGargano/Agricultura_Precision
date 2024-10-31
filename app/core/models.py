from typing import Optional

from pydantic import BaseModel

class SensorData(BaseModel):
    temperatura: Optional[int] = None
    humedad_R: Optional[float] = None
    humedad: Optional[float] = None

class PromptRequest(BaseModel):
    prompt: str 

   


