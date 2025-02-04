from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Include.app import db

class Banco(db.Model):
    __tablename__ = 'bancos'
    __table_args__ = {'extend_existing': True}

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
