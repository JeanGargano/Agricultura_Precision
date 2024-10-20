from app.adapters.Micro_Adapter import MongoMicroAdapter
from app.adapters.User_Adapter import MongoUserAdapter
from app import usecases

class AgriculturaPrecisionSingleton:
    _instance = None

    @classmethod
    def get_instance(cls) -> usecases.Agricultura_Precision_Service:
        if cls._instance is None:

            # Inicializa adaptador de usuario
            user_Adapter = MongoUserAdapter()

            # Inicializa el cliente ChromaDB
            micro_Adapter = MongoMicroAdapter()

            # Crea la instancia de Agricultura de precision service
            cls._instance = usecases.Agricultura_Precision_Service(
                user_Adapter=user_Adapter,
                micro_Adapter=micro_Adapter,
            )
        return cls._instance
