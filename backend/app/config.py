import os

ENV = os.getenv("FLASK_ENV", "development")

if ENV == "development":
    from .config_dev import *
elif ENV == "production":
    from .config_prd import *
else:
    raise ValueError(f"Entorno no válido: {ENV}")