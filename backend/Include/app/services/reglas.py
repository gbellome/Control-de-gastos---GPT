import re
from models import db, ReglaCategorizacion, Transaccion

def categorizar_transacciones():
    """
    Este servicio aplica las reglas de categorización a las transacciones no categorizadas
    utilizando expresiones regulares definidas en la base de datos.
    """
    reglas = ReglaCategorizacion.query.all()
    
    # Obtener todas las transacciones no categorizadas
    transacciones = Transaccion.query.filter_by(categoria_id=None).all()
    
    for transaccion in transacciones:
        for regla in reglas:
            if re.search(regla.expresion_regular, transaccion.descripcion, re.IGNORECASE):
                transaccion.categoria_id = regla.categoria_id
                db.session.commit()
                break  # Solo se asigna la primera categoría que coincide

    return f"{len(transacciones)} transacciones categorizadas"
