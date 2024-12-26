import unittest
from app import create_app, db
from app.models import Transaccion, Usuario, Categoria

class TestTransacciones(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_class='TestingConfig')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_crear_transaccion(self):
        # Crear una transacción de prueba
        usuario = Usuario(nombre="Juan", email="juan@test.com", contrasena="123456")
        categoria = Categoria(nombre="Comida", descripcion="Gastos de comida")
        db.session.add(usuario)
        db.session.add(categoria)
        db.session.commit()

        transaccion = Transaccion(monto=150.0, fecha="2024-12-25", descripcion="Compra supermercado", usuario_id=usuario.id, categoria_id=categoria.id)
        db.session.add(transaccion)
        db.session.commit()

        # Verificar que la transacción fue agregada
        transacciones = Transaccion.query.all()
        self.assertEqual(len(transacciones), 1)
        self.assertEqual(transacciones[0].descripcion, "Compra supermercado")
