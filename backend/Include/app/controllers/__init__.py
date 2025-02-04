from flask import Blueprint

# Importar controladores
from Include.app.controllers.usuario import usuario_bp
from Include.app.controllers.banco import banco_bp
from Include.app.controllers.categoria import categoria_bp
from Include.app.controllers.transaccion import transaccion_bp
from Include.app.controllers.objetivo import objetivo_bp
from Include.app.controllers.auditoria import auditoria_bp
from Include.app.controllers.regla_categorizacion import regla_categorizacion_bp
from Include.app.controllers.regla_identificacion_bancos import regla_identificacion_bp

def register_blueprints(app):
    app.register_blueprint(usuario_bp, url_prefix="/api/usuarios")
    app.register_blueprint(banco_bp, url_prefix="/api/bancos")
    app.register_blueprint(categoria_bp, url_prefix="/api/categorias")
    app.register_blueprint(transaccion_bp, url_prefix="/api/transacciones")
    app.register_blueprint(objetivo_bp, url_prefix="/api/objetivos")
    app.register_blueprint(auditoria_bp, url_prefix="/api/auditorias")
    app.register_blueprint(regla_categorizacion_bp, url_prefix="/api/reglas_categorizacion")
    app.register_blueprint(regla_identificacion_bp, url_prefix="/api/reglas_identificacion_bancos")
