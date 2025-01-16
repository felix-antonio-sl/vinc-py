from openai import OpenAI
import os
from dotenv import load_dotenv

def main():
    # Cargar variables de entorno
    load_dotenv()
    
    try:
        # Inicializar el cliente de OpenAI
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        if not os.getenv('OPENAI_API_KEY'):
            raise ValueError("No se encontró la API key de OpenAI")
            
        # Realizar una prueba simple de chat completion
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": "Di hola mundo como prueba"
            }]
        )
        
        print("Conexión exitosa!")
        print("Respuesta del modelo:", response.choices[0].message.content)
        
    except ValueError as e:
        print(f"Error de configuración: {str(e)}")
    except Exception as e:
        print(f"Error al conectarse a OpenAI: {str(e)}")

if __name__ == "__main__":
    main()