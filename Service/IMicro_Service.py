from abc import ABC, abstractmethod
from Model import Models

class MicroService(ABC):

    #Guardar Micro
    @abstractmethod
    def Save_Micro(self, user: Models.Micro) -> None:
        pass
