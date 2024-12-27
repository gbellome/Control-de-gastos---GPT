def test_aplicar_reglas_a_transacciones(self):
    transacciones = [
        {"descripcion": "Compra Carrefour", "monto": 200.0},
        {"descripcion": "Pago Amazon", "monto": 50.0}
    ]
    reglas = [
        {"expresion_regular": "Carrefour", "categoria_id": 1},
        {"expresion_regular": "Amazon", "categoria_id": 2}
    ]
    resultado = aplicar_reglas_a_transacciones(transacciones, reglas)
    self.assertEqual(resultado[0]["categoria_id"], 1)
    self.assertEqual(resultado[1]["categoria_id"], 2)
