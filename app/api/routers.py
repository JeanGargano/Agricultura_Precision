from fastapi import APIRouter, Depends, HTTPException
from app.api import dependencies
from app.usecases import AgriculturaPrecisionService
from app.core.models import PromptRequest

router = APIRouter()

@router.get("/sensor-data")
def get_sensor_data(
    Agricultura_service: AgriculturaPrecisionService = Depends(dependencies.AgriculturaPrecisionSingleton.get_instance)
):
    try:
        data = Agricultura_service.get_sensor_data()
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
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
