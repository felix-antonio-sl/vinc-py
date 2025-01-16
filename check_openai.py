from openai import OpenAI
import os
from dotenv import load_dotenv

def main():
    # Cargar variables de entorno
    load_dotenv()
    
    try:
        # Inicializar el cliente de OpenAI
        client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
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
        print("ID de la solicitud:", response._request_id)
        
    except Exception as e:
        print(f"Error al conectarse a OpenAI: {str(e)}")

if __name__ == "__main__":
    main()