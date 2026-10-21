from nucleo.reglas_catalogo import buscar_libros, disponibilidad_titulo
from nucleo.tipos import (
    DisponibilidadCatalogo,
    Ejemplar,
    EstadoEjemplar,
    Libro,
)


def test_busca_por_titulo_autor_y_categoria_sin_distinguir_mayusculas():
    libro = Libro("b1", "Cien años de soledad", ("Gabriel García Márquez",), "Novela")

    assert buscar_libros([libro], "CIEN") == [libro]
    assert buscar_libros([libro], "garcía") == [libro]
    assert buscar_libros([libro], "novela") == [libro]


def test_no_incluye_libros_inactivos_ni_consulta_vacia():
    libro = Libro("b1", "Título", ("Autor",), "Categoría", activo=False)

    assert buscar_libros([libro], "Título") == []
    assert buscar_libros([libro], "  ") == []


def test_disponibilidad_se_deriva_de_los_ejemplares_del_titulo():
    ejemplares = [
        Ejemplar("e1", "b1", "A1", EstadoEjemplar.PRESTADO),
        Ejemplar("e2", "b1", "A2", EstadoEjemplar.DISPONIBLE),
        Ejemplar("e3", "b2", "B1", EstadoEjemplar.RESERVADO),
    ]

    assert disponibilidad_titulo("b1", ejemplares) is DisponibilidadCatalogo.DISPONIBLE
    assert (
        disponibilidad_titulo(
            "b1", [Ejemplar("e1", "b1", "A1", EstadoEjemplar.PRESTADO)]
        )
        is DisponibilidadCatalogo.PRESTADO
    )
    assert disponibilidad_titulo("b3", ejemplares) is DisponibilidadCatalogo.NO_DISPONIBLE


def test_reservado_prevalece_sobre_prestado_si_no_hay_disponibles():
    ejemplares = [
        Ejemplar("e1", "b1", "A1", EstadoEjemplar.PRESTADO),
        Ejemplar("e2", "b1", "A2", EstadoEjemplar.RESERVADO),
    ]

    assert disponibilidad_titulo("b1", ejemplares) is DisponibilidadCatalogo.RESERVADO
