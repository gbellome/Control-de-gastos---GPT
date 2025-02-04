from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from Include.app import db

class Transaccion(db.Model):
    __tablename__ = 'transacciones'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    monto = Column(Float, nullable=False)
    fecha = Column(DateTime, nullable=False)
    tipo = Column(String(50), nullable=False)
    descripcion = Column(String(255), nullable=True)

    # Relación con categoria
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    categoria = relationship('Categoria', back_populates='transacciones')

    # Relación con banco
    banco_id = Column(Integer, ForeignKey('bancos.id'))
    banco = relationship('Banco', back_populates='transacciones')

    # Relación con usuario
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship('Usuario', back_populates='transacciones')

    def to_dict(self):
        return {
            "id": self.id,
            "monto": self.monto,
            "fecha": self.fecha,
            "tipo": self.tipo,
            "descripcion": self.descripcion,
            "categoria_id": self.categoria_id,
            "banco_id": self.banco_id,
            "usuario_id": self.usuario_id,
        }

    def __repr__(self):
        return f'<Transaccion {self.descripcion}, {self.monto}, {self.fecha}>'
