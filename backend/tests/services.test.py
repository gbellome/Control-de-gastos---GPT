

def test_aplicar_regla_categorizacion(self):
    transaccion = {
        "descripcion": "Compra en Carrefour",
        "monto": 200.0
    }
    regla = {
        "expresion_regular": "Carrefour",
        "categoria_id": 2
    }
    resultado = aplicar_regla_categorizacion(transaccion, regla)
    self.assertEqual(resultado["categoria_id"], 2)
