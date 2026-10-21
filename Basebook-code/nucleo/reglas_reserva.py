"""Reglas puras de cola y asignación de reservas."""

from dataclasses import replace
from collections.abc import Iterable
from datetime import date

from nucleo.tipos import (
    Ejemplar,
    EstadoEjemplar,
    EstadoReserva,
    Prestamo,
    Reserva,
)
from nucleo.reglas_prestamo import devolver_prestamo


def crear_reserva(
    reserva: Reserva,
    ejemplares: Iterable[Ejemplar],
    reservas_existentes: Iterable[Reserva],
) -> Reserva:
    """Crea una reserva solo si no hay ejemplares libres ni duplicados activos."""
    ejemplares_titulo = [
        ejemplar
        for ejemplar in ejemplares
        if ejemplar.libro_id == reserva.libro_id
    ]
    if any(
        ejemplar.estado is EstadoEjemplar.DISPONIBLE
        for ejemplar in ejemplares_titulo
    ):
        raise ValueError("No se puede reservar un título con ejemplares disponibles.")
    if not any(
        ejemplar.estado
        in (EstadoEjemplar.PRESTADO, EstadoEjemplar.RESERVADO)
        for ejemplar in ejemplares_titulo
    ):
        raise ValueError("El título no tiene ejemplares que puedan reservarse.")
    if reserva.estado is not EstadoReserva.EN_COLA or reserva.ejemplar_id is not None:
        raise ValueError("La nueva reserva debe iniciar en estado de cola.")
    if any(
        existente.lector_id == reserva.lector_id
        and existente.libro_id == reserva.libro_id
        and existente.estado in (EstadoReserva.EN_COLA, EstadoReserva.LISTA)
        for existente in reservas_existentes
    ):
        raise ValueError("El lector ya tiene una reserva activa para este título.")
    return reserva


def asignar_siguiente_reserva(
    ejemplar: Ejemplar, reservas: Iterable[Reserva]
) -> tuple[Ejemplar, list[Reserva], Reserva | None]:
    """Asigna un ejemplar libre a la reserva en cola más antigua."""
    if ejemplar.estado is not EstadoEjemplar.DISPONIBLE:
        raise ValueError("Solo se pueden asignar ejemplares disponibles.")

    reservas_actualizadas = list(reservas)
    candidatas = [
        reserva
        for reserva in reservas_actualizadas
        if reserva.libro_id == ejemplar.libro_id
        and reserva.estado is EstadoReserva.EN_COLA
    ]
    if not candidatas:
        return ejemplar, reservas_actualizadas, None

    siguiente = min(candidatas, key=lambda r: (r.fecha_solicitud, r.id))
    reserva_lista = replace(
        siguiente, estado=EstadoReserva.LISTA, ejemplar_id=ejemplar.id
    )
    reservas_actualizadas = [
        reserva_lista if reserva.id == siguiente.id else reserva
        for reserva in reservas_actualizadas
    ]
    ejemplar_reservado = replace(ejemplar, estado=EstadoEjemplar.RESERVADO)
    return ejemplar_reservado, reservas_actualizadas, reserva_lista


def devolver_y_asignar_reserva(
    prestamo: Prestamo,
    ejemplar: Ejemplar,
    fecha_devolucion: date,
    reservas: Iterable[Reserva],
) -> tuple[Prestamo, Ejemplar, list[Reserva], Reserva | None]:
    """Devuelve un ejemplar y lo asigna a la siguiente reserva, si existe."""
    prestamo_devuelto, ejemplar_disponible = devolver_prestamo(
        prestamo, ejemplar, fecha_devolucion
    )
    ejemplar_actualizado, reservas_actualizadas, siguiente = (
        asignar_siguiente_reserva(ejemplar_disponible, reservas)
    )
    return (
        prestamo_devuelto,
        ejemplar_actualizado,
        reservas_actualizadas,
        siguiente,
    )


def cancelar_reserva(
    reserva: Reserva,
    ejemplar: Ejemplar | None = None,
    reservas: Iterable[Reserva] = (),
) -> tuple[Reserva, Ejemplar | None, list[Reserva], Reserva | None]:
    if reserva.estado not in (EstadoReserva.EN_COLA, EstadoReserva.LISTA):
        raise ValueError("Solo se pueden cancelar reservas activas.")
    reservas_actualizadas = [
        replace(item, estado=EstadoReserva.CANCELADA, ejemplar_id=None)
        if item.id == reserva.id
        else item
        for item in reservas
    ]
    reserva_cancelada = replace(
        reserva, estado=EstadoReserva.CANCELADA, ejemplar_id=None
    )
    if reserva.estado is EstadoReserva.EN_COLA:
        if ejemplar is not None:
            raise ValueError("Una reserva en cola no tiene un ejemplar asignado.")
        if not any(item.id == reserva.id for item in reservas_actualizadas):
            reservas_actualizadas.append(reserva_cancelada)
        return reserva_cancelada, None, reservas_actualizadas, None
    if ejemplar is None:
        raise ValueError("Se requiere el ejemplar asignado para cancelar la reserva.")
    if ejemplar.id != reserva.ejemplar_id:
        raise ValueError("El ejemplar no corresponde a la reserva.")
    if ejemplar.estado is not EstadoEjemplar.RESERVADO:
        raise ValueError("El ejemplar no está reservado.")
    ejemplar_disponible = replace(ejemplar, estado=EstadoEjemplar.DISPONIBLE)
    ejemplar_actualizado, reservas_actualizadas, siguiente = (
        asignar_siguiente_reserva(ejemplar_disponible, reservas_actualizadas)
    )
    if not any(item.id == reserva.id for item in reservas_actualizadas):
        reservas_actualizadas.append(reserva_cancelada)
    return (
        reserva_cancelada,
        ejemplar_actualizado,
        reservas_actualizadas,
        siguiente,
    )


def atender_reserva(
    reserva: Reserva,
    ejemplar: Ejemplar,
    fecha_prestamo: date,
    fecha_limite: date,
    prestamo_id: str,
) -> tuple[Reserva, Ejemplar, Prestamo]:
    if reserva.estado is not EstadoReserva.LISTA:
        raise ValueError("La reserva debe estar lista para ser atendida.")
    if reserva.ejemplar_id != ejemplar.id:
        raise ValueError("El ejemplar no corresponde a la reserva.")
    if ejemplar.estado is not EstadoEjemplar.RESERVADO:
        raise ValueError("El ejemplar no está reservado.")
    if fecha_limite <= fecha_prestamo:
        raise ValueError("La fecha límite debe ser posterior al préstamo.")
    if fecha_prestamo < reserva.fecha_solicitud:
        raise ValueError("El préstamo no puede preceder a la reserva.")

    reserva_atendida = replace(reserva, estado=EstadoReserva.ATENDIDA)
    ejemplar_prestado = replace(ejemplar, estado=EstadoEjemplar.PRESTADO)
    prestamo = Prestamo(
        id=prestamo_id,
        lector_id=reserva.lector_id,
        ejemplar_id=ejemplar.id,
        fecha_prestamo=fecha_prestamo,
        fecha_limite=fecha_limite,
    )
    return reserva_atendida, ejemplar_prestado, prestamo
