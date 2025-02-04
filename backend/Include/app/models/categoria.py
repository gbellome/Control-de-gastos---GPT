from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app import db

class Categoria(db.Model):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=True)

    # Relación con transacciones
    transacciones = relationship('Transaccion', back_populates='categoria')
    # Relación con reglas de categorización
    reglas_categorizacion = relationship('ReglaCategorizacion', back_populates='categoria')

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion
        }

    def __repr__(self):
        return f'<Categoria {self.nombre}>'
