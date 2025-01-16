from flask import Flask, render_template
from config import get_config
from app.api.chat import chat_bp
from app.services.chat_service import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())
    
    # Inicializar la base de datos
    db.init_app(app)
    
    # Registrar blueprints
    app.register_blueprint(chat_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return render_template('chat.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run() 