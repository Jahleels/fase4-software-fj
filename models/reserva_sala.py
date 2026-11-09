"""Servicio de reserva de salas."""

from exceptions import DatoInvalidoError
from models.servicio import Servicio


class ReservaSala(Servicio):
    """Representa una sala que puede reservarse por horas."""

    def __init__(self, identificador: str, costo_base: float, capacidad: int) -> None:
        self._capacidad = int(capacidad)
        super().__init__(identificador, "Reserva de sala", costo_base)

    def validar(self) -> None:
        super().validar()
        if self._capacidad <= 0:
            raise DatoInvalidoError("La capacidad debe ser mayor que cero.")

    def calcular_costo(self, duracion: float, descuento: float = 0) -> float:
        subtotal = self._costo_base * float(duracion)
        return subtotal * (1 - float(descuento))

    def describir(self) -> str:
        return f"Sala para {self._capacidad} personas"

