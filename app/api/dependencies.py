from app.adapters.Mongo_Adapter import MongoAdapter
from app.adapters.Gemini_Adapter import GeminiAdapter
from app import usecases

class AgriculturaPrecisionSingleton:
    _instance = None

    @classmethod
    def get_instance(cls) -> usecases.AgriculturaPrecisionService:
        if cls._instance is None:

            #inicializa el cliente de MongoDB
            mongo_adapter = MongoAdapter()
            gemini_adapter = GeminiAdapter()


            # Crea la instancia de Agricultura de precision service
            cls._instance = usecases.AgriculturaPrecisionService(
                mongo_adapter=mongo_adapter,
                gemini_adapter = gemini_adapter
                
            )
        return cls._instance
