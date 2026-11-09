"""Clase abstracta para las entidades del sistema."""

from abc import ABC, abstractmethod

from exceptions import DatoInvalidoError


class Entidad(ABC):
    """Define la información mínima que comparten las entidades."""

    def __init__(self, identificador: str) -> None:
        self._identificador = str(identificador).strip()

    @property
    def identificador(self) -> str:
        return self._identificador

    @abstractmethod
    def validar(self) -> None:
        """Valida la información particular de cada entidad."""

        if not self._identificador:
            raise DatoInvalidoError("El identificador es obligatorio.")

