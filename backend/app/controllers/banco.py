from flask import Blueprint, jsonify, request
from app.models import db, Banco

banco_bp = Blueprint("banco", __name__)

@banco_bp.route("/", methods=["GET"])
def get_bancos():
    bancos = Banco.query.all()
    return jsonify([banco.to_dict() for banco in bancos])

@banco_bp.route("/", methods=["POST"])
def create_banco():
    data = request.json
    nuevo_banco = Banco(nombre=data["nombre"])
    db.session.add(nuevo_banco)
    db.session.commit()
    return jsonify(nuevo_banco.to_dict()), 201
