from datetime import date

import pytest

from nucleo.reglas_prestamo import (
    aprobar_solicitud,
    cancelar_solicitud,
    crear_solicitud,
    devolver_prestamo,
    rechazar_solicitud,
)
from nucleo.tipos import (
    Ejemplar,
    EstadoEjemplar,
    EstadoSolicitud,
    Prestamo,
    SolicitudPrestamo,
)


SOLICITUD = SolicitudPrestamo("s1", "u1", "b1", date(2026, 10, 1))
EJEMPLAR = Ejemplar("e1", "b1", "INV-1")


def test_aprobar_solicitud_crea_prestamo_y_ocupa_ejemplar():
    aprobada, ejemplar, prestamo = aprobar_solicitud(
        SOLICITUD, EJEMPLAR, "p1", date(2026, 10, 2), date(2026, 10, 16)
    )

    assert aprobada.estado is EstadoSolicitud.APROBADA
    assert ejemplar.estado is EstadoEjemplar.PRESTADO
    assert prestamo.lector_id == "u1"
    assert prestamo.ejemplar_id == "e1"
    assert SOLICITUD.estado is EstadoSolicitud.PENDIENTE
    assert EJEMPLAR.estado is EstadoEjemplar.DISPONIBLE


def test_crea_solicitud_si_hay_ejemplar_disponible_y_no_es_duplicada():
    assert crear_solicitud(SOLICITUD, [EJEMPLAR]) == SOLICITUD

    with pytest.raises(ValueError, match="pendiente"):
        crear_solicitud(SOLICITUD, [EJEMPLAR], [SOLICITUD])
    with pytest.raises(ValueError, match="reserva"):
        crear_solicitud(
            SOLICITUD,
            [Ejemplar("e2", "b1", "INV-2", EstadoEjemplar.PRESTADO)],
        )


def test_solo_puede_cancelarse_una_solicitud_pendiente():
    assert cancelar_solicitud(SOLICITUD).estado is EstadoSolicitud.CANCELADA
    aprobada = SolicitudPrestamo(
        "s2", "u1", "b1", date(2026, 10, 1), EstadoSolicitud.APROBADA
    )

    with pytest.raises(ValueError, match="pendientes"):
        cancelar_solicitud(aprobada)


@pytest.mark.parametrize(
    ("ejemplar", "fecha_prestamo", "fecha_limite", "mensaje"),
    [
        (Ejemplar("e1", "b1", "INV-1", EstadoEjemplar.PRESTADO),
         date(2026, 10, 2), date(2026, 10, 16), "no está disponible"),
        (Ejemplar("e2", "b2", "INV-2"),
         date(2026, 10, 2), date(2026, 10, 16), "no pertenece"),
        (EJEMPLAR, date(2026, 9, 30), date(2026, 10, 16), "preceder"),
        (EJEMPLAR, date(2026, 10, 2), date(2026, 10, 2), "posterior"),
    ],
)
def test_aprobar_solicitud_rechaza_datos_inconsistentes(
    ejemplar, fecha_prestamo, fecha_limite, mensaje
):
    with pytest.raises(ValueError, match=mensaje):
        aprobar_solicitud(
            SOLICITUD, ejemplar, "p1", fecha_prestamo, fecha_limite
        )


def test_solo_puede_rechazarse_una_solicitud_pendiente():
    assert rechazar_solicitud(SOLICITUD).estado is EstadoSolicitud.RECHAZADA
    aprobada = SolicitudPrestamo(
        "s2", "u1", "b1", date(2026, 10, 1), EstadoSolicitud.APROBADA
    )

    with pytest.raises(ValueError, match="pendientes"):
        rechazar_solicitud(aprobada)


def test_devolver_prestamo_libera_ejemplar():
    prestamo = Prestamo("p1", "u1", "e1", date(2026, 10, 1), date(2026, 10, 15))
    ejemplar = Ejemplar("e1", "b1", "INV-1", EstadoEjemplar.PRESTADO)

    devuelto, disponible = devolver_prestamo(
        prestamo, ejemplar, date(2026, 10, 15)
    )

    assert devuelto.fecha_devolucion == date(2026, 10, 15)
    assert devuelto.estado.value == "devuelto"
    assert disponible.estado is EstadoEjemplar.DISPONIBLE


def test_no_permite_devolver_otra_vez_ni_un_ejemplar_ajeno():
    prestamo = Prestamo(
        "p1", "u1", "e1", date(2026, 10, 1), date(2026, 10, 15),
        date(2026, 10, 14),
    )
    ejemplar_prestado = Ejemplar("e1", "b1", "INV-1", EstadoEjemplar.PRESTADO)
    otro_prestamo = Prestamo("p2", "u1", "e2", date(2026, 10, 1), date(2026, 10, 15))

    with pytest.raises(ValueError, match="ya fue devuelto"):
        devolver_prestamo(prestamo, ejemplar_prestado, date(2026, 10, 16))
    with pytest.raises(ValueError, match="no corresponde"):
        devolver_prestamo(otro_prestamo, ejemplar_prestado, date(2026, 10, 16))
