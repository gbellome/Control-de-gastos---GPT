from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class ReglaCategorizacion(db.Model):
    __tablename__ = 'reglas_categorizacion'

    id = Column(Integer, primary_key=True)
    expresion_regular = Column(String(255), nullable=False)

    # Relación con categoria
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    categoria = relationship('Categoria', back_populates='reglas_categorizacion')

    def to_dict(self):
        return {
            "id": self.id,
            "expresion_regular": self.expresion_regular,
            "categoria_id": self.categoria_id,
        }

    def __repr__(self):
        return f'<ReglaCategorizacion {self.expresion_regular}>'
