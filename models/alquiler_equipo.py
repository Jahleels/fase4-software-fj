"""Servicio de alquiler de equipos."""

from exceptions import DatoInvalidoError
from models.servicio import Servicio


class AlquilerEquipo(Servicio):
    """Representa un equipo disponible para alquiler."""

    def __init__(self, identificador: str, costo_base: float, tipo: str) -> None:
        self._tipo = tipo.strip()
        super().__init__(identificador, "Alquiler de equipo", costo_base)

    def validar(self) -> None:
        super().validar()
        if not self._tipo:
            raise DatoInvalidoError("El tipo de equipo es obligatorio.")

    def calcular_costo(self, duracion: float, descuento: float = 0) -> float:
        duracion, descuento = self.validar_calculo(duracion, descuento)
        subtotal = self._costo_base * duracion
        return subtotal * (1 - descuento)

    def describir(self) -> str:
        return f"Alquiler de equipo: {self._tipo}"

