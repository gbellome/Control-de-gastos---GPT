from app import db

# Modelo base para simplificar la conversión a diccionarios
class BaseModel(db.Model):
    __abstract__ = True

    def to_dict(self):
        """Convierte el modelo a un diccionario."""
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
