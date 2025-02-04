# backend/Include/app/models/tests/test_models_auditoria.py

# ------- Importaciones
import unittest
from datetime import datetime

from Include.app import create_app, db
from Include.app.models import Usuario, Auditoria


# ------- Clases
class TestAssuranceModels(unittest.TestCase):
    
    # Antes de ejecutar las pruebas
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    # Luego de ejecutar todas las pruebas
    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
    
    # Configuracion previa al inicio
    def setUp(self):
        """
        Configura el entorno de prueba, incluyendo una base de datos SQLite en memoria.
        """
        
        # Crear un usuario de prueba para asociar con las auditorías
        self.usuario = Usuario(nombre="Usuario de Prueba", email="prueba@example.com", contrasena="password123")
        
        db.session.add(self.usuario)
        db.session.commit()
        
    # Configuracion posterior al inicio
    def tearDown(self):
        """
        Limpia la base de datos después de cada prueba.
        """
        
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    # PRUEBA 01        
    def test_crear_auditoria(self):
        """
        Verifica que una auditoría se pueda crear y almacenar correctamente en la base de datos.
        """
        
        auditoria = Auditoria(accion="Crear transacción", fecha=datetime.now(), usuario_id=self.usuario.id)
        
        db.session.add(auditoria)
        db.session.commit()

        resultado = Auditoria.query.first()
        
        self.assertIsNotNone(resultado, "La auditoría no fue guardada en la base de datos.")
        self.assertEqual(resultado.accion, "Crear transacción", "La acción de auditoría no coincide.")
        self.assertEqual(resultado.usuario_id, self.usuario.id, "El ID de usuario asociado no coincide.")

    # PRUEBA 02        
    #def test_auditoria_sin_accion(self):
    #    """
    #    Verifica que no se permita crear una auditoría sin una acción definida.
    #    """
    #    
    #    auditoria = Auditoria(fecha=datetime.now(), usuario_id=self.usuario.id)
    #
    #    with self.assertRaises(Exception, msg="Se esperaba una excepción al guardar una auditoría sin acción."):
    #        db.session.add(auditoria)
    #        db.session.commit()

    # PRUEBA 03        
    #def test_auditoria_sin_usuario(self):
    #    """
    #    Verifica que no se permita crear una auditoría sin un usuario asociado.
    #    """
    #    
    #    auditoria = Auditoria(accion="Eliminar transacción", fecha=datetime.now())
    #
    #    with self.assertRaises(Exception, msg="Se esperaba una excepción al guardar una auditoría sin usuario."):
    #        db.session.add(auditoria)
    #        db.session.commit()

    # PRUEBA 04        
    #def test_auditoria_fecha_automatica(self):
    #    """
    #    Verifica que, si no se proporciona una fecha, se asigne automáticamente la fecha y hora actual.
    #    """
    #    
    #    auditoria = Auditoria(accion="Actualizar categoría", usuario_id=self.usuario.id)
    #    db.session.add(auditoria)
    #    db.session.commit()
    #
    #    resultado = Auditoria.query.first()
    #    self.assertIsNotNone(resultado.fecha, "La fecha debería haberse asignado automáticamente.")

    # PRUEBA 05        
    #def test_auditorias_multiples(self):
    #    """
    #    Verifica que se puedan registrar múltiples auditorías para el mismo usuario.
    #    """
    #    
    #    auditoria1 = Auditoria(accion="Acceso al sistema", fecha=datetime.now(), usuario_id=self.usuario.id)
    #    auditoria2 = Auditoria(accion="Modificación de datos", fecha=datetime.now(), usuario_id=self.usuario.id)
    #
    #    db.session.add_all([auditoria1, auditoria2])
    #    db.session.commit()
    #
    #    resultados = Auditoria.query.filter_by(usuario_id=self.usuario.id).all()
    #    self.assertEqual(len(resultados), 2, "Debería haber dos registros de auditoría para el mismo usuario.")
        
if __name__ == '__main__':
    unittest.main()