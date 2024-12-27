from app.models import db, Transaccion

def test_procesar_gran_cantidad_transacciones(self):
    transacciones = [{"descripcion": f"Transacción {i}", "monto": i * 10.0} for i in range(1000)]
    response = self.client.post('/transacciones/masivo', json=transacciones)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(Transaccion.query.all()), 1000)
