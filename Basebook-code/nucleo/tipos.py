"""Tipos inmutables del dominio de biblioteca."""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from enum import Enum


class EstadoEjemplar(str, Enum):
    DISPONIBLE = "disponible"
    PRESTADO = "prestado"
    RESERVADO = "reservado"
    RETIRADO = "retirado"


class EstadoSolicitud(str, Enum):
    PENDIENTE = "pendiente"
    APROBADA = "aprobada"
    RECHAZADA = "rechazada"
    CANCELADA = "cancelada"


class EstadoReserva(str, Enum):
    EN_COLA = "en_cola"
    LISTA = "lista"
    ATENDIDA = "atendida"
    CANCELADA = "cancelada"


class EstadoPrestamo(str, Enum):
    ACTIVO = "activo"
    DEVUELTO = "devuelto"


class EstadoMulta(str, Enum):
    PENDIENTE = "pendiente"
    PAGADA = "pagada"


class DisponibilidadCatalogo(str, Enum):
    DISPONIBLE = "disponible"
    RESERVADO = "reservado"
    PRESTADO = "prestado"
    NO_DISPONIBLE = "no_disponible"


@dataclass(frozen=True)
class Libro:
    id: str
    titulo: str
    autores: tuple[str, ...]
    categoria: str
    activo: bool = True


@dataclass(frozen=True)
class Ejemplar:
    id: str
    libro_id: str
    codigo_inventario: str
    estado: EstadoEjemplar = EstadoEjemplar.DISPONIBLE


@dataclass(frozen=True)
class SolicitudPrestamo:
    id: str
    lector_id: str
    libro_id: str
    fecha_solicitud: date
    estado: EstadoSolicitud = EstadoSolicitud.PENDIENTE


@dataclass(frozen=True)
class Prestamo:
    id: str
    lector_id: str
    ejemplar_id: str
    fecha_prestamo: date
    fecha_limite: date
    fecha_devolucion: date | None = None

    @property
    def estado(self) -> EstadoPrestamo:
        if self.fecha_devolucion is None:
            return EstadoPrestamo.ACTIVO
        return EstadoPrestamo.DEVUELTO


@dataclass(frozen=True)
class Reserva:
    id: str
    lector_id: str
    libro_id: str
    fecha_solicitud: date
    estado: EstadoReserva = EstadoReserva.EN_COLA
    ejemplar_id: str | None = None


@dataclass(frozen=True)
class Multa:
    id: str
    prestamo_id: str
    lector_id: str
    importe: Decimal
    estado: EstadoMulta = EstadoMulta.PENDIENTE
