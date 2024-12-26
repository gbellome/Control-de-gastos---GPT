from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class ReglaIdentificacionBanco(db.Model):
    __tablename__ = 'reglas_identificacion_bancos'

    id = Column(Integer, primary_key=True)
    expresion_regular = Column(String(255), nullable=False)

    # Relación con banco
    banco_id = Column(Integer, ForeignKey('bancos.id'))
    banco = relationship('Banco', back_populates='reglas_identificacion')

    def to_dict(self):
        return {
            "id": self.id,
            "expresion_regular": self.expresion_regular,
            "banco_id": self.banco_id,
        }

    def __repr__(self):
        return f'<ReglaIdentificacionBanco {self.expresion_regular}>'
