from fastapi import APIRouter, Depends, HTTPException
from app.api import dependencies
from app.usecases import AgriculturaPrecisionService
from app.core.models import PromptRequest, SensorData

#Enrutador
router = APIRouter()

#Endpoint para obtener los datos del sensor
@router.get("/sensor-data")
def get_sensor_data(
    Agricultura_service: AgriculturaPrecisionService = Depends(dependencies.AgriculturaPrecisionSingleton.get_instance)
):
    try:
        data = Agricultura_service.get_sensor_data()
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

#Endpoint para calcular la cantidad de agua en litros
@router.post("/cantidad")
def get_cantidad_agua(
    data = SensorData,
    Agricultura_service: AgriculturaPrecisionService = Depends(dependencies.AgriculturaPrecisionSingleton.get_instance)
):
    try:
        response = Agricultura_service.calcular_cantidad_agua(data)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

#Endpoint para obtener recomendaciones de gemini    
@router.post("/generar_respuesta")
def process_prompt(
    prompt_request: PromptRequest,
    Agricultura_service: AgriculturaPrecisionService = Depends(dependencies.AgriculturaPrecisionSingleton.get_instance)
):
    try:
        # Llama al servicio para procesar el prompt
        response = Agricultura_service.process_prompt(prompt_request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
