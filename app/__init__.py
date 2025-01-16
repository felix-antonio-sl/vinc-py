from flask import Flask, render_template
from config import get_config
from app.models import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())
    
    # Inicializar la base de datos
    db.init_app(app)
    
    # Inicializar Flask-Migrate
    migrate = Migrate(app, db)
    
    # Registrar blueprints después de inicializar db
    from app.api.chat import chat_bp
    app.register_blueprint(chat_bp, url_prefix='/api')

    @app.route('/')
    def index():
        return render_template('chat.html')

    return app