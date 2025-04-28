jugadores = []

numJugadores = 0

for jugador in jugadores:
    numJugadores += 1

#TODO agregar ids jugadores

def mostrarLista():
    if not jugadores:
        print("No hay jugadores cargados.")
        return

    print("Lista de jugadores:")
    for i, jugador in enumerate(jugadores, start = 1):
        print(f"{i}. Nombre: {jugador['nombre']}, Edad: {jugador['edad']}, Posición: {jugador['posicion']}, Partidos jugados: {jugador['partidos']}, Goles: {jugador['goles']}, Asistencias: {jugador['asistencias']}")
    print()


def altaJugador():
    while True:
        nombre = input("Nombre del jugador: ")
        if nombre.isalpha():
            break
        else:
            print("El nombre debe contener solo letras. Intente nuevamente.")
        nombre = input("Nombre del jugador: ")

    for jugador in jugadores:
        if jugador[nombre].lower() == nombre.lower():
            print("Ya existe un jugador con ese nombre. Intente utilizar otro nombre.")
            nombre = input("Nombre del jugador: ")

    while True:
        edadInput = input("Edad del jugador: ")
        edad = 0
        if edadInput.isdigit():
            edad = int(edadInput)
            break
        else:
            print("La edad debe ser un número entero. Intente nuevamente.")


    while True:
        print("Posición del jugador: ")
        print("1. ARQ")
        print("2. DEF")
        print("3. MC")
        print("4. DEL")
        posInput = input("Ingresar posición: ")

        if posInput.isdigit():
            posicion = int(posInput)
            if posicion == 1:
                posicion = 'ARQ'
                break
            elif posicion == 2:
                posicion = 'DEF'
                break
            elif posicion == 3:
                posicion = 'MC'
                break
            elif posicion == 4:
                posicion = 'DEL'
                break
            else:
                print("Error. Intente nuevamente.")
                print("1. ARQ")
                print("2. DEF")
                print("3. MC")
                print("4. DEL")
        else:
            print("Ingrese una opción válida.")
            print("1. ARQ")
            print("2. DEF")
            print("3. MC")
            print("4. DEL")
            posInput = input("Ingresar posición: ")

    partidos = 0
    goles = 0
    asistencias = 0
    rating = 0

    jugador = {
        "nombre": nombre,
        "edad": edad,
        "posicion": posicion,
        "partidos": partidos,
        "goles": goles,
        "asistencias": asistencias,
        "rating": rating
    }

    jugadores.append(jugador)
    print("Jugador agregado exitosamente.")

def editarJugador():
    if not jugadores:
        print("No hay jugadores cargados para editar")
        print()
        return

    mostrarLista()
    nombre_buscar = input("Ingrese el nombre del jugador que quiere editar: ")

    for jugador in jugadores:
        if jugador[nombre].lower() == nombre.lower():
            print("Ya existe un jugador con ese nombre. Intente utilizar otro nombre.")
            nombre = input("Nombre del jugador: ")

        if jugador['nombre'].lower() == nombre_buscar.lower():
            print(f"Jugador encontrado: Nombre: {jugador['nombre']}, Edad: {jugador['edad']}, Posición: {jugador['posicion']}, Partidos jugados: {jugador['partidos']}, Goles: {jugador['goles']}, Asistencias: {jugador['asistencias']}")
            actNombre = input("Nuevo nombre (Enter para mantener): ")
            actEdad = input("Nueva edad (Enter para mantener): ")
            actPosicion = input("Nueva posición (Enter para mantener): ")

            if actNombre:
                jugador['nombre'] = actNombre
            elif actEdad:
                jugador['edad'] = int(actEdad)
            elif actPosicion:
                jugador['posicion'] = actPosicion

            print("Jugador actualizado exitosamente.")
            return

    print("Jugador no encontrado.")
    nombre_buscar = input("Ingrese el nombre del jugador que quiere editar: ")

def bajaJugador():

    if not jugadores:
        print("No hay jugadores cargados para eliminar.")
        return

    nombre_buscar = input("Ingrese el nombre del jugador que quiere eliminar: ")

    for i, jugador in enumerate(jugadores):
        if jugador['nombre'].lower() == nombre_buscar.lower():
            print(f"Jugador encontrado y eliminado: {jugador}")
            jugadores.pop(i)
            print("Jugador eliminado exitosamente.")
            return

    print("Jugador no encontrado.")
