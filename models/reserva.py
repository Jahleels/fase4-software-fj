"""Modelo que relaciona un cliente con un servicio."""

from exceptions import OperacionNoPermitidaError, ReservaInvalidaError
from models.cliente import Cliente
from models.entidad import Entidad
from models.servicio import Servicio


class Reserva(Entidad):
    """Representa una reserva y controla sus cambios de estado."""

    def __init__(
        self,
        identificador: str,
        cliente: Cliente,
        servicio: Servicio,
        duracion: float,
    ) -> None:
        super().__init__(identificador)
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = float(duracion)
        self._estado = "pendiente"
        self.validar()

    @property
    def estado(self) -> str:
        return self._estado

    def validar(self) -> None:
        super().validar()
        if self._duracion <= 0:
            raise ReservaInvalidaError("La duración debe ser mayor que cero.")

    def confirmar(self) -> None:
        if self._estado != "pendiente":
            raise OperacionNoPermitidaError("Solo se confirman reservas pendientes.")
        self._estado = "confirmada"

    def cancelar(self) -> None:
        if self._estado == "cancelada":
            raise OperacionNoPermitidaError("La reserva ya está cancelada.")
        self._estado = "cancelada"

    def calcular_total(self, descuento: float = 0) -> float:
        return self._servicio.calcular_costo(self._duracion, descuento)

