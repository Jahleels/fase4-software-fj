"""Excepciones personalizadas del proyecto."""


class SistemaFJError(Exception):
    """Error general controlado por la aplicación."""


class DatoInvalidoError(SistemaFJError):
    """Se usa cuando un dato no cumple las validaciones."""


class ServicioNoDisponibleError(SistemaFJError):
    """Se usa cuando se intenta reservar un servicio no disponible."""


class ReservaInvalidaError(SistemaFJError):
    """Se usa cuando una reserva tiene información incorrecta."""


class OperacionNoPermitidaError(SistemaFJError):
    """Se usa cuando el estado actual impide una operación."""

