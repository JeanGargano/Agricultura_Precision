from abc import ABC, abstractmethod

    
class MongoInterface(ABC):
    
    @abstractmethod
    def save_sensor_data(self):
        "Guarada los datos de los sensores"
        pass
    
    @abstractmethod
    def collect_sensor_data(self):
        """Obtiene los datos del sensor"""
        pass

    @abstractmethod
    def get_bd_data(self):
        "Obtiene los datos de la base de datos"
        pass


    
class GeminiInterface(ABC):
    @abstractmethod
    def process_prompt(self):
        "Procesa el prompt para generar una respuesta"
        pass