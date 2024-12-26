import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Crear instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    """
    Crea y configura una instancia de la aplicación Flask.
    """
    app = Flask(__name__)

    # Configuración de la aplicación (según el entorno)
    env = os.getenv("FLASK_ENV", "development")
    if env == "development":
        app.config.from_object("app.config_dev")
    elif env == "production":
        app.config.from_object("app.config_prd")
    else:
        raise ValueError(f"Entorno no válido: {env}")

    # Inicializar extensiones
    db.init_app(app)
    CORS(app)

    # Registrar blueprints
    from app.controllers.transacciones import transacciones_bp
    from app.controllers.categorias import categorias_bp
    from app.controllers.objetivos import objetivos_bp
    from app.controllers.reportes import reportes_bp

    app.register_blueprint(transacciones_bp, url_prefix="/api/transacciones")
    app.register_blueprint(categorias_bp, url_prefix="/api/categorias")
    app.register_blueprint(objetivos_bp, url_prefix="/api/objetivos")
    app.register_blueprint(reportes_bp, url_prefix="/api/reportes")

    # Rutas base (opcional)
    @app.route("/")
    def index():
        return {"message": "API Backend en Flask está funcionando correctamente."}

    return app
