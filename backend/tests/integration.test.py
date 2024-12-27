from app.models import db, Usuario, Transaccion

def test_flujo_completo(self):
    # Crear usuario
    usuario = Usuario(nombre="Test User", email="test@user.com", contrasena="password123")
    db.session.add(usuario)
    db.session.commit()

    # Crear transacción
    transaccion = {
        "monto": 500.0,
        "fecha": "2024-12-25",
        "descripcion": "Compra en Walmart",
        "categoria_id": None,
        "usuario_id": usuario.id
    }
    self.client.post('/transacciones/', json=transaccion)

    # Aplicar regla de categorización
    regla = {
        "expresion_regular": "Walmart",
        "categoria_id": 3
    }
    aplicar_reglas_categorizacion([transaccion], [regla])

    # Verificar que la transacción esté categorizada
    transaccion_actualizada = Transaccion.query.filter_by(descripcion="Compra en Walmart").first()
    self.assertEqual(transaccion_actualizada.categoria_id, 3)
