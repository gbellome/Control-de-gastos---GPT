from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(100), nullable=False)

    # Relación con transacciones
    transacciones = relationship('Transaccion', back_populates='usuario')
    # Relación con objetivos
    objetivos = relationship('Objetivo', back_populates='usuario')
    # Relación con auditorías
    auditorias = relationship('Auditoria', back_populates='usuario')

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "contrasena": self.contrasena,
        }

    def __repr__(self):
        return f'<Usuario {self.nombre}>'
