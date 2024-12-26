from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Objetivo(db.Model):
    __tablename__ = 'objetivos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    porcentaje_sueldo = Column(Float, nullable=False)
    sueldo_base = Column(Float, nullable=False)
    mes = Column(String(20), nullable=False)

    # Relación con usuario
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship('Usuario', back_populates='objetivos')

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "porcentaje_sueldo": self.porcentaje_sueldo,
            "sueldo_base": self.sueldo_base,
            "mes": self.mes,
            "usuario_id": self.usuario_id,
        }

    def __repr__(self):
        return f'<Objetivo {self.nombre}, {self.porcentaje_sueldo * self.sueldo_base}>'
