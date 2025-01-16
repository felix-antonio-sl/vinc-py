import os
import uuid
import openai
from app.models.chat import ChatSession, ChatMessage
from app.models import db

class ChatService:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.context = self._load_context_files()

    def _load_context_files(self):
        """Cargar archivos de contexto"""
        context = ""
        files = [
            "recursos/punto-de-partida.txt",
            "recursos/resumen-instructivo.txt"
        ]
        
        for file_path in files:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    context += file.read() + "\n\n"
            except Exception as e:
                print(f"Error al cargar {file_path}: {str(e)}")
        
        return context

    def create_session(self):
        """Crear nueva sesión de chat"""
        session = ChatSession(session_id=str(uuid.uuid4()))
        db.session.add(session)
        db.session.commit()
        return session

    def get_session(self, session_id):
        """Obtener sesión existente"""
        return ChatSession.query.filter_by(session_id=session_id).first()

    def process_message(self, session_id, user_message):
        """Procesar mensaje del usuario y obtener respuesta"""
        session = self.get_session(session_id)
        if not session:
            session = self.create_session()

        # Guardar mensaje del usuario
        user_msg = ChatMessage(
            session_id=session.id,
            role='user',
            content=user_message
        )
        db.session.add(user_msg)

        # Preparar el historial de mensajes para OpenAI
        messages = [
            {
                "role": "system",
                "content": f"""Eres un asistente experto en el Concurso de Vinculación con la Comunidad 8% FNDR 2024. 
                Tu función es ayudar con consultas sobre la rendición de cuentas basándote en el siguiente contexto:

                {self.context}

                Responde de manera clara, precisa y en español. Si no estás seguro de algo, indícalo.
                """
            }
        ]

        # Agregar historial de mensajes previos
        for msg in session.messages[-5:]:  # Últimos 5 mensajes para contexto
            messages.append({
                "role": msg.role,
                "content": msg.content
            })

        # Agregar mensaje actual
        messages.append({
            "role": "user",
            "content": user_message
        })

        try:
            # Obtener respuesta de OpenAI
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )

            # Extraer respuesta
            assistant_response = response.choices[0].message.content

            # Guardar respuesta del asistente
            assistant_msg = ChatMessage(
                session_id=session.id,
                role='assistant',
                content=assistant_response
            )
            db.session.add(assistant_msg)
            db.session.commit()

            return {
                'session_id': session.session_id,
                'response': assistant_response
            }

        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error al procesar mensaje: {str(e)}")

    def get_chat_history(self, session_id):
        """Obtener historial de chat"""
        session = self.get_session(session_id)
        if not session:
            return None
        return [msg.to_dict() for msg in session.messages] 