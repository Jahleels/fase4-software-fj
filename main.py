"""Punto de entrada del sistema Software FJ."""

from utils.logger import obtener_logger


def main() -> None:
    """Inicia el programa. Las simulaciones se agregarán por etapas."""

    logger = obtener_logger()
    logger.info("Inicio de la aplicación Software FJ")
    print("Sistema Software FJ listo para continuar su desarrollo.")


if __name__ == "__main__":
    main()

