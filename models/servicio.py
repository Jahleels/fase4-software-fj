"""Clase abstracta para los servicios de Software FJ."""

from abc import abstractmethod

from exceptions import DatoInvalidoError
from models.entidad import Entidad


class Servicio(Entidad):
    """Define las operaciones comunes de los servicios."""

    def __init__(
        self,
        identificador: str,
        nombre: str,
        costo_base: float,
        disponible: bool = True,
    ) -> None:
        super().__init__(identificador)
        self._nombre = nombre.strip()
        self._costo_base = float(costo_base)
        self._disponible = disponible
        self.validar()

    @property
    def disponible(self) -> bool:
        return self._disponible

    def validar(self) -> None:
        super().validar()
        if not self._nombre:
            raise DatoInvalidoError("El nombre del servicio es obligatorio.")
        if self._costo_base <= 0:
            raise DatoInvalidoError("El costo base debe ser mayor que cero.")

    @abstractmethod
    def calcular_costo(self, duracion: float, descuento: float = 0) -> float:
        """Calcula el costo usando parámetros propios del servicio."""

    @abstractmethod
    def describir(self) -> str:
        """Devuelve una descripción sencilla del servicio."""

