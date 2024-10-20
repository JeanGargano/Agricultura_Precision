from app.adapters.User_Adapter import MongoUserAdapter
import json
from app.adapters.Micro_Adapter import MongoMicroAdapter
from app.core import models

class Agricultura_Precision_Service:

    #Constructor de agricultura de precision
    def __init__(self, user_Adapter: MongoUserAdapter, micro_Adapter: MongoMicroAdapter):
        self.user_Adapter = user_Adapter
        self.micro_Adapter = micro_Adapter

#------------------------------------------------Metodos para el micro--------------------------

    def save_sensor_data(self):
        try:
            # Recolecta datos del sensor
            sensor_data_json = self.micro_Adapter.collect_sensor_data()
            sensor_data = json.loads(sensor_data_json)
            
            # Guarda los datos en la base de datos
            self.micro_Adapter.save_sensor_data(
                humedad=sensor_data['humedad'],
                humedad_relativa=sensor_data['humedad_relativa'],
                temperatura=sensor_data['temperatura']
            )

            return sensor_data 
        except Exception as e:
            raise Exception(f"Error al procesar los datos del sensor: {str(e)}")
        
#-----------------------------------Metodos para usuario----------------------------------

    def registrar_usuario(self, user: models.User):
        try:
            saved_user = self.user_Adapter.save_user(user)
            if saved_user is None:
                    return "Los campos no pueden ser nulos."
            if saved_user:
                return "El usuario se ha guardado exitosamente."
            return "Error al guardar el usuario."
        except Exception as e:
            raise Exception(f"Error al registrar usuario: {str(e)}")
