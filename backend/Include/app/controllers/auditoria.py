from flask import Blueprint, jsonify, request
from app.models import db, Auditoria

auditoria_bp = Blueprint("auditoria", __name__)

@auditoria_bp.route("/", methods=["GET"])
def get_auditorias():
    auditorias = Auditoria.query.all()
    return jsonify([auditoria.to_dict() for auditoria in auditorias])

@auditoria_bp.route("/", methods=["POST"])
def create_auditoria():
    data = request.json
    nueva_auditoria = Auditoria(
        accion=data["accion"],
        fecha=data["fecha"],
        usuario_id=data["usuario_id"]
    )
    db.session.add(nueva_auditoria)
    db.session.commit()
    return jsonify(nueva_auditoria.to_dict()), 201
