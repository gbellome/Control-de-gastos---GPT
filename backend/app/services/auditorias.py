from app import db
from app.models import Auditoria
from datetime import datetime

def registrar_accion(accion, usuario_id=None):
    """
    Registra una acción en la tabla de auditorías.
    
    Args:
        accion (str): Descripción de la acción realizada.
        usuario_id (int, optional): ID del usuario que realizó la acción. Si es None, se registra como anónimo.
    
    Raises:
        ValueError: Si la acción está vacía o no es válida.
    """
    if not accion or not isinstance(accion, str):
        raise ValueError("La acción debe ser una cadena no vacía.")
    
    # Crear un nuevo registro de auditoría
    nueva_auditoria = Auditoria(
        accion=accion,
        fecha=datetime.utcnow(),
        usuario_id=usuario_id
    )
    
    # Guardar en la base de datos
    db.session.add(nueva_auditoria)
    db.session.commit()

def obtener_auditorias_por_usuario(usuario_id):
    """
    Recupera todas las auditorías asociadas a un usuario específico.
    
    Args:
        usuario_id (int): ID del usuario.
    
    Returns:
        list: Lista de objetos Auditoria relacionados con el usuario.
    """
    if not usuario_id:
        return []
    
    return Auditoria.query.filter_by(usuario_id=usuario_id).order_by(Auditoria.fecha.desc()).all()

def obtener_todas_auditorias():
    """
    Recupera todas las auditorías registradas en el sistema.
    
    Returns:
        list: Lista de todas las auditorías.
    """
    return Auditoria.query.order_by(Auditoria.fecha.desc()).all()

def eliminar_auditorias_anteriores(fecha_limite):
    """
    Elimina todas las auditorías realizadas antes de una fecha específica.
    
    Args:
        fecha_limite (datetime): Fecha límite. Las auditorías anteriores a esta fecha serán eliminadas.
    """
    Auditoria.query.filter(Auditoria.fecha < fecha_limite).delete()
    db.session.commit()
