# modelos/servicio.py

from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre_servicio, tarifa_base):
        self.nombre_servicio = nombre_servicio
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self, horas):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, horas):
        return self.tarifa_base * horas


class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas):
        return (self.tarifa_base * horas) + 20


class AsesoriaTecnica(Servicio):

    def calcular_costo(self, horas):
        return (self.tarifa_base * horas) * 1.5
    