"""Excepciones disponibles para el sistema."""

from .excepciones import (
    DatoInvalidoError,
    EntidadDuplicadaError,
    EntidadNoEncontradaError,
    OperacionNoPermitidaError,
    ReservaInvalidaError,
    ServicioNoDisponibleError,
    SistemaFJError,
)

__all__ = [
    "SistemaFJError",
    "DatoInvalidoError",
    "EntidadDuplicadaError",
    "EntidadNoEncontradaError",
    "ServicioNoDisponibleError",
    "ReservaInvalidaError",
    "OperacionNoPermitidaError",
]

