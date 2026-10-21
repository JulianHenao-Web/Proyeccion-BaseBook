# BaseBook: resumen del proyecto

Este documento sintetiza las decisiones y requisitos principales de
[Proyecto Integrador - BaseBook.md](../Proyecto%20Integrador%20-%20BaseBook.md).
El documento original se conserva como fuente detallada del análisis.

## Propósito y alcance

BaseBook es una aplicación web para centralizar la gestión de una biblioteca
universitaria pequeña o mediana. Su objetivo es mantener organizado el catálogo,
los usuarios, préstamos, devoluciones, reservas y multas, y ofrecer información
consistente sobre la disponibilidad de los libros.

El sistema está dirigido a una biblioteca atendida por un equipo reducido y
accesible desde navegadores web. Los reportes avanzados y las notificaciones se
plantean como posibles ampliaciones. La primera versión sí manejará múltiples
ejemplares físicos por título.

## Actores y permisos

- **Lector:** crea su cuenta, consulta y busca el catálogo por título, autor o
  categoría, consulta disponibilidad, solicita préstamos y reservas, y revisa
  únicamente sus propios préstamos y multas.
- **Bibliotecario:** administra el catálogo; consulta usuarios, disponibilidad
  y préstamos; registra préstamos y devoluciones; gestiona reservas y multas;
  y registra pagos.
- **Administrador:** registra y administra usuarios, asigna roles y configura
  parámetros generales, como la duración estándar de un préstamo y el valor
  diario de la multa. No administra el catálogo, préstamos ni reservas.

El acceso debe estar limitado por rol. El registro público crea cuentas de
Lector; la asignación de roles privilegiados corresponde al Administrador.

## Funcionalidades

1. Registro de lectores, autenticación y cierre de sesión.
2. Gestión y búsqueda del catálogo, incluida la consulta de disponibilidad.
3. Administración de usuarios y roles.
4. Solicitud y registro formal de préstamos, con fechas y estado.
5. Registro de devoluciones y actualización de disponibilidad.
6. Solicitud y gestión de reservas.
7. Cálculo de retrasos, generación de multas y registro de pagos.
8. Consulta de préstamos y supervisión de préstamos activos.
9. Configuración del período de préstamo y el valor diario de la multa.

La disponibilidad debe mantenerse consistente con los préstamos, devoluciones
y reservas. Las multas deben reflejar correctamente si están pendientes o
pagadas.

## Requisitos de calidad

- Interfaz clara y opciones organizadas según el rol.
- Tiempo objetivo aproximado de respuesta de hasta tres segundos para consultas
  habituales en condiciones normales.
- Protección de información y control de acceso.
- Integridad y consistencia de datos en operaciones relacionadas.
- Disponibilidad durante el horario de operación de la biblioteca.
- Compatibilidad con navegadores web modernos.
- Código modular y mantenible, que permita incorporar funciones futuras.

## Arquitectura y tecnologías propuestas

Aplicación web cliente-servidor en **Python y Flask**, con una base de datos
relacional **Supabase**. La arquitectura separa responsabilidades en tres
capas:

| Capa | Carpeta | Responsabilidad |
|---|---|---|
| Presentación | `interfaz/` | Rutas Flask, plantillas y archivos estáticos; coordina solicitudes y respuestas. |
| Negocio | `nucleo/` | Tipos, validaciones y reglas puras; no depende de Flask ni de la base de datos. |
| Datos | `almacen/` | Persistencia y transacciones; accede a Supabase. |

El punto de entrada previsto es `main.py`. Se proponen módulos de negocio para
tipos, catálogo, préstamos, reservas, multas, usuarios, autenticación y
permisos; módulos de datos por entidad; pruebas independientes del servidor y
un directorio `datos/` para el esquema y datos de ejemplo.

Las contraseñas no deben almacenarse en texto plano. La configuración y las
credenciales de Supabase deberán gestionarse fuera del código fuente. Las
decisiones concretas sobre el cliente de base de datos y el esquema aún deben
definirse antes de implementar la persistencia.

## Pruebas y entrega

El núcleo debe poder probarse aisladamente, sin Flask ni conexión a Supabase.
El documento propone `pytest`, pruebas del sistema, documentación de ejecución y
un pipeline de GitHub Actions que instale dependencias y ejecute las pruebas.
El despliegue se explicará conceptualmente para la entrega académica.

## Flujo de trabajo

Se propone mantener `main` para versiones estables, `develop` para integración
y ramas `feature/<nombre>` para cambios acotados. Los cambios se incorporan a
`develop` mediante Pull Requests tras ejecutar las pruebas; `main` se actualiza
cuando `develop` esté verificada. Los commits siguen
`tipo(alcance): descripción`, por ejemplo `feat(nucleo): agrega reglas de multa`.
Las convenciones completas están en [CONVENCIONES.md](CONVENCIONES.md).

## Reglas de dominio acordadas

- **Título y ejemplares:** `Libro` representa la obra del catálogo y cada
  `Ejemplar` representa una unidad física identificada individualmente. Los
  préstamos y las reservas se asignan a ejemplares, no al título abstracto.
- **Solicitud de préstamo:** el Lector crea una solicitud pendiente para un
  título. El Bibliotecario la aprueba o la rechaza. Aprobarla asigna un ejemplar
  disponible y registra el préstamo; el cambio del ejemplar y del préstamo
  deberá persistirse como una operación atómica.
- **Reservas:** solo se permiten cuando no hay ejemplares disponibles. Se
  mantiene una cola FIFO por título; un lector no puede tener más de una reserva
  activa para el mismo título. Al devolverse un ejemplar, se asigna al lector
  que lleva más tiempo esperando y queda reservado para él; si no hay cola,
  vuelve a estar disponible.
- **Multas:** se calculan al devolver un préstamo vencido como días de retraso
  por tarifa diaria. Una devolución puntual no genera multa. Los importes se
  representan con precisión decimal y el bibliotecario registra el pago.
- **Reglas no especificadas:** no se impondrán límites de préstamos o reservas
  por lector ni bloqueos por multas pendientes hasta que exista un requisito
  explícito. Las reglas requieren validación de fechas, estados y pertenencia al
  título correspondiente.

La capa de negocio implementará estas decisiones como reglas puras. La
persistencia deberá proteger las operaciones concurrentes con transacciones;
el esquema y la configuración concreta de Supabase se definirán en una etapa
posterior.

## Estado inicial observado

La carpeta de trabajo contiene documentación y `requirements.txt` con Flask y
pytest, pero todavía no contiene el código de la aplicación. El README describe
la estructura y el proceso previsto. El repositorio remoto
`JulianHenao-Web/Proyeccion-BaseBook` estaba vacío y la carpeta local no tenía
historial Git al iniciar esta tarea. Se inicializó el historial y se publicaron
`main`, `develop` y ramas feature. La síntesis se propuso en el Pull Request #1
hacia `develop`; el desarrollo del núcleo se realiza en una rama feature
independiente.
