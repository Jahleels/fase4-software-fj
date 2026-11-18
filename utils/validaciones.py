"""Funciones de validación que pueden reutilizar todas las clases."""

from exceptions import DatoInvalidoError


def convertir_numero_positivo(valor, nombre: str) -> float:
    """Convierte un valor y encadena el error original si no es numérico."""

    try:
        numero = float(valor)
    except (TypeError, ValueError) as error_original:
        raise DatoInvalidoError(f"{nombre} debe ser un número válido.") from error_original

    if numero <= 0:
        raise DatoInvalidoError(f"{nombre} debe ser mayor que cero.")
    return numero


def validar_descuento(valor) -> float:
    """Comprueba que el descuento esté entre cero y uno."""

    try:
        descuento = float(valor)
    except (TypeError, ValueError) as error_original:
        raise DatoInvalidoError("El descuento debe ser numérico.") from error_original

    if descuento < 0 or descuento > 1:
        raise DatoInvalidoError("El descuento debe estar entre 0 y 1.")
    return descuento
