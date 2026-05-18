# excepciones/errores.py

class ErrorAplicacion(Exception):
    """Clase base para errores del sistema"""
    pass


class ClienteNoValido(ErrorAplicacion):
    pass


class ServicioInvalido(ErrorAplicacion):
    pass


class ErrorReserva(ErrorAplicacion):
    pass
