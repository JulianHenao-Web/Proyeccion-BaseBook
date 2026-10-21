from datetime import date

import pytest

from nucleo.reglas_reserva import (
    asignar_siguiente_reserva,
    atender_reserva,
    cancelar_reserva,
    crear_reserva,
    devolver_y_asignar_reserva,
)
from nucleo.tipos import (
    Ejemplar,
    EstadoEjemplar,
    EstadoReserva,
    Prestamo,
    Reserva,
)


EJEMPLAR_PRESTADO = Ejemplar("e1", "b1", "INV-1", EstadoEjemplar.PRESTADO)
RESERVA_U1 = Reserva("r1", "u1", "b1", date(2026, 10, 1))
RESERVA_U2 = Reserva("r2", "u2", "b1", date(2026, 10, 2))


def test_crea_reserva_si_titulo_no_tiene_copias_disponibles():
    assert crear_reserva(RESERVA_U1, [EJEMPLAR_PRESTADO], []) == RESERVA_U1


def test_no_crea_reserva_si_hay_ejemplar_libre_o_no_hay_ejemplares_activos():
    disponible = Ejemplar("e2", "b1", "INV-2")
    retirado = Ejemplar("e3", "b1", "INV-3", EstadoEjemplar.RETIRADO)

    with pytest.raises(ValueError, match="disponibles"):
        crear_reserva(RESERVA_U1, [EJEMPLAR_PRESTADO, disponible], [])
    with pytest.raises(ValueError, match="no tiene ejemplares"):
        crear_reserva(RESERVA_U1, [retirado], [])


def test_no_permite_reservas_activas_duplicadas_por_lector_y_titulo():
    with pytest.raises(ValueError, match="reserva activa"):
        crear_reserva(RESERVA_U1, [EJEMPLAR_PRESTADO], [RESERVA_U1])


def test_asigna_ejemplar_al_primero_en_cola_fifo_y_desempata_por_id():
    disponible = Ejemplar("e1", "b1", "INV-1")
    reserva_temprana = Reserva("r2", "u2", "b1", date(2026, 10, 1))
    reserva_misma_fecha = Reserva("r1", "u1", "b1", date(2026, 10, 1))

    ejemplar, reservas, siguiente = asignar_siguiente_reserva(
        disponible, [reserva_temprana, reserva_misma_fecha]
    )

    assert siguiente is not None
    assert siguiente.id == "r1"
    assert siguiente.estado is EstadoReserva.LISTA
    assert siguiente.ejemplar_id == "e1"
    assert ejemplar.estado is EstadoEjemplar.RESERVADO
    assert reservas[0] == reserva_temprana


def test_cancelar_reserva_lista_libera_su_asignacion():
    reserva_lista = Reserva(
        "r1", "u1", "b1", date(2026, 10, 1), EstadoReserva.LISTA, "e1"
    )
    ejemplar = Ejemplar("e1", "b1", "INV-1", EstadoEjemplar.RESERVADO)

    cancelada, disponible, reservas, siguiente = cancelar_reserva(
        reserva_lista, ejemplar, [reserva_lista]
    )

    assert cancelada.estado is EstadoReserva.CANCELADA
    assert cancelada.ejemplar_id is None
    assert disponible is not None
    assert disponible.estado is EstadoEjemplar.DISPONIBLE
    assert reservas == [cancelada]
    assert siguiente is None


def test_cancelar_reserva_lista_asigna_ejemplar_a_siguiente_lector():
    reserva_lista = Reserva(
        "r1", "u1", "b1", date(2026, 10, 1), EstadoReserva.LISTA, "e1"
    )
    reserva_en_cola = Reserva("r2", "u2", "b1", date(2026, 10, 2))
    ejemplar = Ejemplar("e1", "b1", "INV-1", EstadoEjemplar.RESERVADO)

    cancelada, reservado, reservas, siguiente = cancelar_reserva(
        reserva_lista, ejemplar, [reserva_lista, reserva_en_cola]
    )

    assert cancelada.estado is EstadoReserva.CANCELADA
    assert reservado is not None
    assert reservado.estado is EstadoEjemplar.RESERVADO
    assert siguiente is not None
    assert siguiente.id == "r2"
    assert reservas[0] == cancelada


def test_devolucion_asigna_el_ejemplar_a_la_siguiente_reserva():
    prestamo = Prestamo(
        "p1", "u0", "e1", date(2026, 9, 15), date(2026, 10, 1)
    )
    ejemplar = Ejemplar("e1", "b1", "INV-1", EstadoEjemplar.PRESTADO)

    devuelto, reservado, reservas, siguiente = devolver_y_asignar_reserva(
        prestamo, ejemplar, date(2026, 10, 1), [RESERVA_U1, RESERVA_U2]
    )

    assert devuelto.estado.value == "devuelto"
    assert reservado.estado is EstadoEjemplar.RESERVADO
    assert siguiente is not None
    assert siguiente.id == "r1"
    assert reservas[0] == siguiente


def test_atender_reserva_crea_prestamo_para_lector_en_cola():
    reserva_lista = Reserva(
        "r1", "u1", "b1", date(2026, 10, 1), EstadoReserva.LISTA, "e1"
    )
    ejemplar = Ejemplar("e1", "b1", "INV-1", EstadoEjemplar.RESERVADO)

    atendida, prestado, prestamo = atender_reserva(
        reserva_lista, ejemplar, date(2026, 10, 2), date(2026, 10, 16), "p1"
    )

    assert atendida.estado is EstadoReserva.ATENDIDA
    assert prestado.estado is EstadoEjemplar.PRESTADO
    assert prestamo.lector_id == "u1"
    assert prestamo.ejemplar_id == "e1"
