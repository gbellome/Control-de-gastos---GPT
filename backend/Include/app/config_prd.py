import os

# Configuración básica
DEBUG = False  # Desactivar modo de depuración para producción
SECRET_KEY = os.getenv("SECRET_KEY", "clave_production")  # Clave secreta, debe ser segura y definida en el entorno

# Configuración de la base de datos
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # Leer la URI de la base de datos desde el entorno
if not SQLALCHEMY_DATABASE_URI:
    raise ValueError("La variable DATABASE_URL no está configurada.")
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deshabilitar el seguimiento de modificaciones (mejora el rendimiento)

# Configuración de CORS
CORS_HEADERS = "Content-Type"

# Configuración adicional para producción
ENV_NAME = "production"
API_VERSION = "v1"

# Opciones de seguridad (HTTPS)
SESSION_COOKIE_SECURE = True  # Asegura que las cookies solo se envíen a través de HTTPS
REMEMBER_COOKIE_SECURE = True  # Asegura que las cookies de "recordar sesión" sean seguras
