from fastapi import APIRouter, Depends,  HTTPException
from app.api import dependencies
from app.usecases import Agricultura_Precision_Service



router = APIRouter()

@router.post("/registrar_usuario")
async def registrar_usuario(user: dict, Agricultura_service: Agricultura_Precision_Service = Depends(dependencies.AgriculturaPrecisionSingleton.get_instance)):
    mensaje = Agricultura_service.registrar_usuario(user)
    return {"mensaje": mensaje}


@router.get("/sensor-data")
def get_sensor_data():
    Agricultura_service: Agricultura_Precision_Service = Depends(dependencies.AgriculturaPrecisionSingleton.get_instance)
    try:
        data = Agricultura_service.save_sensor_data()  # Llama al método para recolectar y guardar datos
        return data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
