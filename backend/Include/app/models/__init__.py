from flask_sqlalchemy import SQLAlchemy

# Inicialización de SQLAlchemy
db = SQLAlchemy()

# Importación de modelos
from .usuario import Usuario
from .banco import Banco
from .categoria import Categoria
from .transaccion import Transaccion
from .objetivo import Objetivo
from .auditoria import Auditoria
from .regla_categorizacion import ReglaCategorizacion
from .regla_identificacion_banco import ReglaIdentificacionBanco

# Agregar aquí otros modelos en caso de que se necesiten en el futuro
__all__ = [
    "db",
    "Usuario",
    "Banco",
    "Categoria",
    "Transaccion",
    "Objetivo",
    "Auditoria",
    "ReglaCategorizacion",
    "ReglaIdentificacionBanco",
]
