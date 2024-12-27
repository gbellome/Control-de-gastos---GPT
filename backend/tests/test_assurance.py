import unittest
from app import create_app, db
from app.models import Auditoria, Usuario
from app.services.auditorias import registrar_accion

class TestAuditoriaService(unittest.TestCase):
    """Pruebas unitarias para el servicio de auditorías."""

    def setUp(self):
        """
        Configuración inicial para las pruebas.
        """
        # Crear la aplicación con configuración de pruebas
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Crear un usuario de prueba
        self.usuario = Usuario(nombre="Test User", email="test@example.com", contrasena="1234")
        db.session.add(self.usuario)
        db.session.commit()

    def tearDown(self):
        """
        Limpieza después de cada prueba.
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_registrar_accion_exitoso(self):
        """
        Prueba que se registre una acción correctamente.
        """
        accion = "Usuario inició sesión"
        registrar_accion(accion, usuario_id=self.usuario.id)

        # Verificar que la acción se registró en la base de datos
        auditoria = Auditoria.query.first()
        self.assertIsNotNone(auditoria)
        self.assertEqual(auditoria.accion, accion)
        self.assertEqual(auditoria.usuario_id, self.usuario.id)

    def test_registrar_accion_sin_usuario(self):
        """
        Prueba que se registre una acción sin un usuario.
        """
        accion = "Acción genérica sin usuario"
        registrar_accion(accion)

        # Verificar que la acción se registró en la base de datos
        auditoria = Auditoria.query.first()
        self.assertIsNotNone(auditoria)
        self.assertEqual(auditoria.accion, accion)
        self.assertIsNone(auditoria.usuario_id)

    def test_registrar_accion_invalida(self):
        """
        Prueba que no se permita registrar una acción inválida.
        """
        with self.assertRaises(ValueError):
            registrar_accion(None)

        with self.assertRaises(ValueError):
            registrar_accion("")

    def test_registrar_varias_acciones(self):
        """
        Prueba que se puedan registrar múltiples acciones.
        """
        acciones = ["Primera acción", "Segunda acción", "Tercera acción"]
        for accion in acciones:
            registrar_accion(accion, usuario_id=self.usuario.id)

        # Verificar que se registraron todas las acciones
        auditorias = Auditoria.query.all()
        self.assertEqual(len(auditorias), len(acciones))
        for i, auditoria in enumerate(auditorias):
            self.assertEqual(auditoria.accion, acciones[i])
            self.assertEqual(auditoria.usuario_id, self.usuario.id)

if __name__ == '__main__':
    unittest.main()
