from abc import ABC, abstractmethod
from Model.Models import User
from typing import List

class IUser_Service(ABC):
    @abstractmethod
    async def save_user(self, user: User) -> User:
        pass

