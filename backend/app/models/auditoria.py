from app.models import db, BaseModel
from datetime import datetime

class Auditoria(BaseModel):
    __tablename__ = "auditoria"

    id = db.Column(db.Integer, primary_key=True)
    accion = db.Column(db.String(255), nullable=False)
    fecha_hora = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    detalles = db.Column(db.Text, nullable=True)
