"""Configuración central del archivo de eventos y errores."""

import logging
from pathlib import Path


def obtener_logger() -> logging.Logger:
    """Crea el logger una sola vez y lo devuelve para todo el proyecto."""

    carpeta_logs = Path(__file__).resolve().parent.parent / "logs"
    carpeta_logs.mkdir(exist_ok=True)

    logger = logging.getLogger("software_fj")
    logger.setLevel(logging.INFO)

    # Evita agregar el mismo manejador cada vez que se solicita el logger.
    if not logger.handlers:
        manejador = logging.FileHandler(
            carpeta_logs / "software_fj.log", encoding="utf-8"
        )
        formato = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
        manejador.setFormatter(formato)
        logger.addHandler(manejador)

    return logger

