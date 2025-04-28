
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import jugadores as j
from functions.creadorEquipos import creadorEquipos

def menuCrearPartido():
    #TODO print("¿Que plantilla quiere usar?")
    #TODO algoritmo de seleccion de jugadores
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
    print("¿De cuantos jugadores van a ser los equipos?") #doy opciones? dejo que el usuario elija y desp checkeo?
    print("¿5, 6, 7, 8, 9, 10 u 11?")
    num = int(input("Ingresar cantidad de jugadores por equipo: "))
    while num < 5 or num > 11:
        print("Número no válido.")
        num = int(input("Ingresar cantidad de jugadores por equipo: "))


    while j.numJugadores < num * 2:
        print("No hay suficientes jugadores en la plantilla para hacer 2 equipos de", num, "jugadores, elija un número menor.")
        num = int(input("Ingresar cantidad de jugadores por equipo: "))

    if j.numJugadores > num * 2:
        print("Van a haber suplentes, se seleccionarán al azar.")
    else:
        creadorEquipos()

def menuJugadores():
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
        j.mostrarLista()
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
#     #print("2. Estadísticas de plantilla") #????
#     print("3. Volver al menú principal")

#     n = int(input("Ingresar acción: "))
#     if n == 1:
#         menuCrearPartido()
#     elif n == 2:
#         menuJugadores()
#     elif n == 3:
#         menuEstadisticas()
