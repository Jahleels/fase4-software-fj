"""Excepciones disponibles para el sistema."""

from .excepciones import (
    DatoInvalidoError,
    OperacionNoPermitidaError,
    ReservaInvalidaError,
    ServicioNoDisponibleError,
    SistemaFJError,
)

__all__ = [
    "SistemaFJError",
    "DatoInvalidoError",
    "ServicioNoDisponibleError",
    "ReservaInvalidaError",
    "OperacionNoPermitidaError",
]

