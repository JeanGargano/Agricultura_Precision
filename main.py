from fastapi import FastAPI
from Controller.Endpoints import router
import uvicorn

app = FastAPI()

app.include_router(router) 

if __name__ == "__main__":  # Asegúrate de incluir los dos puntos aquí
    uvicorn.run(app, host="0.0.0.0", port=8001)

