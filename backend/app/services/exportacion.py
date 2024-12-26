import csv
from models import db, Transaccion
from io import StringIO

def exportar_reportes(usuario_id, mes, anio):
    """
    Este servicio genera un archivo CSV con las transacciones de un usuario para un mes específico.
    """
    transacciones = Transaccion.query.filter(
        Transaccion.usuario_id == usuario_id,
        Transaccion.fecha.month == mes,
        Transaccion.fecha.year == anio
    ).all()

    output = StringIO()
    writer = csv.writer(output)
    
    # Escribir el encabezado del archivo CSV
    writer.writerow(["ID", "Monto", "Fecha", "Descripción", "Categoria", "Banco", "Tipo"])

    # Escribir las transacciones
    for transaccion in transacciones:
        writer.writerow([
            transaccion.id,
            transaccion.monto,
            transaccion.fecha.strftime('%Y-%m-%d'),
            transaccion.descripcion,
            transaccion.categoria.nombre if transaccion.categoria else "N/A",
            transaccion.banco.nombre if transaccion.banco else "N/A",
            transaccion.tipo
        ])
    
    output.seek(0)
    return output.getvalue()
