from app.models.transaccion import Transaccion
from app.models.objetivo import Objetivo
from app import db

def calcular_gasto_por_categoria(categoria_id):
    """
    Calcula el gasto total para una categoría específica.
    """
    total_gasto = db.session.query(db.func.sum(Transaccion.monto)).filter(
        Transaccion.categoria_id == categoria_id
    ).scalar() or 0
    return total_gasto

def calcular_diferencia_objetivos():
    """
    Calcula la diferencia entre los gastos actuales y los objetivos para todas las categorías.
    """
    objetivos = Objetivo.query.all()
    resultado = []
    for objetivo in objetivos:
        gasto_actual = calcular_gasto_por_categoria(objetivo.id_categoria)
        resultado.append({
            "objetivo": objetivo.nombre,
            "gasto_actual": gasto_actual,
            "monto_maximo": objetivo.monto_maximo,
            "restante": objetivo.monto_maximo - gasto_actual
        })
    return resultado
