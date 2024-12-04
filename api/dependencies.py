from adapters.Mongo_Adapter import MongoAdapter
from adapters.Gemini_Adapter import GeminiAdapter
from usecases import AgriculturaPrecisionService

class AgriculturaPrecisionSingleton:
    _instance = None

    @classmethod
    def get_instance(cls) -> AgriculturaPrecisionService:
        if cls._instance is None:

            #inicializa el cliente de MongoDB
            mongo_adapter = MongoAdapter()
            gemini_adapter = GeminiAdapter()


            # Crea la instancia de Agricultura de precision service
            cls._instance = AgriculturaPrecisionService(
                mongo_adapter=mongo_adapter,
                gemini_adapter = gemini_adapter
                
            )
        return cls._instance
