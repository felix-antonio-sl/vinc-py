from app import create_app
from app.models import db

def init_database():
    """Inicializar la base de datos"""
    app = create_app()
    
    with app.app_context():
        # Crear todas las tablas
        db.create_all()
        print("Base de datos inicializada correctamente.")

if __name__ == "__main__":
    init_database() 