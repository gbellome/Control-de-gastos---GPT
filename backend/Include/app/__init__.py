import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

# Crear instancias
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """
    Crea y configura una instancia de la aplicación Flask.
    """
    app = Flask(__name__)

    # Configuración de la aplicación (según el entorno)
    env = os.getenv("FLASK_ENV", "development")
    if env == "development":
        app.config.from_object("Include.app.config_dev")
    elif env == "production":
        app.config.from_object("Include.app.config_prd")
    else:
        raise ValueError(f"Entorno no válido: {env}")

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    # Registrar blueprints
    from Include.app.controllers import register_blueprints
    register_blueprints(app)

    # Rutas base
    @app.route("/")
    def index():
        return {"message": "API Backend en Flask está funcionando correctamente."}

    return app