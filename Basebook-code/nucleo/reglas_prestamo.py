"""Reglas puras para solicitar, aprobar, rechazar y devolver préstamos."""

from collections.abc import Iterable
from dataclasses import replace
from datetime import date

from nucleo.tipos import (
    Ejemplar,
    EstadoEjemplar,
    EstadoPrestamo,
    EstadoSolicitud,
    Prestamo,
    SolicitudPrestamo,
)


def aprobar_solicitud(
    solicitud: SolicitudPrestamo,
    ejemplar: Ejemplar,
    prestamo_id: str,
    fecha_prestamo: date,
    fecha_limite: date,
) -> tuple[SolicitudPrestamo, Ejemplar, Prestamo]:
    """Aprueba una solicitud y asigna un ejemplar disponible del mismo título."""
    if solicitud.estado is not EstadoSolicitud.PENDIENTE:
        raise ValueError("Solo se pueden aprobar solicitudes pendientes.")
    if ejemplar.estado is not EstadoEjemplar.DISPONIBLE:
        raise ValueError("El ejemplar no está disponible.")
    if ejemplar.libro_id != solicitud.libro_id:
        raise ValueError("El ejemplar no pertenece al título solicitado.")
    if fecha_prestamo < solicitud.fecha_solicitud:
        raise ValueError("El préstamo no puede preceder a la solicitud.")
    if fecha_limite <= fecha_prestamo:
        raise ValueError("La fecha límite debe ser posterior al préstamo.")

    solicitud_aprobada = replace(solicitud, estado=EstadoSolicitud.APROBADA)
    ejemplar_prestado = replace(ejemplar, estado=EstadoEjemplar.PRESTADO)
    prestamo = Prestamo(
        id=prestamo_id,
        lector_id=solicitud.lector_id,
        ejemplar_id=ejemplar.id,
        fecha_prestamo=fecha_prestamo,
        fecha_limite=fecha_limite,
    )
    return solicitud_aprobada, ejemplar_prestado, prestamo


def crear_solicitud(
    solicitud: SolicitudPrestamo,
    ejemplares: Iterable[Ejemplar],
    solicitudes_existentes: Iterable[SolicitudPrestamo] = (),
) -> SolicitudPrestamo:
    if solicitud.estado is not EstadoSolicitud.PENDIENTE:
        raise ValueError("La nueva solicitud debe iniciar pendiente.")
    if not any(
        ejemplar.libro_id == solicitud.libro_id
        and ejemplar.estado is EstadoEjemplar.DISPONIBLE
        for ejemplar in ejemplares
    ):
        raise ValueError("No hay ejemplares disponibles; debe crear una reserva.")
    if any(
        existente.lector_id == solicitud.lector_id
        and existente.libro_id == solicitud.libro_id
        and existente.estado is EstadoSolicitud.PENDIENTE
        for existente in solicitudes_existentes
    ):
        raise ValueError("El lector ya tiene una solicitud pendiente para este título.")
    return solicitud


def rechazar_solicitud(solicitud: SolicitudPrestamo) -> SolicitudPrestamo:
    if solicitud.estado is not EstadoSolicitud.PENDIENTE:
        raise ValueError("Solo se pueden rechazar solicitudes pendientes.")
    return replace(solicitud, estado=EstadoSolicitud.RECHAZADA)


def cancelar_solicitud(solicitud: SolicitudPrestamo) -> SolicitudPrestamo:
    if solicitud.estado is not EstadoSolicitud.PENDIENTE:
        raise ValueError("Solo se pueden cancelar solicitudes pendientes.")
    return replace(solicitud, estado=EstadoSolicitud.CANCELADA)


def devolver_prestamo(
    prestamo: Prestamo, ejemplar: Ejemplar, fecha_devolucion: date
) -> tuple[Prestamo, Ejemplar]:
    if prestamo.estado is not EstadoPrestamo.ACTIVO:
        raise ValueError("El préstamo ya fue devuelto.")
    if ejemplar.estado is not EstadoEjemplar.PRESTADO:
        raise ValueError("El ejemplar no está marcado como prestado.")
    if ejemplar.id != prestamo.ejemplar_id:
        raise ValueError("El ejemplar no corresponde al préstamo.")
    if fecha_devolucion < prestamo.fecha_prestamo:
        raise ValueError("La devolución no puede preceder al préstamo.")

    prestamo_devuelto = replace(prestamo, fecha_devolucion=fecha_devolucion)
    ejemplar_disponible = replace(ejemplar, estado=EstadoEjemplar.DISPONIBLE)
    return prestamo_devuelto, ejemplar_disponible
