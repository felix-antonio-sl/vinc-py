from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from app.models import db
from app.api.chat import chat_bp
from config import get_config

def create_app():
    """Crear y configurar la aplicación Flask"""
    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object(get_config())
    
    # Configurar CORS
    CORS(app, resources={
        r"/api/*": {
            "origins": app.config['ALLOWED_ORIGINS'],
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type"]
        }
    })
    
    # Inicializar extensiones
    db.init_app(app)
    Migrate(app, db)
    
    # Registrar blueprints
    app.register_blueprint(chat_bp, url_prefix='/api')
    
    @app.route('/health')
    def health_check():
        return {'status': 'healthy'}, 200
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000) 