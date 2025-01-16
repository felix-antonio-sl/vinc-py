from __future__ import with_statement
import os
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from app import create_app
from app.models import db
import logging

# Configuración de Alembic
config = context.config
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

# Crear la aplicación Flask usando la factory
app = create_app()

# Obtener la URL de la base de datos desde la configuración de Flask
with app.app_context():
    sqlalchemy_url = app.config.get('SQLALCHEMY_DATABASE_URI')
    if sqlalchemy_url is None:
        raise ValueError("SQLALCHEMY_DATABASE_URI no está configurado en la configuración de Flask.")
    config.set_main_option('sqlalchemy.url', sqlalchemy_url)
    target_metadata = db.metadata

def run_migrations_offline():
    """Runs migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Runs migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
