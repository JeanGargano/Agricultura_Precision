from Model.Models import User  
from Service.IUser_Service import IUser_Service  
from db_conection import DatabaseConnection 
from typing import List

class IUser_ServiceImp(IUser_Service): 
    def __init__(self):
        self.db_connection = DatabaseConnection() 

    async def save_user(self, user: User) -> User:
        user_dict = user.dict() 
        result = self.db_connection.collection.insert_one(user_dict)  
        user.id = result.inserted_id
        return user




