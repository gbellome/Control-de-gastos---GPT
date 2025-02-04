from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Auditoria(db.Model):
    __tablename__ = 'auditorias'

    id = Column(Integer, primary_key=True)
    accion = Column(String(255), nullable=False)
    fecha = Column(DateTime, nullable=False)
    
    # Relación con usuario
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship('Usuario', back_populates='auditorias')

    def to_dict(self):
        return {
            "id": self.id,
            "accion": self.accion,
            "fecha": self.fecha,
            "usuario_id": self.usuario_id,
        }

    def __repr__(self):
        return f'<Auditoria {self.accion}, {self.fecha}>'
