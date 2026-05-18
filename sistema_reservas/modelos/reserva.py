# modelos/reserva.py

from excepciones.errores import ErrorReserva
from utilidades.logger import guardar_log


class Reserva:

    def __init__(self, cliente, servicio, horas):

        if horas <= 0:
            raise ErrorReserva(
                "La duración de la reserva debe ser mayor a cero"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar_reserva(self):

        try:
            total = self.servicio.calcular_costo(self.horas)

            self.estado = "Confirmada"

            print(
                f"Reserva realizada correctamente. "
                f"Valor total: ${total}"
            )

        except Exception as error:

            guardar_log(
                f"Error al confirmar reserva: {error}"
            )

            raise ErrorReserva(
                "No fue posible confirmar la reserva"
            )

    def cancelar_reserva(self):

        self.estado = "Cancelada"

        print("La reserva fue cancelada")
        