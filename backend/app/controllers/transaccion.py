from flask import Blueprint, request, jsonify
from app.models import db, Transaccion

transaccion_bp = Blueprint("transaccion", __name__)

@transaccion_bp.route("/", methods=["GET"])
def listar_transacciones():
    """Obtiene todas las transacciones."""
    transacciones = Transaccion.query.all()
    return jsonify([transaccion.to_dict() for transaccion in transacciones]), 200

@transaccion_bp.route("/", methods=["POST"])
def crear_transaccion():
    """Crea una nueva transacción."""
    data = request.get_json()
    nueva_transaccion = Transaccion(
        fecha=data["fecha"],
        descripcion=data["descripcion"],
        monto=data["monto"],
        tipo=data["tipo"],
        categoria_id=data["categoria_id"],
        banco_id=data["banco_id"],
        usuario_id=data["usuario_id"],
    )
    db.session.add(nueva_transaccion)
    db.session.commit()
    return jsonify(nueva_transaccion.to_dict()), 201

@transaccion_bp.route("/<int:id>", methods=["PUT"])
def actualizar_transaccion(id):
    """Actualiza una transacción existente."""
    data = request.get_json()
    transaccion = Transaccion.query.get_or_404(id)
    transaccion.fecha = data.get("fecha", transaccion.fecha)
    transaccion.descripcion = data.get("descripcion", transaccion.descripcion)
    transaccion.monto = data.get("monto", transaccion.monto)
    transaccion.categoria_id = data.get("categoria_id", transaccion.categoria_id)
    db.session.commit()
    return jsonify(transaccion.to_dict()), 200

@transaccion_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_transaccion(id):
    """Elimina una transacción."""
    transaccion = Transaccion.query.get_or_404(id)
    db.session.delete(transaccion)
    db.session.commit()
    return jsonify({"message": "Transacción eliminada"}), 200
