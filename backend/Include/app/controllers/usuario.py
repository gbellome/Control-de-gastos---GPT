from flask import Blueprint, jsonify, request
from Include.app.models import db, Usuario

usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/", methods=["GET"])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios])

@usuario_bp.route("/", methods=["POST"])
def create_usuario():
    data = request.json
    nuevo_usuario = Usuario(nombre=data["nombre"], email=data["email"], contrasena=data["contrasena"])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify(nuevo_usuario.to_dict()), 201
