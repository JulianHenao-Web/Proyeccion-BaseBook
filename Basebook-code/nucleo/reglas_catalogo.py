"""Consultas puras del catálogo y disponibilidad de títulos."""

from collections.abc import Iterable

from nucleo.tipos import (
    DisponibilidadCatalogo,
    Ejemplar,
    EstadoEjemplar,
    Libro,
)


def buscar_libros(libros: Iterable[Libro], consulta: str) -> list[Libro]:
    """Busca por título, autor o categoría, sin distinguir mayúsculas."""
    termino = consulta.strip().casefold()
    if not termino:
        return []

    return [
        libro
        for libro in libros
        if libro.activo
        and (
            termino in libro.titulo.casefold()
            or any(termino in autor.casefold() for autor in libro.autores)
            or termino in libro.categoria.casefold()
        )
    ]


def disponibilidad_titulo(
    libro_id: str, ejemplares: Iterable[Ejemplar]
) -> DisponibilidadCatalogo:
    """Deriva el estado agregado de un título a partir de sus ejemplares."""
    estados = [
        ejemplar.estado
        for ejemplar in ejemplares
        if ejemplar.libro_id == libro_id
    ]
    if EstadoEjemplar.DISPONIBLE in estados:
        return DisponibilidadCatalogo.DISPONIBLE
    if EstadoEjemplar.RESERVADO in estados:
        return DisponibilidadCatalogo.RESERVADO
    if EstadoEjemplar.PRESTADO in estados:
        return DisponibilidadCatalogo.PRESTADO
    return DisponibilidadCatalogo.NO_DISPONIBLE
