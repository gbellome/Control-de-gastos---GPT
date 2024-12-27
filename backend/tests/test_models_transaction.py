import unittest
from app import create_app, db
from app.models.usuario import Usuario
from app.models.categoria import Categoria
from app.models.banco import Banco
from app.models.transaccion import Transaccion
from datetime import datetime

class TestTransaccionModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configuración inicial de la aplicación en modo de pruebas
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        # Limpiar después de todas las pruebas
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def setUp(self):
        # Limpiar la base de datos antes de cada prueba
        db.session.query(Transaccion).delete()
        db.session.query(Categoria).delete()
        db.session.query(Banco).delete()
        db.session.query(Usuario).delete()
        db.session.commit()

    def test_crear_transaccion(self):
        # Crear un usuario de prueba
        usuario = Usuario(nombre="Test User", email="test@example.com", contrasena="password123")
        db.session.add(usuario)
        db.session.commit()

        # Crear una categoría de prueba
        categoria = Categoria(nombre="Alimentos", descripcion="Gastos en comida y supermercado")
        db.session.add(categoria)
        db.session.commit()

        # Crear un banco de prueba
        banco = Banco(nombre="BBVA")
        db.session.add(banco)
        db.session.commit()

        # Crear una transacción de prueba
        transaccion = Transaccion(
            monto=1500.00,
            fecha=datetime(2024, 1, 1),
            tipo="gasto",
            descripcion="Compra en supermercado",
            categoria_id=categoria.id,
            banco_id=banco.id,
            usuario_id=usuario.id
        )
        db.session.add(transaccion)
        db.session.commit()

        # Verificar que la transacción fue creada correctamente
        transaccion_db = Transaccion.query.first()
        self.assertIsNotNone(transaccion_db)
        self.assertEqual(transaccion_db.monto, 1500.00)
        self.assertEqual(transaccion_db.tipo, "gasto")
        self.assertEqual(transaccion_db.descripcion, "Compra en supermercado")
        self.assertEqual(transaccion_db.categoria_id, categoria.id)
        self.assertEqual(transaccion_db.banco_id, banco.id)
        self.assertEqual(transaccion_db.usuario_id, usuario.id)

    def test_relacion_categoria(self):
        # Crear una categoría de prueba
        categoria = Categoria(nombre="Transporte", descripcion="Gastos en transporte público o privado")
        db.session.add(categoria)
        db.session.commit()

        # Crear una transacción asociada a la categoría
        transaccion = Transaccion(
            monto=500.00,
            fecha=datetime(2024, 1, 2),
            tipo="gasto",
            descripcion="Pasaje de tren",
            categoria_id=categoria.id
        )
        db.session.add(transaccion)
        db.session.commit()

        # Verificar la relación
        transaccion_db = Transaccion.query.first()
        self.assertIsNotNone(transaccion_db)
        self.assertEqual(transaccion_db.categoria.nombre, "Transporte")

    def test_relacion_banco(self):
        # Crear un banco de prueba
        banco = Banco(nombre="MercadoPago")
        db.session.add(banco)
        db.session.commit()

        # Crear una transacción asociada al banco
        transaccion = Transaccion(
            monto=200.00,
            fecha=datetime(2024, 1, 3),
            tipo="ingreso",
            descripcion="Transferencia recibida",
            banco_id=banco.id
        )
        db.session.add(transaccion)
        db.session.commit()

        # Verificar la relación
        transaccion_db = Transaccion.query.first()
        self.assertIsNotNone(transaccion_db)
        self.assertEqual(transaccion_db.banco.nombre, "MercadoPago")

if __name__ == "__main__":
    unittest.main()