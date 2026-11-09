"""Configuración central del archivo de eventos y errores."""

import logging
from pathlib import Path


def obtener_logger() -> logging.Logger:
    """Crea el logger una sola vez y lo devuelve para todo el proyecto."""

    carpeta_logs = Path(__file__).resolve().parent.parent / "logs"
    carpeta_logs.mkdir(exist_ok=True)

    logging.basicConfig(
        filename=carpeta_logs / "software_fj.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        encoding="utf-8",
    )
    return logging.getLogger("software_fj")

