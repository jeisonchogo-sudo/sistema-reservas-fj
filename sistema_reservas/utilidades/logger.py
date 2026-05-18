# utilidades/logger.py

from datetime import datetime

def guardar_log(mensaje):
    """
    Guarda eventos y errores del sistema
    """
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{datetime.now()} -> {mensaje}\n")
        