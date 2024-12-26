from app.models import db, BaseModel

class Objetivo(BaseModel):
    __tablename__ = "objetivos_gastos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    porcentaje_sueldo = db.Column(db.Float, nullable=False)  # Ejemplo: 0.2 para 20%
    sueldo_base = db.Column(db.Float, nullable=False)
    monto_maximo = db.Column(db.Float, nullable=False)
    mes = db.Column(db.String(7), nullable=False)  # Formato: "YYYY-MM"

    # Relación con Categorías (si aplica)
    id_categoria = db.Column(db.Integer, db.ForeignKey("categorias.id"), nullable=True)
    categoria = db.relationship("Categoria", back_populates="objetivos")
