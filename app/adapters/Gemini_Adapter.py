import google.generativeai as genai
import os
from app.core.ports import GeminiInterface

class GeminiAdapter(GeminiInterface):
    def __init__(self):
    
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("API_KEY no está configurada. Asegúrate de definirla en el archivo .env.")
        genai.configure(api_key=api_key) 
        print(f"API_KEY cargada en GeminiAdapter: {api_key}")
        # Inicializa el modelo
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def process_prompt(self, prompt: str):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Error al consultar la API de Gemini: {str(e)}")
