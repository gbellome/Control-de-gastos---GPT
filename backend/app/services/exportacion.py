import csv
from io import StringIO
from app.models.transaccion import Transaccion
from app.models.categoria import Categoria
from app import db

def exportar_transacciones_csv():
    """
    Exporta todas las transacciones a un archivo CSV.
    """
    transacciones = db.session.query(
        Transaccion.fecha,
        Transaccion.descripcion,
        Transaccion.monto,
        Categoria.nombre.label("categoria")
    ).join(Categoria, Transaccion.categoria_id == Categoria.id).all()

    # Crear un archivo CSV en memoria
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Fecha", "Descripción", "Monto", "Categoría"])
    for transaccion in transacciones:
        writer.writerow([transaccion.fecha, transaccion.descripcion, transaccion.monto, transaccion.categoria])

    # Retornar el contenido del archivo CSV
    output.seek(0)
    return output.getvalue()
