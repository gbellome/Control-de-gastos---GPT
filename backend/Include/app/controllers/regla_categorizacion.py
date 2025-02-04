from flask import Blueprint, jsonify, request
from app.models import db, ReglaCategorizacion

regla_categorizacion_bp = Blueprint("regla_categorizacion", __name__)

@regla_categorizacion_bp.route("/", methods=["GET"])
def get_reglas_categorizacion():
    reglas = ReglaCategorizacion.query.all()
    return jsonify([regla.to_dict() for regla in reglas])

@regla_categorizacion_bp.route("/", methods=["POST"])
def create_regla_categorizacion():
    data = request.json
    nueva_regla = ReglaCategorizacion(
        expresion_regular=data["expresion_regular"],
        categoria_id=data["categoria_id"]
    )
    db.session.add(nueva_regla)
    db.session.commit()
    return jsonify(nueva_regla.to_dict()), 201

@regla_categorizacion_bp.route("/<int:id>", methods=["DELETE"])
def delete_regla_categorizacion(id):
    regla = ReglaCategorizacion.query.get_or_404(id)
    db.session.delete(regla)
    db.session.commit()
    return jsonify({"message": "Regla de categorización eliminada con éxito"})
