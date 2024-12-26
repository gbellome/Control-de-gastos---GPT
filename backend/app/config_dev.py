import os

# Configuración básica
DEBUG = True  # Habilitar modo de depuración para desarrollo
SECRET_KEY = os.getenv("SECRET_KEY", "clave_development")  # Clave secreta para la app

# Configuración de la base de datos
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///local_dev.db")  # SQLite por defecto
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deshabilitar el seguimiento de modificaciones (mejora el rendimiento)

# Configuración de CORS
CORS_HEADERS = "Content-Type"

# Configuración adicional para desarrollo
ENV_NAME = "development"
API_VERSION = "v1"