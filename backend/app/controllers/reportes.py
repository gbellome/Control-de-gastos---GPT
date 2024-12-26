from flask import Blueprint, jsonify
from app.models.transaccion import Transaccion
from app.models.objetivo import Objetivo
from app import db

reportes_bp = Blueprint("reportes", __name__)

@reportes_bp.route("/gastos-por-categoria", methods=["GET"])
def gastos_por_categoria():
    """Genera un reporte de gastos por categoría."""
    query = """
    SELECT c.nombre AS categoria, SUM(t.monto) AS total_gastado
    FROM transacciones t
    JOIN categorias c ON t.categoria_id = c.id
    GROUP BY c.nombre
    """
    resultados = db.session.execute(query).fetchall()
    reporte = [{"categoria": row[0], "total_gastado": row[1]} for row in resultados]
    return jsonify(reporte), 200

@reportes_bp.route("/gastos-vs-objetivos", methods=["GET"])
def gastos_vs_objetivos():
    """Compara gastos actuales contra los objetivos."""
    objetivos = Objetivo.query.all()
    reporte = []
    for objetivo in objetivos:
        total_gastado = db.session.query(db.func.sum(Transaccion.monto)).filter(
            Transaccion.categoria_id == objetivo.id_categoria
        ).scalar() or 0
        reporte.append({
            "objetivo": objetivo.nombre,
            "gasto_actual": total_gastado,
            "monto_maximo": objetivo.monto_maximo,
            "restante": objetivo.monto_maximo - total_gastado
        })
    return jsonify(reporte), 200
