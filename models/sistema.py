"""Gestión en memoria de clientes, servicios y reservas."""

from exceptions import EntidadDuplicadaError, EntidadNoEncontradaError
from models.cliente import Cliente
from models.reserva import Reserva
from models.servicio import Servicio
from utils.logger import obtener_logger


class SistemaReservas:
    """Coordina el sistema sin utilizar una base de datos."""

    def __init__(self) -> None:
        self._clientes: list[Cliente] = []
        self._servicios: list[Servicio] = []
        self._reservas: list[Reserva] = []
        self._logger = obtener_logger()

    @property
    def clientes(self) -> list[Cliente]:
        return self._clientes.copy()

    @property
    def servicios(self) -> list[Servicio]:
        return self._servicios.copy()

    @property
    def reservas(self) -> list[Reserva]:
        return self._reservas.copy()

    def registrar_cliente(self, cliente: Cliente) -> None:
        if self._buscar(self._clientes, cliente.identificador, permitir_faltante=True):
            raise EntidadDuplicadaError("Ya existe un cliente con ese identificador.")
        self._clientes.append(cliente)
        self._logger.info("Cliente registrado: %s", cliente.identificador)

    def registrar_servicio(self, servicio: Servicio) -> None:
        if self._buscar(self._servicios, servicio.identificador, permitir_faltante=True):
            raise EntidadDuplicadaError("Ya existe un servicio con ese identificador.")
        self._servicios.append(servicio)
        self._logger.info("Servicio registrado: %s", servicio.identificador)

    def crear_reserva(
        self,
        identificador: str,
        cliente_id: str,
        servicio_id: str,
        duracion,
    ) -> Reserva:
        if self._buscar(self._reservas, identificador, permitir_faltante=True):
            raise EntidadDuplicadaError("Ya existe una reserva con ese identificador.")

        cliente = self._buscar(self._clientes, cliente_id)
        servicio = self._buscar(self._servicios, servicio_id)
        reserva = Reserva(identificador, cliente, servicio, duracion)
        self._reservas.append(reserva)
        self._logger.info("Reserva creada: %s", reserva.identificador)
        return reserva

    def confirmar_reserva(self, identificador: str) -> Reserva:
        reserva = self._buscar(self._reservas, identificador)
        reserva.confirmar()
        self._logger.info("Reserva confirmada: %s", reserva.identificador)
        return reserva

    def cancelar_reserva(self, identificador: str) -> Reserva:
        reserva = self._buscar(self._reservas, identificador)
        reserva.cancelar()
        self._logger.info("Reserva cancelada: %s", reserva.identificador)
        return reserva

    @staticmethod
    def _buscar(coleccion, identificador: str, permitir_faltante: bool = False):
        for entidad in coleccion:
            if entidad.identificador == identificador:
                return entidad

        if permitir_faltante:
            return None
        raise EntidadNoEncontradaError(
            f"No se encontró una entidad con identificador {identificador}."
        )
