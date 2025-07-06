import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.armado import seleccionJugadoresEquipo, creadorEquipos
from functions.archivos import manejoJson
from functions.jugadores import jugadores as j
from functions.ratings import top5
from functions.partido.cargarEstadisticas import cargarEstadisticas
from functions.partido.guardarRegistros import guardarRegistro
from functions.partido.actualizarEstadisticas import actualizar_estadisticas


def menuCrearPartido():
    """
    Muestra un submenú con opciones relacionadas a la creación de un nuevo partido.

    Opciones:
        1 - Crear Partido: inicia el proceso de armado de equipos.
        2 - Volver: retorna al menú principal.

    Notas:
        - Valida la entrada del usuario para evitar opciones incorrectas.
        - Llama a la función 'crearPartido()' si se selecciona la opción 1.
    """
    print()
    print()
    print()
    print()
    print("¿Que acción quiere realizar?") 
    print("1. Crear Partido")
    print("2. Volver al menú principal")
    

    n = int(input("Ingresar acción: "))
    while n != 1 and n != 2:
        print("Ingresar una acción válida.")
        n = int(input("Ingresar acción: "))
    if n == 1:
        crearPartido()
    elif n == 2:
        main()


    
def crearPartido():
    """
    Inicia el proceso de armado de un partido con equipos equilibrados.

    Flujo:
        1. Solicita cuántos jugadores por equipo (entre 5 y 11).
        2. Valida que haya suficientes jugadores en la base de datos.
        3. Permite seleccionar manualmente a los jugadores que participarán.
        4. Usa el algoritmo de 'creadorEquipos' para generar los equipos equilibrados.
        5. Muestra por pantalla los equipos y el promedio de cada uno.

    Notas:
        - Se asegura de que se ingresen solo valores válidos.
        - La cantidad total de jugadores seleccionados será el doble del valor ingresado.
    """

    if os.path.exists("registroPartido.json"):
        os.remove("registroPartido.json")

    print("\n=== CREAR PARTIDO ===")
    print("¿Cuántos jugadores por equipo? (5 a 11)")
    
    while True:
        try:
            num = int(input("Ingresar cantidad: "))
            if 5 <= num <= 11:
                break
            else:
                print("❌ Debe estar entre 5 y 11.")
        except ValueError:
            print("❌ Ingresá un número válido.")

    total_jugadores = len(manejoJson.cargar_jugadores())

    while total_jugadores < num * 2:
        print(f"⚠️ No hay suficientes jugadores para 2 equipos de {num}. (Total disponibles: {total_jugadores})")
        try:
            num = int(input("Elegí un número menor de jugadores por equipo: "))
            if num < 5 or num > 11:
                print("❌ Número fuera de rango (5-11).")
        except ValueError:
            print("❌ Ingresá un número válido.")

    jugadoresPartido = seleccionJugadoresEquipo.agregar_jugador_a_partido(num * 2)
    equipo1, equipo2, puntaje1, puntaje2 = creadorEquipos.creadorEquipos(jugadoresPartido)

    print("\n" + "=" * 40)
    print(f"{'Equipos de Fútbol':^40}")
    print("=" * 40)
    print(f"{'Equipo 1':<20} {'Equipo 2':<20}")
    print("-" * 40)

    for j1, j2 in zip(equipo1, equipo2):
        print(f"{j1:<20} {j2:<20}")

    print("-" * 40)
    print(f"{'Promedio Equipo 1:':<20} {puntaje1:<20.1f}")
    print(f"{'Promedio Equipo 2:':<20} {puntaje2:<20.1f}")
    print("=" * 40)

    guardarRegistro(jugadoresPartido)

    print("")
    n = int(input("Presione 1 para finalizar el partido: "))

    if n == 1:
        cargarEstadisticas()
        actualizar_estadisticas()
        print("✅ Estadísticas actualizadas correctamente.")
        print("✅ Registro guardado correctamente.")
        


def menuJugadores():
    """
    Muestra un submenú para gestionar jugadores.

    Opciones:
        1 - Mostrar lista de jugadores.
        2 - Dar de alta un nuevo jugador.
        3 - Editar los datos de un jugador existente.
        4 - Eliminar un jugador de la base de datos.
        5 - Volver al menú principal.

    Notas:
        - Llama a funciones del módulo 'jugadores' para cada acción.
        - Valida la opción seleccionada antes de continuar.
    """
    print()
    print()
    print("¿Que acción quiere realizar?") 
    print("1. Mostrar lista de jugadores")
    print("2. Alta de jugador")
    print("3. Editar jugador")
    print("4. Baja de jugador")
    print("5. Volver al menú principal")

    n = int(input("Ingresar acción: "))
    while n < 0 and n > 5:
        print("Ingresar una acción válida.")
        n = int(input("Ingresar acción: "))

    if n == 1:
        j.mostrar_lista()
        menuJugadores()
    elif n == 2:
        j.altaJugador()
        menuJugadores()
    elif n == 3:
        j.editarJugador()
        menuJugadores()
    elif n == 4:
        j.bajaJugador()
        menuJugadores()
    elif n == 5:
        main()
        

def main():
    """
    Función principal que lanza el menú inicial de la aplicación.

    Opciones:
        1 - Crear Partido.
        2 - Administración de jugadores.
        3 - Ver estadísticas.
        4 - Salir del programa.

    Notas:
        - Es la primera función que se ejecuta.
        - Controla la navegación hacia los demás submenús.
        - La validación de opciones tiene un error lógico en la condición del while (debería ser `while n < 1 or n > 4`).
    """
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("------Bienvenido a la aplicación de TeamBuilder------")
    print("¿Que acción quiere realizar?")
    print("1. Crear Partido")
    print("2. Administración de jugadores")
    print("3. Estadísticas")                   
    print("4. Salir")
    

    n = int(input("Ingresar acción: "))
    while n < 0 and n > 3:
        print("Ingresar una acción válida.")
        n = int(input("Ingresar acción: "))

    if n == 1:
        menuCrearPartido()
    elif n == 2:
        menuJugadores()
    elif n == 3:            
        menuEstadisticas()
    else:
        print("¡Hasta pronto!")

def menuEstadisticas():
    """
    Muestra un submenú para consultar diferentes estadísticas de jugadores.

    Opciones:
        1 - Top 5 goleadores.
        2 - Top 5 asistidores.
        3 - Top 5 más activos.
        4 - Top 5 con mejor promedio.
        5 - Top 5 con peor promedio.
        6 - Volver al menú principal.

    Notas:
        - Cada opción muestra un ranking generado por funciones del módulo 'top5'.
        - Después de mostrar el ranking, solicita al usuario que presione 1 para volver.
    """

    print("¿De qué quiere ver estadísticas?")
    print("1. Top 5 goleadores")
    print("2. Top 5 asistidores") 
    print("3. Top 5 más activos")
    print("4. Top 5 mas ganadores")
    print("5. Top 5 mas perdedores")
    print("6. Volver atras")

    n = int(input("Ingresar acción: "))
    if   n == 1:
        top5.goleadores()
        print("1. Volver atras")
        n2 = int(input("Escriba '1' para volver atras: "))
        if   n2 == 1:
            menuEstadisticas()
    elif n == 2:
        top5.asistidores()
        print("1. Volver atras")
        n2 = int(input("Escriba '1' para volver atras: "))
        if   n2 == 1:
            menuEstadisticas()
    elif n == 3:
        top5.activos()
        print("1. Volver atras")
        n2 = int(input("Escriba '1' para volver atras: "))
        if   n2 == 1:
            menuEstadisticas()
    elif n == 4:
        top5.ganadores()
        print("1. Volver atras")
        n2 = int(input("Escriba '1' para volver atras: "))
        if   n2 == 1:
            menuEstadisticas()
    elif n == 5:
        top5.perdedores()
        print("1. Volver atras")
        n2 = int(input("Escriba '1' para volver atras: "))
        if   n2 == 1:
            menuEstadisticas()
    elif n == 6:
        main()
    

main()
