from flask import Blueprint, request, jsonify
from app.models.objetivo import Objetivo
from app import db

objetivos_bp = Blueprint("objetivos", __name__)

@objetivos_bp.route("/", methods=["GET"])
def listar_objetivos():
    """Obtiene todos los objetivos."""
    objetivos = Objetivo.query.all()
    return jsonify([objetivo.to_dict() for objetivo in objetivos]), 200

@objetivos_bp.route("/", methods=["POST"])
def crear_objetivo():
    """Crea un nuevo objetivo."""
    data = request.get_json()
    nuevo_objetivo = Objetivo(
        nombre=data["nombre"],
        porcentaje_sueldo=data["porcentaje_sueldo"],
        sueldo_base=data["sueldo_base"],
        mes=data["mes"]
    )
    db.session.add(nuevo_objetivo)
    db.session.commit()
    return jsonify(nuevo_objetivo.to_dict()), 201

@objetivos_bp.route("/<int:id>", methods=["PUT"])
def actualizar_objetivo(id):
    """Actualiza un objetivo existente."""
    data = request.get_json()
    objetivo = Objetivo.query.get_or_404(id)
    objetivo.nombre = data.get("nombre", objetivo.nombre)
    objetivo.porcentaje_sueldo = data.get("porcentaje_sueldo", objetivo.porcentaje_sueldo)
    objetivo.sueldo_base = data.get("sueldo_base", objetivo.sueldo_base)
    objetivo.mes = data.get("mes", objetivo.mes)
    db.session.commit()
    return jsonify(objetivo.to_dict()), 200

@objetivos_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_objetivo(id):
    """Elimina un objetivo."""
    objetivo = Objetivo.query.get_or_404(id)
    db.session.delete(objetivo)
    db.session.commit()
    return jsonify({"message": "Objetivo eliminado"}), 200
