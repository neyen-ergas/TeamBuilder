import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.armado import seleccionJugadoresEquipo, creadorEquipos
from functions.archivos import manejoJson
from functions.jugadores import jugadores as j
from functions.partido.cargarEstadisticas import cargarEstadisticas
from functions.partido.guardarRegistros import guardarRegistro
from functions.partido.actualizarEstadisticas import actualizar_estadisticas


def menuCrearPartido():
    #TODO print("¿Que plantilla quiere usar?")
    #TODO algoritmo de seleccion de jugadores
    print()
    print()
    print()
    print()
    print("¿Que acción quiere realizar?") #seleccionar plantilla??
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
    print()
    print()
    print("¿Que acción quiere realizar?") #seleccionar plantilla??
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
    # print("3. Estadísticas")                     #TODO
    print("3. Salir")
    

    n = int(input("Ingresar acción: "))
    while n < 0 and n > 3:
        print("Ingresar una acción válida.")
        n = int(input("Ingresar acción: "))

    if n == 1:
        menuCrearPartido()
    elif n == 2:
        menuJugadores()
    # elif n == 3:            #TODO
    #     menuEstadisticas()
    else:
        print("¡Hasta pronto!")
    

main()


#TODO

# def menuEstadisticas():
#     print("¿De qué quiere ver estadísticas?")
#     print("1. Estadísticas de jugadores")
#     #print("2. Estadísticas de plantilla") 
#     print("3. Volver al menú principal")

#     n = int(input("Ingresar acción: "))
#     if n == 1:
#         menuCrearPartido()
#     elif n == 2:
#         menuJugadores()
#     elif n == 3:
#         menuEstadisticas()