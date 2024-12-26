from app.services.calculos import calcular_diferencia_objetivos

def generar_alertas():
    """
    Genera alertas si se exceden los objetivos de gasto.
    """
    diferencias = calcular_diferencia_objetivos()
    alertas = []
    for diferencia in diferencias:
        if diferencia["gasto_actual"] > diferencia["monto_maximo"]:
            alertas.append(
                f"¡Alerta! Has excedido el límite de '{diferencia['objetivo']}' "
                f"({diferencia['gasto_actual']} > {diferencia['monto_maximo']})"
            )
    return alertas
