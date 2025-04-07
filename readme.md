Proyecto TeamBuilder: ALGORITMOS Y ESTRUCTURAS DE DATOS I
Integrantes:
Nicolás Diez - LU:

Lucio Dillon - LU: 1156126

Neyen Ergas - LU: 1209504

Iván Rapisarda - LU: 1055142

Introducción
Normalmente, en encuentros informales entre amigos, solemos encontrarnos con el desafío de armar equipos equilibrados para que los partidos sean parejos y disfrutables. Esta tarea, aunque cotidiana, puede volverse subjetiva, repetitiva o generar desbalances que afectan la experiencia de juego.

En este contexto, surge la idea de desarrollar TeamBuilder, una aplicación que desarrollaremos en Python donde se permita gestionar jugadores, formar equipos balanceados de forma automatizada y registrar el resultado de los partidos. A través del uso de estadísticas individuales, calificaciones y resultados históricos, el sistema ajustará el rendimiento proyectado de cada jugador y mejorará progresivamente la equidad en los equipos generados.

El proyecto apunta a ser una solución práctica y original que responde a una necesidad concreta del día a día.

Alcance del Producto
El sistema permitirá organizar partidos de fútbol amateur entre amigos mediante el armado automático de equipos balanceados. Se mantendrá una base de datos de jugadores con estadísticas como goles, partidos jugados, calificaciones y rendimiento. El sistema registrará los resultados de cada partido, actualizará automáticamente las estadísticas y mejorará el algoritmo de armado en función de los datos acumulados.

El producto será una aplicación de consola escrita en Python, utilizando archivos para persistencia de datos y dividiendo el sistema en módulos independientes.

Requisitos Funcionales
Gestión de jugadores
El sistema debe permitir agregar, editar y eliminar jugadores.

Cada jugador debe tener asociados: nombre, partidos jugados, goles, promedio de calificaciones, racha de rendimiento y rating general.

El sistema debe permitir visualizar la base de datos completa de jugadores con sus estadísticas actualizadas.

Selección de jugadores para un partido
El usuario podrá seleccionar un grupo de jugadores activos para el próximo partido.

El sistema debe permitir elegir una cantidad de jugadores para formar dos equipos.

Armado automático de equipos
El sistema debe generar dos equipos lo más parejos posible según las estadísticas de los jugadores seleccionados.

El cálculo debe considerar como mínimo: rating general, promedio de calificaciones, goles y racha.

El sistema debe mostrar el resultado del armado, indicando las estadísticas totales por equipo.

Registro de partido
El sistema debe permitir registrar:

El resultado final (goles por equipo).

Los goles anotados por cada jugador.

Las calificaciones individuales de cada jugador (por ejemplo, del 1 al 10).

Al registrar un partido, el sistema debe actualizar automáticamente las estadísticas de los jugadores involucrados.

Historial y análisis
El sistema debe guardar un historial de todos los partidos jugados.

Debe poder mostrar:

Ranking de jugadores según rating promedio.

Tabla de goleadores.

Jugadores en racha positiva o negativa.

Persistencia de datos
Todos los datos (jugadores y partidos) deben ser guardados y cargados automáticamente desde archivos JSON.

El sistema debe mantener la persistencia entre ejecuciones.

Validaciones y manejo de errores
El sistema debe validar entradas del usuario: nombre de jugador, número de goles, calificación, etc.

Debe manejar errores comunes como:

Jugador inexistente.

Formato incorrecto de entrada.

Número impar de jugadores seleccionados.

Pruebas unitarias
El sistema debe incluir pruebas unitarias para verificar:

Cálculo de rating y promedio.

Balanceo de equipos.

Actualización de estadísticas tras un partido.

Entregables
🔹 Entregable 40% – Versión Inicial
Objetivo: Sistema básico funcional para cargar jugadores y armar equipos.

Características:

Gestión de jugadores: alta, baja, edición, visualización.

Guardado de datos en JSON.

Selección de jugadores para un partido.

Algoritmo simple de armado de equipos (por promedio de rating).

Menú interactivo en consola.

Modularización inicial del código.

🔸 Entregable 80% – Versión Intermedia
Objetivo: Sistema funcional casi completo con registro de partidos y actualización de stats.

Características:

Registro de partidos jugados.

Registro de goles por jugador y resultado del partido.

Calificación de jugadores.

Actualización automática de estadísticas (rating, promedio, partidos jugados).

Visualización de rankings y tabla de goleadores.

Mejoras en el algoritmo de balance (ponderación por racha).

Pruebas unitarias básicas para cálculo de stats.

Validaciones de entradas (formato, existencia, etc.).

🔹 Entregable 100% – Versión Final
Objetivo: Producto terminado, estable, probado y listo para presentación.

Características:

Historial completo de partidos con exportación.

Jugadores en racha: bonus o penalización en el armado.

Sistema refinado de ranking (ponderado por rendimiento reciente).

Pruebas unitarias completas.

Archivos bien estructurados, menús refinados y comentarios/documentación.

Preparación de defensa y demo en consola.

(Opcional si hay tiempo: simulador de torneo, estadísticas más profundas, exportación en TXT).
