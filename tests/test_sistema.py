"""Pruebas automáticas de la lógica principal."""

import unittest

from exceptions import (
    DatoInvalidoError,
    EntidadDuplicadaError,
    ReservaInvalidaError,
    ServicioNoDisponibleError,
)
from models import Cliente, ReservaSala, SistemaReservas
from simulaciones import ejecutar_simulaciones


class SistemaFJTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sistema = SistemaReservas()
        self.cliente = Cliente("C1", "Jahleel Solano", "jahleel@example.com")
        self.servicio = ReservaSala("S1", 50000, 10)
        self.sistema.registrar_cliente(self.cliente)
        self.sistema.registrar_servicio(self.servicio)

    def test_cliente_invalido(self) -> None:
        with self.assertRaises(DatoInvalidoError):
            Cliente("C2", "Lu", "correo")

    def test_no_permite_cliente_duplicado(self) -> None:
        with self.assertRaises(EntidadDuplicadaError):
            self.sistema.registrar_cliente(
                Cliente("C1", "Otro Cliente", "otro@example.com")
            )

    def test_calculo_polimorfico_con_descuento(self) -> None:
        self.assertEqual(self.servicio.calcular_costo(2, 0.1), 90000)

    def test_reserva_con_duracion_invalida(self) -> None:
        with self.assertRaises(ReservaInvalidaError):
            self.sistema.crear_reserva("R1", "C1", "S1", 0)

    def test_servicio_no_disponible(self) -> None:
        self.servicio.cambiar_disponibilidad(False)
        self.sistema.crear_reserva("R1", "C1", "S1", 1)
        with self.assertRaises(ServicioNoDisponibleError):
            self.sistema.confirmar_reserva("R1")

    def test_diez_simulaciones_sin_error_inesperado(self) -> None:
        resultados = ejecutar_simulaciones()
        self.assertEqual(len(resultados), 10)
        self.assertNotIn(
            "ERROR INESPERADO", [resultado["estado"] for resultado in resultados]
        )


if __name__ == "__main__":
    unittest.main()
