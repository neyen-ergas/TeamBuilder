
def menuCrearPartido():
    #TODO print("¿Que plantilla quiere usar?")
    print("¿De cuantos jugadores van a ser los equipos?") #doy opciones? dejo que el usuario elija y desp checkeo?
    print("¿5, 6, 7, 8, 9, 10 u 11?")
    num = int(input("Ingresar cantidad de jugadores por equipo: "))
    while num < 5 or num > 11:
        print("Número no válido.")
        num = int(input("Ingresar cantidad de jugadores por equipo: "))

    #TODO algoritmo de seleccion de jugadores

def menuJugadores():
    print("¿Que acción quiere realizar?") #seleccionar plantilla??
    print("1. Alta de jugador")
    print("2. Editar jugador")
    print("3 Baja de jugador")

def menuEstadisticas():
    print("¿De qué quiere ver estadísticas?")
    print("1. Estadísticas de jugadores")
    print("2. Estadísticas de plantilla") #????

def main():
    print("------Bienvenido a la aplicación de TeamBuilder------")
    print("¿Que acción quiere realizar?")
    print("1. Crear Partido")
    print("2. Administración de jugadores")
    print("3. Estadísticas")
    print("4. Salir")

    n = int(input("Ingresar acción: "))

    if n == 1:
        menuCrearPartido()
    elif n == 2:
        menuJugadores()
    else:
        menuEstadisticas()
    
    

    