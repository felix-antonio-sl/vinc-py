import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class Config:
    """Configuración base"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-prod')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    ALLOWED_ORIGINS = os.getenv('ALLOWED_ORIGINS', '').split(',')

class DevelopmentConfig(Config):
    """Configuración de desarrollo"""
    DEBUG = True
    DEVELOPMENT = True

class ProductionConfig(Config):
    """Configuración de producción"""
    DEBUG = False
    DEVELOPMENT = False

# Diccionario de configuraciones
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# Obtener configuración activa
def get_config():
    """Obtener configuración según ambiente"""
    env = os.getenv('FLASK_ENV', 'development')
    return config.get(env, config['default']) 