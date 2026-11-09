"""Modelo de cliente."""

from exceptions import DatoInvalidoError
from models.entidad import Entidad


class Cliente(Entidad):
    """Representa un cliente y protege sus datos principales."""

    def __init__(self, identificador: str, nombre: str, correo: str) -> None:
        super().__init__(identificador)
        self._nombre = nombre.strip()
        self._correo = correo.strip().lower()
        self.validar()

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def correo(self) -> str:
        return self._correo

    def validar(self) -> None:
        super().validar()
        if len(self._nombre) < 3:
            raise DatoInvalidoError("El nombre debe tener al menos tres caracteres.")
        if "@" not in self._correo:
            raise DatoInvalidoError("El correo no tiene un formato válido.")

