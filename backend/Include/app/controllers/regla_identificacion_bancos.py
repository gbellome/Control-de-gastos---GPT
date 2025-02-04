from flask import Blueprint, jsonify, request
from Include.app.models import db, ReglaIdentificacionBanco

regla_identificacion_bp = Blueprint("regla_identificacion_bancos", __name__)

@regla_identificacion_bp.route("/", methods=["GET"])
def get_reglas_identificacion():
    reglas = ReglaIdentificacionBanco.query.all()
    return jsonify([regla.to_dict() for regla in reglas])

@regla_identificacion_bp.route("/", methods=["POST"])
def create_regla_identificacion():
    data = request.json
    nueva_regla = ReglaIdentificacionBanco(
        banco_id=data["banco_id"],
        expresion_regular=data["expresion_regular"]
    )
    db.session.add(nueva_regla)
    db.session.commit()
    return jsonify(nueva_regla.to_dict()), 201

@regla_identificacion_bp.route("/<int:id>", methods=["DELETE"])
def delete_regla_identificacion(id):
    regla = ReglaIdentificacionBanco.query.get_or_404(id)
    db.session.delete(regla)
    db.session.commit()
    return jsonify({"message": "Regla de identificación de banco eliminada con éxito"})
