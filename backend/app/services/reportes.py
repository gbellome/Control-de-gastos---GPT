from app.models.transaccion import Transaccion
from app.models.categoria import Categoria
from app.models.objetivo import Objetivo
from app import db

def generar_reporte_gastos_por_categoria():
    """
    Genera un reporte de gastos totales por categoría.
    """
    query = """
    SELECT c.nombre AS categoria, SUM(t.monto) AS total_gastado
    FROM transacciones t
    JOIN categorias c ON t.categoria_id = c.id
    GROUP BY c.nombre
    """
    resultados = db.session.execute(query).fetchall()
    return [{"categoria": row[0], "total_gastado": row[1]} for row in resultados]

def generar_reporte_gastos_vs_objetivos():
    """
    Genera un reporte comparativo entre los gastos actuales y los objetivos.
    """
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
            "restante": max(0, objetivo.monto_maximo - total_gastado)
        })
    return reporte
