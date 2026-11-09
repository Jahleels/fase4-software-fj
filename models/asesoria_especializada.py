"""Servicio de asesorías especializadas."""

from exceptions import DatoInvalidoError
from models.servicio import Servicio


class AsesoriaEspecializada(Servicio):
    """Representa una asesoría cobrada por horas."""

    def __init__(self, identificador: str, costo_base: float, especialidad: str) -> None:
        self._especialidad = especialidad.strip()
        super().__init__(identificador, "Asesoría especializada", costo_base)

    def validar(self) -> None:
        super().validar()
        if not self._especialidad:
            raise DatoInvalidoError("La especialidad es obligatoria.")

    def calcular_costo(self, duracion: float, descuento: float = 0) -> float:
        subtotal = self._costo_base * float(duracion)
        return subtotal * (1 - float(descuento))

    def describir(self) -> str:
        return f"Asesoría en {self._especialidad}"

