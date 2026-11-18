"""Clase abstracta para los servicios de Software FJ."""

from abc import abstractmethod

from exceptions import DatoInvalidoError
from models.entidad import Entidad
from utils.validaciones import convertir_numero_positivo, validar_descuento


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
        self._costo_base = convertir_numero_positivo(costo_base, "El costo base")
        self._disponible = bool(disponible)
        self.validar()

    @property
    def disponible(self) -> bool:
        return self._disponible

    @property
    def costo_base(self) -> float:
        return self._costo_base

    def cambiar_disponibilidad(self, disponible: bool) -> None:
        """Permite habilitar o deshabilitar un servicio."""

        self._disponible = bool(disponible)

    def validar(self) -> None:
        super().validar()
        if not self._nombre:
            raise DatoInvalidoError("El nombre del servicio es obligatorio.")
        if self._costo_base <= 0:
            raise DatoInvalidoError("El costo base debe ser mayor que cero.")

    def validar_calculo(self, duracion, descuento=0) -> tuple[float, float]:
        """Valida los parámetros compartidos por los cálculos de costo."""

        duracion_valida = convertir_numero_positivo(duracion, "La duración")
        descuento_valido = validar_descuento(descuento)
        return duracion_valida, descuento_valido

    @abstractmethod
    def calcular_costo(self, duracion: float, descuento: float = 0) -> float:
        """Calcula el costo usando parámetros propios del servicio."""

    @abstractmethod
    def describir(self) -> str:
        """Devuelve una descripción sencilla del servicio."""

