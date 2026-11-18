"""Diez simulaciones válidas e inválidas solicitadas en la actividad."""

from collections.abc import Callable

from exceptions import SistemaFJError
from models import (
    AlquilerEquipo,
    AsesoriaEspecializada,
    Cliente,
    ReservaSala,
    SistemaReservas,
)
from utils.logger import obtener_logger


def ejecutar_caso(
    numero: int,
    nombre: str,
    operacion: Callable[[], str],
) -> dict:
    """Ejecuta un caso sin permitir que un error detenga los siguientes."""

    logger = obtener_logger()
    resultado = {"numero": numero, "nombre": nombre, "estado": ""}
    print(f"\nCaso {numero}: {nombre}")

    try:
        detalle = operacion()
    except SistemaFJError as error:
        resultado["estado"] = "ERROR CONTROLADO"
        logger.exception("Caso %s controlado: %s", numero, nombre)
        print(f"Resultado: error controlado - {error}")
    except Exception as error:
        resultado["estado"] = "ERROR INESPERADO"
        logger.exception("Caso %s inesperado: %s", numero, nombre)
        print(f"Resultado: error inesperado - {error}")
    else:
        resultado["estado"] = "CORRECTO"
        logger.info("Caso %s correcto: %s", numero, nombre)
        print(f"Resultado: correcto - {detalle}")
    finally:
        # Este mensaje demuestra que el bloque finally siempre se ejecuta.
        logger.info("Finalizó el caso %s", numero)

    return resultado


def ejecutar_simulaciones() -> list[dict]:
    """Ejecuta diez operaciones y devuelve un resumen de sus resultados."""

    sistema = SistemaReservas()

    def caso_1() -> str:
        sistema.registrar_cliente(
            Cliente("C001", "Ana Torres", "ana@example.com")
        )
        return "cliente válido registrado"

    def caso_2() -> str:
        sistema.registrar_cliente(Cliente("C002", "Luis", "correo-invalido"))
        return "este mensaje no debe mostrarse"

    def caso_3() -> str:
        sistema.registrar_cliente(
            Cliente("C001", "Ana Repetida", "otra@example.com")
        )
        return "este mensaje no debe mostrarse"

    def caso_4() -> str:
        sistema.registrar_servicio(ReservaSala("S001", 50000, 12))
        sistema.registrar_servicio(AlquilerEquipo("S002", 30000, "Portátil"))
        sistema.registrar_servicio(
            AsesoriaEspecializada("S003", 80000, "Python")
        )
        return "tres tipos de servicio registrados"

    def caso_5() -> str:
        # El texto produce ValueError y se encadena con DatoInvalidoError.
        sistema.registrar_servicio(ReservaSala("S004", "precio", 8))
        return "este mensaje no debe mostrarse"

    def caso_6() -> str:
        reserva = sistema.crear_reserva("R001", "C001", "S001", 2)
        sistema.confirmar_reserva("R001")
        return f"reserva confirmada por ${reserva.calcular_total(0.10):,.0f}"

    def caso_7() -> str:
        servicio = sistema.servicios[1]
        servicio.cambiar_disponibilidad(False)
        sistema.crear_reserva("R002", "C001", "S002", 3)
        sistema.confirmar_reserva("R002")
        return "este mensaje no debe mostrarse"

    def caso_8() -> str:
        sistema.crear_reserva("R003", "C001", "S003", -2)
        return "este mensaje no debe mostrarse"

    def caso_9() -> str:
        sistema.crear_reserva("R004", "C001", "S003", 1)
        sistema.cancelar_reserva("R004")
        sistema.cancelar_reserva("R004")
        return "este mensaje no debe mostrarse"

    def caso_10() -> str:
        reserva = sistema.crear_reserva("R005", "C001", "S003", 1.5)
        sistema.confirmar_reserva("R005")
        return f"asesoría confirmada por ${reserva.calcular_total():,.0f}"

    casos = [
        (1, "Registro válido de cliente", caso_1),
        (2, "Cliente con correo inválido", caso_2),
        (3, "Cliente duplicado", caso_3),
        (4, "Creación de los tres servicios", caso_4),
        (5, "Servicio con costo no numérico", caso_5),
        (6, "Reserva de sala exitosa", caso_6),
        (7, "Reserva de servicio no disponible", caso_7),
        (8, "Reserva con duración inválida", caso_8),
        (9, "Cancelación repetida", caso_9),
        (10, "Asesoría especializada exitosa", caso_10),
    ]

    return [ejecutar_caso(numero, nombre, funcion) for numero, nombre, funcion in casos]


if __name__ == "__main__":
    ejecutar_simulaciones()
