from datetime import date
from decimal import Decimal

import pytest

from nucleo.reglas_multa import (
    calcular_multa,
    dias_retraso,
    generar_multa,
    registrar_pago,
)
from nucleo.tipos import EstadoMulta, Multa, Prestamo


PRESTAMO = Prestamo(
    "p1", "u1", "e1", date(2026, 10, 1), date(2026, 10, 15)
)


def test_no_genera_dias_de_retraso_antes_o_en_la_fecha_limite():
    assert dias_retraso(date(2026, 10, 15), date(2026, 10, 15)) == 0
    assert dias_retraso(date(2026, 10, 15), date(2026, 10, 12)) == 0


def test_calcula_multa_con_importe_decimal():
    assert calcular_multa(
        PRESTAMO, date(2026, 10, 18), Decimal("1250.50")
    ) == Decimal("3751.50")
    assert calcular_multa(
        PRESTAMO, date(2026, 10, 15), Decimal("1250.50")
    ) == Decimal("0.00")


def test_rechaza_tarifa_negativa_y_registra_pago_una_sola_vez():
    with pytest.raises(ValueError, match="negativa"):
        calcular_multa(PRESTAMO, date(2026, 10, 18), Decimal("-1"))

    multa = Multa("m1", "p1", "u1", Decimal("100.00"))
    assert registrar_pago(multa).estado is EstadoMulta.PAGADA
    pagada = Multa(
        "m2", "p1", "u1", Decimal("100.00"), EstadoMulta.PAGADA
    )
    with pytest.raises(ValueError, match="ya está pagada"):
        registrar_pago(pagada)


def test_generar_multa_solo_para_prestamo_devuelto_con_retraso():
    devuelto = Prestamo(
        "p1", "u1", "e1", date(2026, 10, 1), date(2026, 10, 15),
        date(2026, 10, 18),
    )
    puntual = Prestamo(
        "p2", "u2", "e2", date(2026, 10, 1), date(2026, 10, 15),
        date(2026, 10, 15),
    )

    multa = generar_multa(devuelto, "m1", Decimal("1250.50"))

    assert multa is not None
    assert multa.importe == Decimal("3751.50")
    assert multa.lector_id == "u1"
    assert generar_multa(puntual, "m2", Decimal("1250.50")) is None
    with pytest.raises(ValueError, match="devolver"):
        generar_multa(PRESTAMO, "m3", Decimal("1"))
