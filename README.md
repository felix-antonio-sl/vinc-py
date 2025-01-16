# Chatbot FNDR 8% - Asistente de Rendición

Chatbot informativo diseñado para asistir a los beneficiarios del Concurso de Vinculación con la Comunidad 8% FNDR 2024 durante la etapa de rendición.

## Requisitos

- Python 3.8+
- PostgreSQL 12+
- OpenAI API Key

## Instalación

1. Clonar el repositorio:
```bash
git clone <repositorio>
cd vinc-py
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
Crear archivo `.env` con:
```
FLASK_APP=app.py
FLASK_ENV=production
OPENAI_API_KEY=your-api-key-here
DATABASE_URL=postgresql://user:password@localhost:5432/vincdb
SECRET_KEY=your-secret-key-here
ALLOWED_ORIGINS=http://localhost:5000,http://your-domain:5000
```

5. Inicializar base de datos:
```bash
# Crear base de datos en PostgreSQL
createdb vincdb

# Inicializar tablas
python init_db.py
```

## Ejecución

1. Desarrollo:
```bash
flask run
```

2. Producción:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 'app:create_app()'
```

## API Endpoints

### Crear Sesión
```
POST /api/chat/session
Response: { "success": true, "session_id": "..." }
```

### Enviar Mensaje
```
POST /api/chat/message
Body: {
    "session_id": "...",
    "message": "..."
}
Response: {
    "success": true,
    "session_id": "...",
    "response": "..."
}
```

### Obtener Historial
```
GET /api/chat/history/<session_id>
Response: {
    "success": true,
    "history": [...]
}
```

## Estructura del Proyecto

```
vinc-py/
├── .env                      # Variables de entorno
├── app.py                    # Aplicación principal
├── config.py                # Configuración
├── init_db.py              # Script de inicialización de BD
├── requirements.txt        # Dependencias
├── app/
│   ├── api/               # Endpoints de la API
│   ├── models/            # Modelos de la base de datos
│   ├── services/          # Lógica de negocio
│   └── utils/             # Utilidades
├── migrations/            # Migraciones de la base de datos
└── recursos/             # Archivos de contexto
    ├── punto-de-partida.txt
    └── resumen-instructivo.txt
```

## Seguridad

- Las claves API y credenciales sensibles deben configurarse en el archivo `.env`
- En producción, usar HTTPS
- Configurar correctamente CORS en `ALLOWED_ORIGINS`

## Mantenimiento

- Monitorear uso de la API de OpenAI
- Revisar y mantener actualizados los archivos de contexto
- Hacer respaldos regulares de la base de datos 