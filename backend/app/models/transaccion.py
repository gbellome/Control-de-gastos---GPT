from app.models import db, BaseModel

class Transaccion(BaseModel):
    __tablename__ = "transacciones"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.id"), nullable=True)

    # Relación con Categoría
    categoria = db.relationship("Categoria", back_populates="transacciones")
