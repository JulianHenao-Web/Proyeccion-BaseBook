**Facultad de Ingenierías \- Tecnología en Desarrollo de Software** 

# **BaseBook**

Sistema de Gestión de Biblioteca

**Presentado por:**

Julian David Henao Cataño

Daniel Londoño Ruiz 

Alejandro Mosquera Lopez

Miguel Angel Vergara Martinez

**Docente:**

Juan Camilo Olarte Betancourt

**Materia:**

Entornos de Desarrollo de Software

**Universidad Tecnológica de Pereira**

**Pereira, Colombia**

**13 \- 10 \- 2026**

# **1\. Introducción**

El presente análisis define el funcionamiento general del sistema de gestión de biblioteca, estableciendo los actores que interactúan con el sistema, los principales casos de uso, las funcionalidades que serán desarrolladas y los requerimientos que deberá cumplir. La arquitectura propuesta para organizar sus componentes se definirá en una etapa posterior. La finalidad de esta etapa es establecer una base clara para el diseño de los diagramas UML y para la implementación del sistema.

# **2\. Contexto**

El sistema está pensado para una biblioteca universitaria de tamaño pequeño o mediano, donde un equipo reducido atiende a estudiantes y docentes. Los lectores consultan el catálogo y solicitan servicios desde cualquier dispositivo con navegador. El Bibliotecario atiende el mostrador y el Administrador gestiona usuarios y configuración. El sistema opera durante el horario de la biblioteca 

# **3\. Problema a resolver**

Desde hace tiempo las bibliotecas se han considerado centros de conocimiento y aprendizaje, con el propósito de facilitar el acceso a la información y contribuir al desarrollo académico. Sin embargo, su administración puede presentar dificultades relacionadas con la organización de los recursos, el registro de los usuarios y el control de los préstamos y devoluciones, especialmente cuando estos procesos se realizan de forma manual se pueden ocasionar errores y dificultades en la gestión de la información.

BaseBook es una aplicación web diseñada para facilitar la administración y automatización con el propósito de centralizar la información, gestionar el registro de los usuarios y controlar los préstamos y las devoluciones de libros con el fin de optimizar los procesos administrativos y mejorar la organización para facilitar el acceso a la información.

# **4\. Justificación**

# 

Un sistema de software se justifica porque centraliza en un solo lugar el catálogo, los préstamos, las reservas y las multas, y así evita que dos personas vean un mismo libro como disponible. Se eligió una aplicación web porque los tres tipos de usuario pueden usarla sin instalar nada y porque un servidor central garantiza la consistencia de los datos. La separación en tres roles limita lo que cada usuario puede hacer, es viable para el equipo y su organización en capas permite mantener y ampliar óptimamente el sistema.

# **5\. Beneficios esperados**

| Beneficiado | Beneficio |
| :---: | :---: |
| **Lector** | Consulta la disponibilidad real de un libro antes de ir a buscarlo, reserva los que están prestados y revisa sus préstamos y multas. |
| **Bibliotecario** | Registra préstamos y devoluciones sin papel, calcula las multas automáticamente y sabe en todo momento qué está prestado. |
| **Administrador** | Gestiona usuarios y roles, y ajusta el período de préstamo y el valor de la multa sin modificar el sistema  |
| **Biblioteca** | Información centralizada, datos consistentes, contraseñas cifradas y acceso según el rol. |

# **6\. Usuarios del sistema**

Los principales tipos de usuarios son:

# **6.1. Administrador**

Es el usuario responsable de la administración general del sistema. Su función se concentra en la gestión de los usuarios y en la configuración general de la plataforma; no interviene en la gestión del catálogo de libros ni en el proceso de préstamos, que corresponden al Bibliotecario.

**Responsabilidades Principales**

- Gestionar la información de los usuarios.  
- Asignar y modificar los roles de acceso de los usuarios.  
- Configurar los parámetros generales del sistema.  
- Supervisar el funcionamiento general de la plataforma.

**Operaciones Permitidas**

- Registrar usuarios.  
- Consultar usuarios.  
- Modificar información de usuarios.  
- Asignar o modificar el rol de acceso de un usuario.  
- Configurar los parámetros generales del sistema (por ejemplo, el período estándar de préstamo o el valor de la multa por día de retraso).

# **6.2. Bibliotecario**

Es el usuario encargado de ejecutar las operaciones cotidianas de la biblioteca. Su actividad está relacionada con la atención de los lectores y con el control completo de los recursos bibliográficos: el catálogo de libros, los préstamos, las devoluciones, las reservas y las multas.  
>   
**Responsabilidades Principales**

- Gestionar la información de los libros del catálogo.  
- Consultar la disponibilidad de los libros.  
- Registrar préstamos.  
- Registrar devoluciones.  
- Gestionar reservas.  
- Gestionar las multas generadas por retrasos en la devolución.  
- Consultar información de los usuarios.  
- Verificar el estado de los préstamos.

**Operaciones Permitidas**

- Registrar libros.  
- Consultar libros.  
- Modificar información de libros.  
- Eliminar libros.  
- Consultar el catálogo.  
- Consultar la disponibilidad de los libros.  
- Consultar información de los lectores.  
- Registrar un préstamo.  
- Registrar una devolución.  
- Consultar los préstamos activos.  
- Gestionar las reservas.  
- Consultar las multas generadas y registrar su pago.  
- Verificar el estado de los libros.

# **6.3. Lector**

Es el usuario que utiliza los servicios proporcionados por la biblioteca, a través de una cuenta registrada en el sistema. Su interacción está orientada principalmente a consultar el catálogo, conocer la disponibilidad de los libros y solicitar los servicios de préstamo y reserva.

**Responsabilidades Principales**

- Consultar el catálogo.  
- Buscar libros.  
- Consultar la disponibilidad.  
- Solicitar préstamos.  
- Realizar reservas.  
- Consultar sus préstamos.  
- Consultar sus multas, si las hubiera.

**Operaciones Permitidas:**

- Buscar libros por título.  
- Buscar libros por autor.  
- Buscar libros por categoría.  
- Consultar la información de un libro.  
- Consultar la disponibilidad.  
- Solicitar un préstamo.  
- Solicitar una reserva cuando el libro no se encuentre disponible.  
- Consultar el estado de sus préstamos.  
- Consultar el estado de sus multas, si las hubiera.

# **7\. Funcionalidades principales**

# **7.1. Gestión de libros**

Permitir al Bibliotecario registrar, consultar, modificar y eliminar los libros del catálogo, manteniendo actualizada su información y estado de disponibilidad.

# **7.2. Gestión de usuarios**

Permitir al Administrador registrar, consultar, modificar y administrar la información de los usuarios que utilizan la biblioteca, así como sus roles de acceso.

# **7.3. Consulta y búsqueda del catálogo**

Permitir a los usuarios registrados consultar los libros disponibles en la biblioteca y realizar búsquedas utilizando información como el título, autor o categoría.

# **7.4. Consulta de disponibilidad**

Permitir consultar el estado actual de los libros, identificando si se encuentran disponibles, prestados o reservados.

# **7.5. Gestión de préstamos y devoluciones**

Permitir registrar el préstamo de un libro, guardando la fecha de préstamo y la fecha límite de devolución; registrar su devolución, actualizando automáticamente la disponibilidad del libro; y consultar en cualquier momento los préstamos activos y su estado.

# **7.6. Gestión de Reservas**

Permitir que los lectores soliciten la reserva de libros que se encuentren temporalmente no disponibles, facilitando su posterior préstamo cuando sean devueltos.

# **7.7. Gestión de multas**

Calcular automáticamente los días de retraso cuando un préstamo supera su fecha límite de devolución, y generar la multa correspondiente para que el Bibliotecario la gestione. 

# **8\. Casos de uso principales**

Los casos de uso describen las interacciones principales entre los actores y el sistema. Cada caso de uso representa una operación que aporta valor al usuario y que posteriormente podrá representarse en el diagrama de casos de uso.

# **CU01 \- Registrarse**

**Objetivo:** Permitir que una persona cree su propia cuenta de Lector para utilizar el sistema.  
**Actor principal:** Lector.  
**Descripción:** La persona ingresa sus datos personales: nombre completo, número de identificación, correo electrónico, teléfono y contraseña.  
**Resultado esperado:** La cuenta queda creada con el rol de Lector y la persona puede iniciar sesión.

# **CU02 \- Iniciar sesión**

**Objetivo:** Permitir que un usuario registrado acceda al sistema con sus credenciales.  
**Actores:** Lector, Bibliotecario y Administrador.  
**Descripción:** El usuario ingresa su correo electrónico y su contraseña. El sistema autentica las credenciales verificando la contraseña contra su versión cifrada y, si son correctas y la cuenta está activa y abre la sesión y habilita únicamente las funciones correspondientes al rol del usuario  
**Resultado esperado:** El usuario accede solo a las funciones permitidas para su rol, o recibe un mensaje de acceso denegado.

# **CU03 \- Consultar catálogo**

**Objetivo:** Permitir a los usuarios consultar los libros registrados en la biblioteca.  
**Actores:** Lector y Bibliotecario.  
**Descripción:** El usuario accede al catálogo y obtiene la información disponible de los libros registrados.  
**Resultado esperado:** El sistema muestra los libros disponibles en el catálogo de acuerdo con la consulta realizada.

# **CU04 \- Buscar libro**

**Objetivo:** Facilitar la localización de un libro específico dentro del catálogo.  
**Actores:** Lector y Bibliotecario.  
**Descripción:** El usuario introduce uno o más criterios de búsqueda, como título, autor o categoría. El sistema procesa la información y presenta los libros que coinciden con los criterios establecidos.  
**Resultado esperado:** El sistema muestra una lista de resultados que permite identificar el libro buscado.

# **CU05 \- Consultar disponibilidad**

**Objetivo:** Permitir conocer el estado actual de un libro.  
**Actores:** Lector y Bibliotecario.  
**Descripción:** El usuario selecciona un libro y consulta su estado. El sistema deberá indicar si el libro se encuentra:

- Disponible.  
- Prestado.  
- Reservado.

**Resultado esperado:** El usuario obtiene el estado actual del libro y puede determinar si es posible solicitarlo, reservarlo o consultar otro ejemplar.

# **CU06 \- Gestionar libros**

**Objetivo:** Administrar la información de los libros registrados en el sistema.  
**Actor principal:** Bibliotecario.  
**Descripción:** El Bibliotecario podrá realizar operaciones CRUD sobre los libros. La información almacenada deberá permitir identificar adecuadamente cada libro y conocer su estado de disponibilidad.  
**Resultado esperado:** La información del catálogo permanece actualizada y disponible para las consultas de los usuarios.

# **CU07 \- Gestionar usuarios**

**Objetivo:** Administrar la información correspondiente a los usuarios del sistema.  
**Actor principal:** Administrador.  
**Descripción:** El Administrador registra y administra los usuarios, manteniendo la información necesaria para que puedan utilizar el sistema de acuerdo con su rol.  
**Resultado esperado:** Los usuarios quedan correctamente registrados y asociados al rol correspondiente.

# **CU08 \- Solicitar préstamo**

**Objetivo:** Permitir que un Lector solicite un libro disponible.  
**Actor principal:** Lector.  
**Descripción:** El Lector consulta un libro y, cuando este se encuentra disponible, solicita su préstamo. El sistema deberá verificar el estado del libro antes de aceptar la solicitud.  
**Resultado esperado:** La solicitud queda registrada para ser procesada por el Bibliotecario.

# **CU09 \- Registrar préstamo**

**Objetivo:** Registrar formalmente un préstamo dentro del sistema.  
**Actor principal:** Bibliotecario.  
**Descripción:** El Bibliotecario recibe la solicitud de préstamo, verifica que el lector y el libro sean válidos y registra el préstamo. El sistema deberá almacenar como mínimo:

- Lector asociado.  
- Libro asociado.  
- Fecha del préstamo.  
- Fecha prevista de devolución.  
- Estado del préstamo.

Una vez registrado correctamente, el estado del libro deberá cambiar de disponible a prestado.  
**Resultado esperado:** El préstamo queda almacenado y el libro deja de aparecer como disponible.

# **CU10 \- Registrar devolución**

**Objetivo:** Registrar la devolución de un libro prestado.  
**Actor principal:** Bibliotecario.  
**Descripción:** El Bibliotecario selecciona el préstamo correspondiente y registra la devolución del libro. El sistema actualiza el préstamo y modifica el estado del libro. Si la devolución se realiza después de la fecha límite establecida, el sistema calculará automáticamente los días de retraso y generará la multa correspondiente.  
**Resultado esperado:** La devolución queda registrada y el libro vuelve a estar disponible, siempre que no exista una reserva pendiente que deba ser atendida.

# **CU11 \- Gestionar reservas**

**Objetivo:** Permitir administrar las reservas de libros que temporalmente no se encuentran disponibles.  
**Actores principales:** Lector y Bibliotecario.  
**Descripción:** Cuando un libro está prestado o no disponible, el Lector podrá solicitar una reserva. El Bibliotecario podrá consultar y gestionar las reservas registradas.  
**Resultado esperado:** La reserva queda almacenada y asociada al lector y al libro correspondiente.

# **CU12 \- Consultar préstamos**

**Objetivo:** Permitir consultar la información de los préstamos registrados.  
**Actores:** Lector y Bibliotecario.  
**Descripción:** El sistema mostrará los préstamos según el rol del usuario.

- El Lector podrá consultar únicamente sus propios préstamos.  
- El Bibliotecario podrá consultar los préstamos necesarios para realizar su trabajo.

**Resultado esperado:** El usuario obtiene información actualizada sobre los préstamos que puede consultar de acuerdo con sus permisos.

# **CU13 \- Supervisar préstamos**

**Objetivo:** Permitir verificar el estado general de los préstamos.  
**Actor principal:** Bibliotecario.  
**Descripción:** El sistema permitirá consultar los préstamos activos y su estado, facilitando la supervisión de los libros que actualmente se encuentran prestados.  
**Resultado esperado:** El Bibliotecario puede conocer qué libros están prestados y qué usuarios los tienen asociados.

# **CU14 \- Gestionar multas**

**Objetivo:** Controlar las multas generadas por el retraso en la devolución de los libros.  
**Actor principal:** Bibliotecario.  
**Descripción:** Cuando una devolución se registra después de la fecha límite establecida, el sistema calcula automáticamente los días de retraso y genera una multa asociada al préstamo y al lector correspondiente. El Bibliotecario podrá consultar las multas pendientes y registrar su pago una vez este se realice.  
**Resultado esperado:** Las multas quedan correctamente generadas y asociadas al lector correspondiente, y su estado (pendiente o pagada) se mantiene actualizado.

# **CU15 \- Configurar parámetros del sistema**

**Objetivo:** Permitir ajustar la configuración general de la plataforma.  
**Actor principal:** Administrador.  
**Descripción:** El Administrador podrá definir parámetros generales de funcionamiento del sistema, como el período estándar de préstamo o el valor de la multa por día de retraso.  
**Resultado esperado:** El sistema opera de acuerdo con los parámetros definidos por el Administrador.

# 

# **9\. Requerimientos Funcionales**

Los requerimientos funcionales describen las acciones y servicios que el sistema deberá proporcionar.

# **RF01 — Registro de Lectores**

El sistema deberá permitir que una persona cree su propia cuenta de Lector ingresando nombre completo, número de identificación, correo electrónico, teléfono y contraseña.

# **RF02 — Iniciar y cierre de sesión**

El sistema deberá permitir a los usuarios registrados (Lectores, Bibliotecarios y Administradores) iniciar sesión con su correo electrónico y contraseña, y cerrar su sesión.

# **RF03 — Gestión de libros**

El sistema deberá permitir al Bibliotecario registrar nuevos libros en el catálogo.

# **RF04 — Consulta de libros**

El sistema deberá permitir consultar la información de los libros registrados.

# **RF05 — Modificación de libros**

El sistema deberá permitir al Bibliotecario modificar la información de los libros.

# **RF06 — Eliminación de libros**

El sistema deberá permitir al Bibliotecario eliminar libros del catálogo cuando corresponda.

# **RF07 — Búsqueda de libros**

El sistema deberá permitir buscar libros mediante criterios como título, autor o categoría.

# **RF08 — Consulta de disponibilidad**

El sistema deberá permitir consultar el estado de disponibilidad de cada libro. Los estados principales serán:

- Disponible.  
- Prestado.  
- Reservado.

# **RF09 — Gestión de usuarios**

El sistema deberá permitir al Administrador registrar y administrar la información de los usuarios.

# **RF10 — Gestión de roles**

El sistema deberá diferenciar los permisos correspondientes a Administradores, Bibliotecarios y Lectores. El Administrador podrá asignar o modificar el rol de un usuario.

# **RF11 — Solicitud de préstamo**

El sistema deberá permitir al Lector solicitar el préstamo de un libro disponible.

# **RF12 — Registro de préstamo**

El sistema deberá permitir al Bibliotecario registrar formalmente los préstamos. Cada préstamo deberá almacenar como mínimo el usuario, libro, fecha de préstamo y fecha prevista de devolución.

# **RF13 — Registro de devolución**

El sistema deberá permitir al Bibliotecario registrar la devolución de los libros prestados.

# **RF14 — Actualización de disponibilidad**

El sistema deberá actualizar el estado del libro de acuerdo con las operaciones de préstamo, devolución y reserva.

# **RF15 — Gestión de reservas**

El sistema deberá permitir que los Lectores soliciten reservas sobre libros que no estén disponibles, y que el Bibliotecario las gestione.

# **RF16 — Consulta de préstamos**

El sistema deberá permitir consultar los préstamos de acuerdo con los permisos del usuario: el Lector podrá consultar únicamente sus propios préstamos, y el Bibliotecario podrá consultar los préstamos necesarios para su labor.

# **RF17 — Supervisión de préstamos**

El sistema deberá permitir al Bibliotecario consultar el estado de los préstamos activos.

# **RF18 — Control de acceso**

El sistema deberá restringir las operaciones según el rol del usuario. Un Lector no podrá modificar información administrativa, y un Administrador no podrá realizar operaciones sobre el catálogo, los préstamos o las reservas, las cuales están reservadas al Bibliotecario.

# **RF19 — Cálculo automático de multas**

El sistema deberá calcular automáticamente los días de retraso cuando una devolución se registre después de la fecha límite de devolución, y generar la multa correspondiente.

# **RF20 — Gestión de multas**

El sistema deberá permitir al Bibliotecario consultar las multas generadas y registrar su pago.

# **RF21 — Configuración del sistema**

El sistema deberá permitir al Administrador configurar los parámetros generales de la plataforma, como el período estándar de préstamo o el valor de la multa por día de retraso.

# **10\. Requerimientos No Funcionales**

Los requerimientos no funcionales establecen características de calidad y restricciones que deberá cumplir el sistema.

# **RNF01 — Usabilidad**

El sistema deberá proporcionar una interfaz sencilla, clara e intuitiva, de manera que los usuarios puedan realizar las operaciones principales sin requerir conocimientos técnicos avanzados. Las opciones disponibles deberán estar organizadas según el rol del usuario.

# **RNF02 — Rendimiento**

Las consultas habituales del sistema, como búsquedas de libros y consultas de disponibilidad, deberán ejecutarse en un tiempo adecuado para permitir una interacción fluida. Para las condiciones normales de uso planteadas para el proyecto, se establece como objetivo que las operaciones habituales respondan en un máximo aproximado de tres segundos.

# **RNF03 — Seguridad**

El sistema deberá proteger la información de los usuarios y restringir el acceso a funcionalidades según los permisos correspondientes. Las operaciones administrativas deberán estar disponibles únicamente para los usuarios autorizados.

# **RNF04 — Integridad de la información**

El sistema deberá mantener consistencia entre los libros, préstamos, devoluciones, reservas y multas. Por ejemplo, un libro que se encuentre registrado como prestado no deberá aparecer simultáneamente como disponible, y una multa pagada no deberá aparecer como pendiente.

# **RNF05 — Disponibilidad**

El sistema deberá estar disponible durante el horario de operación definido para la biblioteca y permitir el acceso a las funcionalidades principales sin interrupciones innecesarias.

# **RNF06 — Compatibilidad**

Al tratarse de una aplicación web, el sistema deberá poder utilizarse desde los principales navegadores web modernos.

# **RNF07 — Mantenibilidad**

La aplicación deberá organizarse mediante una estructura modular que facilite la modificación, corrección y ampliación de sus funcionalidades. La separación de responsabilidades propuesta en la arquitectura ayudará a cumplir este requerimiento.

# **RNF08 — Escalabilidad**

La estructura del sistema deberá permitir incorporar nuevas funcionalidades en el futuro sin tener que reconstruir completamente la aplicación. Entre posibles ampliaciones se encuentran reportes avanzados, notificaciones o manejo de múltiples ejemplares.

# **RNF09 — Consistencia de datos**

Las operaciones realizadas sobre préstamos, devoluciones, reservas y multas deberán actualizar correctamente la información relacionada para evitar estados contradictorios.

# 

# 

# 

# 

# 

# 

# 

# 

# 

# **11\. Diagramas UML**

# **11.1 Diagrama de Casos de Uso**

# **11.2 Diagrama de Clases**

# **11.3 Diagrama de Secuencia**

# **12\. Arquitectura del Sistema**

La arquitectura propuesta es Cliente-Servidor Web, organizada internamente en tres capas, construida con Python y el framework Flask, y con Supabase como motor de base de datos. A continuación se explica y justifica cada decisión por separado, ya que cada una responde una pregunta distinta del diseño del sistema.

# **12.1 Modelo de distribución: Cliente-Servidor**

El cliente será un navegador web: los tres actores (Administrador, Bibliotecario y Lector) acceden al sistema desde cualquier dispositivo, sin necesidad de instalar software adicional. El servidor, centralizado, procesa todas las peticiones y mantiene una única fuente de verdad sobre el estado real del sistema — en particular, sobre la disponibilidad de cada libro.

Esta decisión se deriva directamente de RF08 (consulta de disponibilidad), de RNF04 (integridad de la información: un libro prestado no puede aparecer simultáneamente como disponible) y de RNF06 (uso desde navegadores web). Si cada cliente manejara su propia copia de la información sin un servidor central que la validara, sería imposible garantizar esa consistencia. Un servidor central resuelve esto por diseño.

# **12.2 Modelo lógico: tres capas — Presentación, Negocio y Datos**

Dentro del servidor, el código se organiza en tres capas, cada una con una única responsabilidad y ubicada en su propia carpeta del proyecto. Los nombres de las carpetas describen el rol técnico de cada una y no repiten literalmente el nombre de la capa, por lo que la siguiente tabla indica la correspondencia:

| Capa | Carpeta | Qué contiene | De qué depende |
| :---: | :---: | :---: | :---: |
| Presentación | interfaz/ | Rutas web (Flask), plantillas HTML y archivos estáticos | Negocio y Datos |
| Negocio | nucleo/ | Reglas y validaciones como funciones puras: reglas del catálogo, préstamos, reservas, multas y usuarios, autenticación, permisos y tipos de datos | De nada: no importa ni Flask ni la base de datos |
| Datos | almacen/ | Funciones de lectura y escritura en Supabase y control de transacciones | Del núcleo, solo para los tipos de datos |

- **Capa de Presentación (carpeta interfaz/)**

  Recibe las solicitudes del navegador y muestra la información. No contiene reglas del negocio: se limita a coordinar el flujo de cada operación (pedir los datos al almacén, consultar al núcleo qué hacer y guardar el resultado) y a mostrar la respuesta.

- **Capa de Negocio (carpeta nucleo/)**

  Contiene las reglas y validaciones del sistema, escritas como funciones puras: el control de acceso según el rol (RF18), el cálculo automático de los días de retraso (RF19), la verificación de que un libro pueda prestarse, entre otras.

- **Capa de Datos (carpeta almacen/)**

  Se encarga exclusivamente de guardar y recuperar la información de la base de datos.





# **12.3 Lenguaje de programación y framework: Python con Flask**

Se eligió Python como lenguaje principal del proyecto y Flask como framework web. La justificación tiene varias partes:

- **Python es legible y adecuado para un equipo que está aprendiendo.** Además, las reglas del negocio (carpeta nucleo/) son Python puro: el equipo puede escribirlas y probarlas sin conocer ningún framework.

- **Flask es un framework ligero.** Tiene pocos conceptos que aprender (rutas, solicitudes y plantillas) y su uso queda limitado a la carpeta interfaz/ y al archivo de arranque main.py. La mayor parte del código del sistema no depende de él.

- **Un solo lenguaje en todo el proyecto.** Las pantallas se construyen con plantillas HTML, por lo que no hace falta aprender un segundo lenguaje de programación para la interfaz.

- **Contrapartida asumida.** El equipo implementa sistema de inicio de sesión, roles y panel de administración en los módulos nucleo/autenticacion.py y nucleo/permisos.py, cubriendo RF01, RF02, RF10, RF18, y RNF03. Esto exige un poco más de código, pero da control total y una comprensión clara de cómo funciona la seguridad del sistema.

# **12.4 Entorno de desarrollo**

Se utilizará Visual Studio Code como editor de trabajo: es gratuito, liviano, cuenta con extensiones específicas para Python y Flask, e integra control de versiones con Git. El código y la documentación se alojan en un repositorio de GitHub, con la estrategia de ramas definida.

# **12.5 Base de datos: Supabase**

Se eligió Supabase como motor de base de datos, al que se accede mediante consultas SQL escritas en las funciones de la carpeta almacen/. La justificación es la siguiente:

- Es una base de datos relacional, adecuada para las relaciones entre Usuario, Libro, Préstamo, Reserva y Multa.

- Soporta transacciones y control de concurrencia, necesarios para cumplir RNF04 y RNF09 (por ejemplo, evitar que dos usuarios tomen prestado el mismo libro al mismo tiempo).

- Es robusta y gratuita, y permite cumplir el tiempo de respuesta de RNF02.

# **12.6 Estructura del proyecto**

`Basebook-code/`  
`├── README.md`  
`├── main.py   # arranque de la aplicación web (Flask)`  
`│`  
`├── interfaz/   # CAPA DE PRESENTACIÓN: rutas web (Flask)`  
`│   ├── plantillas/   # páginas HTML`  
`│   └── estaticos/   # hojas de estilo e imágenes`  
`│`  
`├── nucleo/   # CAPA DE NEGOCIO: Solo funciones puras`  
`│   ├── tipos.py   # Libro, Prestamo, Reserva, Multa, Usuario, Parametros`  
`│   ├── reglas_catalogo.py   # filtrar_libros(), estado_resultante()`  
`│   ├── reglas_prestamo.py   # puede_prestar(), crear_prestamo()`   
`│   ├── reglas_reserva.py   # puede_reservar(), siguiente_en_cola()`  
`│   ├── reglas_multa.py   # dias_retraso(), calcular_multa()`  
`│   ├── reglas_usuario.py   # validación de datos de usuario y roles válidos`  
`│   ├── autenticacion.py   # cifrar_contrasena(), verificar_contrasena()`  
`│   └── permisos.py   # PERMISOS = {rol: {operaciones}}, rol_permite()`  
`│`  
`├── almacen/   # CAPA DE DATOS: funciones de entrada/salida a la BD`  
`│   ├── conexion.py   # transaccion()`  
`│   └── libros.py`  
`│   └── prestamos.py`  
`│   └── reservas.py`  
`│   └── multas.py`  
`│   └── usuarios.py`  
`│   └── parametros.py`  
`│`  
`├── pruebas/`  
`│   └── test_nucleo/`  
`└── datos/   # esquema SQL de la base de datos y datos de ejemplo`

# **12.7. Componentes Esenciales del Sistema**

A partir de la arquitectura anterior, estos son los componentes necesarios, organizados por capa. Entre paréntesis se indica el requerimiento que cada uno satisface.

### **Capa de Presentación (interfaz/)**

- **Rutas web (Flask):** reciben las peticiones del navegador, comprueban el permiso del rol antes de ejecutar cada operación, administran la sesión del usuario y devuelven la página correspondiente (RF18, RF02, RNF03).

- **Pantallas de acceso:** formularios de registro de Lectores y de inicio y cierre de sesión, comunes a los tres roles (RF01, RF02).

- **Catálogo (consulta y búsqueda):** pantallas donde Lector y Bibliotecario buscan y consultan libros (RF04, RF07, RF08).

- **Módulo del Bibliotecario:** pantallas para gestionar libros, préstamos, devoluciones, reservas y multas (RF03, RF05, RF06, RF12, RF13, RF15, RF16, RF17, RF20).

- **Módulo del Administrador:** pantallas para gestionar usuarios, roles y configuración del sistema (RF09, RF10, RF21).

- **Portal del Lector:** solicitud de préstamos y reservas, y consulta de sus propios préstamos y multas (RF11, RF15, RF16).

### **Capa de Negocio (nucleo/)**

- **Reglas del catálogo (reglas\_catalogo.py):** Filtran los libros según los criterios de búsqueda y determinan el estado resultante de un libro (RF07, RF08, RF14).

- **Reglas de préstamos (reglas\_prestamo.py):** Verifican si un libro puede prestarse, crean el préstamo con su fecha prevista de devolución y lo cierran al devolverse (RF11, RF14).

- **Reglas de reservas (reglas\_reserva.py):** Determinan si un libro puede reservarse y quién sigue en la cola de reservas (RF15).

- **Reglas de multas (reglas\_multa.py):** Calculan los días de retraso y el valor de la multa (RF19).

- **Reglas de usuarios (reglas\_usuario.py):** validan los datos de los usuarios (completitud y formato del correo) y los roles permitidos (RF01, RF09, RF10).

- **Autenticación (autenticacion.py):** cifra las contraseñas, y verifica las credenciales al iniciar sesión (RF01, RF02, RNF03).

- **Permisos (permisos.py):** define qué operaciones puede realizar cada rol y permite consultarlo (RF10, RF18).

### **Capa de Datos (almacen/ y Supabase)**

- **Conexión y transacciones (conexion.py):** administra la conexión con la base de datos y agrupa en una transacción las operaciones que deben guardarse juntas (RNF04, RNF09).

- **Acceso por entidad (libros.py, prestamos.py, reservas.py, multas.py, usuarios.py, parametros.py):** funciones que leen y escriben cada tipo de información en la base de datos (RF01, RF02, RF03, RF05, RF6, RF09, RF12, RF13, RF15, RF20, RF21).

- **Base de datos Supabase:** almacena de forma estructurada y persistente los usuarios, libros, préstamos, reservas, multas y parámetros del sistema (RNF02, RNF04).

- **Seguridad de datos:** las contraseñas se almacenan cifradas y se realizan copias de seguridad periódicas de la base de datos (RNF03).

### **Soporte del proyecto**

- **Pruebas (pruebas/test\_nucleo):** verifican las reglas del negocio sin necesidad de base de datos ni servidor (RNF07).

- **Documentación y repositorio (README.md, docs/):** reúnen la descripción del proyecto, los documentos de análisis y los diagramas UML.

# **13\. Repositorio GitHub BaseBook**

[https\://github.com/JulianHenao-Web/BaseBook.git](https://github.com/JulianHenao-Web/BaseBook.git)

El repositorio es público y contiene el README.md y la carpeta Basebook-code/, que reúne la estructura inicial descrita en la sección 12.6: nucleo/ (capa de Negocio), almacen/ (capa de Datos), interfaz/ (capa de Presentación), pruebas/ y datos/, además del archivo de arranque main.py. 

# **14\. Diagrama general**

![][image4]

El diagrama resume cómo se organiza el sistema. Arriba está el cliente: los tres tipos de usuario acceden desde un navegador web, que se comunica con el servidor por HTTP. El servidor, construido con Python y Flask, tiene tres capas: Presentación (interfaz/), que recibe las peticiones y arma las pantallas; Negocio (nucleo/), que contiene las reglas como funciones puras sin depender de Flask ni de la base de datos; y Datos (almacen/), que lee y guarda la información en Supabase mediante SQL y transacciones. Las flechas indican quién usa a quién: la Presentación consulta las reglas y pide y guarda datos; la capa de Datos solo usa los tipos de datos del Negocio; y el Negocio no depende de nadie, por lo que puede probarse de forma aislada.

# **15\. Historial de commits**

| Commit | Fecha | Autor | Mensaje | Registra |
| :---: | :---: | :---: | ----- | ----- |
| fcfb676 | 05 Oct | Alejandro Mosquera | README provisional  | Crea el README.md inicial, un borrador a partir de una plantilla  |
| 268844d | 05 Oct | Alejandro Mosquera | Update README.md  | Adapta el borrador: título, descripción y una primera organización de carpetas  |
| 61f1aac | 08 Oct | Alejandro Mosquera | Update README.md  | Agrega la estructura deseada del proyecto  |
| 1366d2d | 08 Oct | Alejandro Mosquera | Update README.md  | Reorganiza el README y reubica los requisitos previos  |
| de8901a | 11 Oct | Alejandro Mosquera | Add files via upload  | Sube main.py dentro de la carpeta Basebook-code  |
| 6cecd0c | 11 Oct | Julian Henao | Creación del módulo Núcleo  | Crea los 6 archivos iniciales de nucleo/  |
| 75f5f7e | 11 Oct | Daniel Londoño | Crea estructura inicial del módulo almacén  | Crea los 7 archivos de almacen/  |
| 80da928 | 12 Oct | Miguel Vergara | Creación inicial de estructura interfaz, pruebas y datos  | Crea 4 archivos en interfaz/, pruebas/ y datos/  |
| f6832dc | 13 Oct | Julian Henao | Creacion de reglas\_usuario.py y autenticacion.py en nucleo  | Agrega los módulos de registro y autenticación  |

**![][image5]**

# **16\. Estrategia de ramas a implementar**

Para el desarrollo colaborativo del proyecto se utilizará una estrategia de ramas en Git, apoyada en un repositorio remoto alojado en GitHub. Esta estrategia permitirá que los integrantes del equipo trabajen en diferentes funcionalidades de manera organizada, manteniendo un historial de cambios claro y reduciendo el riesgo de que las modificaciones de un integrante afecten directamente el trabajo de los demás.

La estrategia se basará en tres tipos principales de ramas: main, develop y feature. Cada una tendrá una responsabilidad definida dentro del proceso de desarrollo y se utilizará de acuerdo con el estado de las funcionalidades implementadas.

El propósito de esta organización es mantener una versión estable del proyecto, disponer de una rama de integración para los cambios que se encuentren en desarrollo y permitir que cada nueva funcionalidad se implemente de forma independiente antes de incorporarse al sistema.

# **16.1. Creación de Ramas**

El repositorio utilizará las siguientes ramas:

## **Rama main**

La rama main contendrá las versiones estables y verificadas de BaseBook. Representará el estado del proyecto que se considera apto para presentarse, entregarse o utilizarse como versión de referencia.

Sus principales características serán:

- Contener únicamente versiones integradas y verificadas del proyecto.  
- No se utilizará para desarrollar directamente nuevas funcionalidades.  
- Recibir cambios procedentes de develop cuando estos hayan sido revisados y se haya comprobado su funcionamiento.  
- Mantener un historial de las versiones estables del sistema.  
- Servir como referencia para identificar las versiones presentables del proyecto.

No se realizarán modificaciones directamente sobre esta rama durante el desarrollo habitual, con el fin de evitar que código incompleto o funcionalidades en prueba afecten la versión estable.

## **Rama develop**

La rama develop será la rama principal de integración del equipo. En ella se reunirán las funcionalidades que hayan terminado su desarrollo individual y superado las verificaciones correspondientes.

Sus principales características serán:

- Servir como punto de partida para crear las ramas de nuevas funcionalidades.  
- Recibir las modificaciones integradas mediante solicitudes de incorporación (Pull Requests).  
- Permitir comprobar la compatibilidad entre los diferentes módulos desarrollados por los integrantes.  
- Mantener una versión de trabajo que reúna las funcionalidades implementadas hasta el momento.  
- Servir como origen para actualizar main cuando se haya alcanzado un estado estable.

Antes de incorporar una nueva funcionalidad, se comprobará que los cambios no contradigan la arquitectura establecida ni afecten el funcionamiento de los módulos existentes.

## **Rama feature**

Las ramas feature se utilizarán para desarrollar funcionalidades específicas de BaseBook de manera independiente. Cada rama se creará a partir de develop y tendrá un nombre descriptivo que identifique el trabajo realizado.

Algunos ejemplos de ramas que podrían utilizarse son:

| Rama | Funcionalidad |
| ----- | ----- |
| feature/registro-lectores | Registro de nuevos lectores e información asociada. |
| feature/autenticacion-permisos | Inicio de sesión, control de acceso y validación de roles. |
| feature/gestion-libros | Registro, consulta, modificación y eliminación de libros. |
| feature/prestamos-devoluciones | Registro de préstamos, devoluciones y actualización de disponibilidad. |
| feature/gestion-reservas | Solicitud y administración de reservas. |
| feature/gestion-multas | Cálculo de retrasos, generación de multas y registro de pagos. |
| feature/configuracion-sistema | Parámetros generales, como el período de préstamo y el valor de la multa. |

Estos nombres son ejemplos de una posible organización del trabajo; las ramas que se creen efectivamente dependerán de la distribución de tareas acordada por el equipo. Cada rama deberá concentrarse en una funcionalidad o conjunto pequeño de cambios relacionados. Se evitará incorporar modificaciones que no correspondan a su objetivo, con el propósito de facilitar la revisión y la identificación de errores.

## **Convenciones para los nombres**

Los nombres de las ramas de funcionalidad utilizarán el prefijo feature/, seguido de un nombre breve, descriptivo y escrito en minúsculas, utilizando guiones para separar palabras.

Por ejemplo:

feature/gestion-libros

Esta convención permitirá reconocer rápidamente la finalidad de cada rama y mantener una organización homogénea en el repositorio.

# **16.2 Flujo de trabajo colaborativo para nuevas funcionalidades**

## **1\. Planificación de la funcionalidad.**

El equipo identificará la funcionalidad que debe desarrollarse y definirá su objetivo con base en los requerimientos del sistema. Se asignará un responsable y se determinarán los resultados esperados.

**2\. Actualización de la rama develop.**

Antes de iniciar el trabajo, el integrante actualizará su repositorio local y comprobará que dispone de la versión más reciente de develop.

**3\. Creación de la rama feature.**

A partir de develop, el integrante creará una rama específica para la funcionalidad asignada. El desarrollo se realizará en esta rama, sin modificar directamente la rama de integración.

## **4\. Desarrollo y pruebas.**

El integrante implementará los cambios respetando la estructura del proyecto y las responsabilidades de cada capa. También realizará las pruebas pertinentes para verificar que la funcionalidad opere correctamente.

## **5\. Registro de cambios mediante commits.**

Los avances se guardarán en Git mediante commits pequeños y descriptivos. Cada commit deberá representar un cambio lógico y tener un mensaje que permita comprender qué se modificó.

## **6\. Publicación de la rama.**

Una vez registrados los cambios localmente, el integrante publicará la rama feature en GitHub para que el resto del equipo pueda consultarla y revisarla.

## **7\. Solicitud de incorporación (Pull Request).**

Cuando la funcionalidad se encuentre lista, se creará un Pull Request dirigido a develop. En él se explicará el propósito de los cambios, las funcionalidades implementadas y las pruebas realizadas.

## **8\. Revisión por otro integrante.**

Al menos un compañero revisará los cambios para identificar posibles errores, comprobar su coherencia con los requerimientos y verificar que se respete la organización del proyecto. Si es necesario, solicitará correcciones antes de aprobar la incorporación.

## **9\. Integración en develop.**

Una vez aprobados los cambios y corregidos los problemas identificados, la rama feature se integrará en develop. Después de confirmar que la integración se realizó correctamente, la rama de funcionalidad podrá eliminarse del repositorio remoto y de los repositorios locales.

## **10\. Actualización de main.**

Cuando el conjunto de funcionalidades integrado en develop haya sido verificado y se considere estable, se incorporará a main. Este paso se realizará especialmente cuando se prepare una versión para una entrega académica o una versión estable del proyecto.

Las ramas feature se crearán desde develop y sus cambios se incorporarán primero a esta rama. La actualización de main se realizará posteriormente, una vez verificada la estabilidad de la versión integrada.

# **17\. Conclusiones y próximos pasos**

# **17.1 Decisiones**

| Decisión | Motivo |
| :---: | ----- |
| Asignar 3 roles y funcionalidades | Cubrir el ciclo completo del préstamo y dar sentido al plazo de devolución. |
| Aplicación web Cliente \- Servidor | Acceso desde cualquier dispositivo y una sola fuente de verdad. |
| Arquitectura en tres capas | Separar interfaz, reglas y datos para mantener y probar. |
| Estructura nucleo / almacen / interfaz | Núcleo de funciones puras, probable sin base de datos y repartible por módulos. |
| Utilizar Python, Flask, Supabase, etc. | Lenguaje legible, framework ligero y un solo lenguaje en el proyecto, junto con una base relacional y transaccional. |
| Control de versiones con Git y Github | Trabajo colaborativo ordenado para mantener el flujo organizado. |

# **17.2 Dificultades encontradas y abordaje**

Durante el análisis de BaseBook se tomaron decisiones relacionadas con el alcance funcional, los tipos de usuarios, la arquitectura, las tecnologías, la organización del código, la seguridad y el proceso de desarrollo. Estas decisiones se adoptaron con el objetivo de mantener un sistema coherente, viable para el equipo y preparado para una implementación progresiva.

| Dificultad | Cómo se Abordó |
| :---: | ----- |
| Detallado de los diagramas | Se rehicieron tomando como referencia los ejemplos: relaciones include/extend, atributos con tipo y visibilidad, y multiplicidades |
| Definiciones entre roles de Administrador y Bibliotecario | Se redefinió el alcance del Administrador y se fusionaron las funcionalidades de préstamos y devoluciones |
| Cambios para una versión final de requerimientos | Se analizaron sus importancias y se rehicieron enfocandolos en una sola tarea. |
| Implementación de las arquitecturas | Se estudió cómo se organizaba, sus beneficios y forma de aplicación al proyecto. |
| Elecciones de herramientas | Se analizó cuales traían mejores beneficios y facilidad de implementación al proyecto. |

# **17.3 Aspectos pendientes**

- Implementar el código de los módulos, empezando por nucleo/ y sus pruebas.  
- Crear el proyecto en Supabase, el esquema SQL y la conexión desde almacen/ con variables de entorno.  
- Desarrollar las plantillas y los estilos de la interfaz.  
- Mejorar el desarrollo del código mediante manejo con ramas feature, develop, main y pull requests.  
- Añadir aspectos nuevos como reportes avanzados y las notificaciones.

# **17.4 Actividades previstas para la entrega final**

| Actividad | Qué se hará |
| :---: | ----- |
| Mejora de diagramas UML | Ajustar los tres diagramas según el avance de la implementación |
| Prototipo | Interfaz simple y backend básico en Python y Flask, conectado a Supabase o con datos de ejemplo |
| Pipeline CI/CD | Con GitHub Actions: al hacer push o abrir un Pull Request, instalar dependencias y ejecutar las pruebas del núcleo. Como el núcleo no depende de la base de datos, esas pruebas corren sin conexión. El despliegue se explicará de forma conceptual.  |
| Pruebas del Sistema | Pruebas básicas con ejemplos de ejecución |
| Documentación final | Descripción, arquitectura, proceso de desarrollo e instrucciones de ejecución |