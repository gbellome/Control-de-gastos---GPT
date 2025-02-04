from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app import db

class Banco(db.Model):
    __tablename__ = 'bancos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)

    # Relación con transacciones
    transacciones = relationship('Transaccion', back_populates='banco')
    # Relación con reglas de identificación de bancos
    reglas_identificacion = relationship('ReglaIdentificacionBanco', back_populates='banco')

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
        }

    def __repr__(self):
        return f'<Banco {self.nombre}>'
