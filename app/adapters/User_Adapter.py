# src/adapters/MysqlUserAdapter.py
from app.core import models
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from http.client import HTTPException
from typing import Optional
from app.core.ports import UserInterface

class MongoUserAdapter(UserInterface):

    def __init__(self):
        try:
            self.client = MongoClient("mongodb+srv://jean:root@bd2.evaabnw.mongodb.net/")
            self.db = self.client['SMC']
            self.collection = self.db['User']
        except PyMongoError as e:
            print(f"Error connecting to MongoDB: {e}")
            raise 

    #Cerrando la conexion
    def __del__(self):
        if hasattr(self, 'client'):
            self.client.close()


    def save_user(self, user: models.User) -> Optional[models.User]:
        try:
            user_data = user.dict(by_alias=True)
            result = self.collection.insert_one(user_data)
            if result.inserted_id:
                return user
        except PyMongoError as e:
            raise HTTPException(status_code=500, detail=f"Error saving user: {e}")
