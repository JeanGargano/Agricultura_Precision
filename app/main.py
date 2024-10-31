from fastapi import FastAPI
from app.api.routers import router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv 
import os


load_dotenv() 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
