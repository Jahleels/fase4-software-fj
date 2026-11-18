"""Servicio de reserva de salas."""

from exceptions import DatoInvalidoError
from models.servicio import Servicio


class ReservaSala(Servicio):
    """Representa una sala que puede reservarse por horas."""

    def __init__(self, identificador: str, costo_base: float, capacidad: int) -> None:
        try:
            self._capacidad = int(capacidad)
        except (TypeError, ValueError) as error_original:
            raise DatoInvalidoError("La capacidad debe ser un número entero.") from error_original
        super().__init__(identificador, "Reserva de sala", costo_base)

    def validar(self) -> None:
        super().validar()
        if self._capacidad <= 0:
            raise DatoInvalidoError("La capacidad debe ser mayor que cero.")

    def calcular_costo(self, duracion: float, descuento: float = 0) -> float:
        duracion, descuento = self.validar_calculo(duracion, descuento)
        subtotal = self._costo_base * duracion
        return subtotal * (1 - descuento)

    def describir(self) -> str:
        return f"Sala para {self._capacidad} personas"

