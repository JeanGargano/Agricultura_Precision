from fastapi import APIRouter, HTTPException
from Model.Models import User  
from Service.IUser_ServiceImp import IUser_ServiceImp 

router = APIRouter()
user_service = IUser_ServiceImp() 

# Endpoint para guardar usuario
@router.post("/user/", response_model=User)
async def create_user(user: User):
    try:
        saved_user = await user_service.save_user(user) 
        return saved_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



