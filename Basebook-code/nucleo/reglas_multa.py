"""Cálculo y pago de multas por retraso."""

from dataclasses import replace
from datetime import date
from decimal import Decimal

from nucleo.tipos import EstadoMulta, Multa, EstadoPrestamo, Prestamo


def dias_retraso(fecha_limite: date, fecha_devolucion: date) -> int:
    return max(0, (fecha_devolucion - fecha_limite).days)


def calcular_multa(
    prestamo: Prestamo, fecha_devolucion: date, tarifa_diaria: Decimal
) -> Decimal:
    if tarifa_diaria < Decimal("0"):
        raise ValueError("La tarifa diaria no puede ser negativa.")
    dias = dias_retraso(prestamo.fecha_limite, fecha_devolucion)
    return Decimal(dias) * tarifa_diaria


def generar_multa(
    prestamo: Prestamo, multa_id: str, tarifa_diaria: Decimal
) -> Multa | None:
    if prestamo.estado is not EstadoPrestamo.DEVUELTO:
        raise ValueError("Solo se generan multas al devolver el préstamo.")
    if prestamo.fecha_devolucion is None:
        raise ValueError("El préstamo devuelto debe tener fecha de devolución.")
    importe = calcular_multa(
        prestamo, prestamo.fecha_devolucion, tarifa_diaria
    )
    if importe == Decimal("0"):
        return None
    return Multa(
        id=multa_id,
        prestamo_id=prestamo.id,
        lector_id=prestamo.lector_id,
        importe=importe,
    )


def registrar_pago(multa: Multa) -> Multa:
    if multa.estado is EstadoMulta.PAGADA:
        raise ValueError("La multa ya está pagada.")
    return replace(multa, estado=EstadoMulta.PAGADA)
