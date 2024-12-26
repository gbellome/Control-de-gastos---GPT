from flask import Blueprint, request, jsonify
from app.models.categoria import Categoria
from app import db

categorias_bp = Blueprint("categorias", __name__)

@categorias_bp.route("/", methods=["GET"])
def listar_categorias():
    """Obtiene todas las categorías."""
    categorias = Categoria.query.all()
    return jsonify([categoria.to_dict() for categoria in categorias]), 200

@categorias_bp.route("/", methods=["POST"])
def crear_categoria():
    """Crea una nueva categoría."""
    data = request.get_json()
    nueva_categoria = Categoria(nombre=data["nombre"])
    db.session.add(nueva_categoria)
    db.session.commit()
    return jsonify(nueva_categoria.to_dict()), 201

@categorias_bp.route("/<int:id>", methods=["PUT"])
def actualizar_categoria(id):
    """Actualiza una categoría existente."""
    data = request.get_json()
    categoria = Categoria.query.get_or_404(id)
    categoria.nombre = data.get("nombre", categoria.nombre)
    db.session.commit()
    return jsonify(categoria.to_dict()), 200

@categorias_bp.route("/<int:id>", methods=["DELETE"])
def eliminar_categoria(id):
    """Elimina una categoría."""
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    return jsonify({"message": "Categoría eliminada"}), 200
