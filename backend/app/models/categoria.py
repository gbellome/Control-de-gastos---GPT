from app.models import db, BaseModel

class Categoria(BaseModel):
    __tablename__ = "categorias"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False, unique=True)

    # Relación con Transacciones
    transacciones = db.relationship("Transaccion", back_populates="categoria", cascade="all, delete")
