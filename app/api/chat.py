from flask import Blueprint, request, jsonify
from ..services.chat_service import ChatService
from flask_cors import cross_origin

chat_bp = Blueprint('chat', __name__)
chat_service = ChatService()

@chat_bp.route('/chat/session', methods=['POST'])
@cross_origin()
def create_session():
    """Crear nueva sesión de chat"""
    try:
        session = chat_service.create_session()
        return jsonify({
            'success': True,
            'session_id': session.session_id
        }), 201
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@chat_bp.route('/chat/message', methods=['POST'])
@cross_origin()
def send_message():
    """Enviar mensaje y obtener respuesta"""
    data = request.get_json()
    
    if not data or 'message' not in data:
        return jsonify({
            'success': False,
            'error': 'Se requiere un mensaje'
        }), 400

    session_id = data.get('session_id')
    message = data['message']

    try:
        response = chat_service.process_message(session_id, message)
        return jsonify({
            'success': True,
            **response
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@chat_bp.route('/chat/history/<session_id>', methods=['GET'])
@cross_origin()
def get_history(session_id):
    """Obtener historial de chat"""
    try:
        history = chat_service.get_chat_history(session_id)
        return jsonify({
            'success': True,
            'history': history
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500 