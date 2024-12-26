import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models.transaccion import Transaccion

app = create_app()

with app.app_context():
    # Crear una transaccion de prueba
    nueva_transaccion = Transaccion(monto=100, categoria="Supermercado")
    db.session.add(nueva_transaccion)
    db.session.commit()

    # Verificar si la transaccion fue agregada
    transacciones = Transaccion.query.all()
    print(transacciones)