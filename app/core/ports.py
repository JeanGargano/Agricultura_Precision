from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def save_user(self, nombre: str, email: str, password: str):
        """Guarda un nuevo usuario en el sistema"""
        pass
    
class MicroInterface(ABC):
    @abstractmethod
    def save_sensor_data(self, humedad: float, humedad_relativa: float, temperatura: float):
        """Guarda los datos del sensor en el sistema"""
        pass

    @abstractmethod
    def collect_sensor_data(self):
        """Obtiene los datos del sensor"""
        pass
