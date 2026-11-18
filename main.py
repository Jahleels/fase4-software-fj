"""Punto de entrada del sistema Software FJ."""

from simulaciones import ejecutar_simulaciones
from utils.logger import obtener_logger


def main() -> None:
    """Inicia el programa y ejecuta las diez simulaciones."""

    logger = obtener_logger()
    logger.info("Inicio de la aplicación Software FJ")
    print("Sistema Software FJ - simulaciones de estabilidad")
    resultados = ejecutar_simulaciones()

    correctos = sum(resultado["estado"] == "CORRECTO" for resultado in resultados)
    controlados = sum(
        resultado["estado"] == "ERROR CONTROLADO" for resultado in resultados
    )
    inesperados = sum(
        resultado["estado"] == "ERROR INESPERADO" for resultado in resultados
    )

    print("\nResumen")
    print(f"Casos ejecutados: {len(resultados)}")
    print(f"Casos correctos: {correctos}")
    print(f"Errores controlados: {controlados}")
    print(f"Errores inesperados: {inesperados}")


if __name__ == "__main__":
    main()

