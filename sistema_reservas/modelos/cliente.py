# modelos/cliente.py

from excepciones.errores import ClienteNoValido


class Cliente:
    """
    Representa un cliente del sistema
    """

    def __init__(self, nombre, correo, telefono):
        
        # Validar nombre
        if len(nombre.strip()) < 3:
            raise ClienteNoValido(
                "El nombre debe tener mínimo 3 caracteres"
            )

        # Validar correo
        if "@" not in correo:
            raise ClienteNoValido(
                "Correo electrónico inválido"
            )

        # Validar teléfono
        if not telefono.isdigit():
            raise ClienteNoValido(
                "El teléfono solo debe contener números"
            )

        # Encapsulación
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    def obtener_nombre(self):
        return self.__nombre

    def mostrar_datos(self):
        return f"{self.__nombre} - {self.__correo}"
    
    