# src/adapters/MysqlMicroAdapter.py
from core.models import SensorData
from app.core.ports import MicroInterface
import subprocess  # Para ejecutar el módulo de C++
from pymongo import MongoClient
from pymongo.errors import PyMongoError

class MongoMicroAdapter(MicroInterface):
    def __init__(self):
        try:
            self.client = MongoClient("mongodb+srv://jean:root@bd2.evaabnw.mongodb.net/")
            self.db = self.client['SMC']
            self.collection = self.db['Microcontrolador']
        except PyMongoError as e:
            print(f"Error connecting to MongoDB: {e}")
            raise

    #Cerrando la conexion
    def __del__(self):
        if hasattr(self, 'client'):
            self.client.close()


    #Metodos
    def save_sensor_data(self, humedad: float, humedad_relativa: float, temperatura: float):
        try:
            nuevo_dato = SensorData(
                humedad=humedad,
                humedad_relativa=humedad_relativa,
                temperatura=temperatura
            )
            self.session.add(nuevo_dato)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Error al guardar los datos del sensor: {str(e)}")
        finally:
            self.session.close()

    def collect_sensor_data(self):
        # Suponiendo que tu módulo de C++ es un ejecutable que devuelve los datos en formato JSON
        try:
            result = subprocess.run(["path/to/your_cpp_module"], capture_output=True, text=True)
            if result.returncode != 0:
                raise Exception(f"Error en el módulo de C++: {result.stderr}")
            data = result.stdout
            return data
        except Exception as e:
            raise Exception(f"Error al recolectar datos del sensor: {str(e)}")
        

