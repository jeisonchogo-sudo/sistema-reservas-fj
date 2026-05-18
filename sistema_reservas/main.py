# main.py

from modelos.cliente import Cliente
from modelos.servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaTecnica
)
from modelos.reserva import Reserva
from utilidades.logger import guardar_log


print("\n========== INICIO DEL SISTEMA ==========\n")

try:

    # CLIENTE VÁLIDO
    cliente1 = Cliente(
        "Carlos Perez",
        "carlos@gmail.com",
        "3001234567"
    )

    # SERVICIOS
    sala = ReservaSala("Sala VIP", 100)
    equipo = AlquilerEquipo("Video Beam", 80)
    asesoria = AsesoriaTecnica("Consultoría", 150)

    # RESERVAS
    reserva1 = Reserva(cliente1, sala, 2)
    reserva1.confirmar_reserva()

    reserva2 = Reserva(cliente1, equipo, 3)
    reserva2.confirmar_reserva()

    reserva3 = Reserva(cliente1, asesoria, 1)
    reserva3.confirmar_reserva()

    # ERROR CONTROLADO
    cliente_error = Cliente(
        "AA",
        "correo_malo",
        "abc"
    )

except Exception as problema:

    guardar_log(problema)

    print(f"Se presentó un error: {problema}")

finally:
    print("\n========== FIN DEL SISTEMA ==========\n")
    