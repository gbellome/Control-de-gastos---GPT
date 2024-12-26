from models import db, Objetivo, Transaccion, Usuario
from datetime import datetime

def generar_alertas():
    """
    Este servicio revisa los objetivos de gasto y genera alertas si el gasto excede el objetivo.
    """
    alertas = []
    usuarios = Usuario.query.all()
    
    for usuario in usuarios:
        # Obtener los objetivos de gasto para el usuario
        objetivos = Objetivo.query.filter_by(usuario_id=usuario.id).all()
        
        for objetivo in objetivos:
            # Obtener las transacciones del mes actual para el usuario
            transacciones_mes = Transaccion.query.filter(
                Transaccion.usuario_id == usuario.id,
                Transaccion.fecha >= datetime(datetime.now().year, datetime.now().month, 1)
            ).all()
            
            # Calcular el gasto total en la categoría correspondiente
            gasto_total = sum(t.monto for t in transacciones_mes if t.categoria_id == objetivo.categoria_id)
            
            # Verificar si se excede el objetivo
            if gasto_total > (objetivo.sueldo_base * (objetivo.porcentaje_sueldo / 100)):
                alertas.append({
                    "usuario_id": usuario.id,
                    "objetivo_id": objetivo.id,
                    "gasto_total": gasto_total,
                    "limite_objetivo": objetivo.sueldo_base * (objetivo.porcentaje_sueldo / 100)
                })
    
    return alertas
