from fastapi import APIRouter, Depends, HTTPException
from api import dependencies
from usecases import AgriculturaPrecisionService
from core.models import PromptRequest, SensorData, AguaRequest
from pydantic import BaseModel

#Enrutador
router = APIRouter()

#Endpoint para guardar los datos del microcontrolador
@router.post("/save")
def post_sensor_data(
    data: SensorData,
    Agricultura_service: AgriculturaPrecisionService = Depends(dependencies.AgriculturaPrecisionSingleton.get_instance)
):
    try:
        response = Agricultura_service.save_sensor_data(data)
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


#Endpoint para obtener los datos del sensor
@router.get("/sensor-data")
def get_sensor_data(
    Agricultura_service: AgriculturaPrecisionService = Depends(dependencies.AgriculturaPrecisionSingleton.get_instance)
):
    try:
        response = Agricultura_service.get_sensor_data()
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

#Endpoint para obtener la data de la BD
@router.get("/data")
async def get_bd_data(
    Agricultura_service: AgriculturaPrecisionService = Depends(dependencies.AgriculturaPrecisionSingleton.get_instance)
):
    try:
        all_sensor_data = Agricultura_service.get_bd_data()
        return all_sensor_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los datos: {str(e)}")
    
    

#Endpoint para calcular la cantidad de agua en litros
@router.post("/cantidad")
def get_cantidad_agua(
    data:AguaRequest,
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
        response = Agricultura_service.process_prompt(prompt_request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
