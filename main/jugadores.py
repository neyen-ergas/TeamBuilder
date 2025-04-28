def jugadoresListaADiccionario(jugadoresLista):
    """
    Convierte una lista de listas de jugadores en una lista de diccionarios.

    Parámetros:
        jugadoresLista (list): Lista de listas, donde cada sublista contiene los datos de un jugador
                               en el orden: nombre, apellido, edad, posición, partidos, goles,
                               asistencias, rating.

    Retorna:
        list: Lista de diccionarios que representan a los jugadores.
    """
    jugadores_dicc = []
    for j in jugadoresLista:
        jugador = {
            "nombre": j[0],
            "apellido": j[1],
            "edad": j[2],
            "posicion": j[3],
            "partidos": j[4],
            "goles": j[5],
            "asistencias": j[6],
            "rating": j[7]
        }
        jugadores_dicc.append(jugador)

    return jugadores_dicc

def mostrarLista():
    """
    Muestra la lista de jugadores actuales en consola.

    Si no hay jugadores cargados, muestra un mensaje informándolo.
    """
    if not jugadores:
        print("No hay jugadores cargados.")
        return

    print("Lista de jugadores:")
    for i, jugador in enumerate(jugadores, start=1):
        print(f"{i}. Nombre: {jugador['nombre']},{jugador['apellido']}, Edad: {jugador['edad']}, "
              f"Posición: {jugador['posicion']}, Partidos: {jugador['partidos']}, "
              f"Goles: {jugador['goles']}, Asistencias: {jugador['asistencias']}")
    print()

def altaJugador():
    """
    Solicita datos al usuario para agregar un nuevo jugador a la lista.

    Se validan nombre, apellido, edad y posición.
    Inicializa partidos, goles, asistencias y rating en cero.
    """
    while True:
        nombre = input("Nombre del jugador: ")
        if nombre.isalpha():
            break
        else:
            print("El nombre debe contener solo letras. Intente nuevamente.")

    while True:
        apellido = input("Apellido del jugador: ")
        if apellido.isalpha():
            break
        else:
            print("El apellido debe contener solo letras. Intente nuevamente.")

    while True:
        edadInput = input("Edad del jugador: ")
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
        else:
            print("Ingrese una opción válida.")

    partidos = 0
    goles = 0
    asistencias = 0
    rating = 0

    jugador = {
        "nombre": nombre,
        "apellido": apellido,
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
    """
    Permite buscar un jugador por nombre y apellido, y editar sus datos.

    Si el campo de actualización se deja vacío, mantiene el valor anterior.
    """
    if not jugadores:
        print("No hay jugadores cargados para editar.")
        return

    mostrarLista()
    nombre_buscar = input("Ingrese el nombre del jugador que quiere editar: ")
    apellido_buscar = input("Ingrese el apellido del jugador que quiere editar: ")

    for jugador in jugadores:
        if jugador['nombre'].lower() == nombre_buscar.lower() and jugador['apellido'].lower() == apellido_buscar.lower():
            print(f"Jugador encontrado: {jugador['nombre']} {jugador['apellido']}, Edad: {jugador['edad']}, "
                  f"Posición: {jugador['posicion']}, Partidos: {jugador['partidos']}, "
                  f"Goles: {jugador['goles']}, Asistencias: {jugador['asistencias']}")

            actNombre = input("Nuevo nombre (Enter para mantener): ")
            actApellido = input("Nuevo apellido (Enter para mantener): ")
            actEdad = input("Nueva edad (Enter para mantener): ")
            actPosicion = input("Nueva posición (Enter para mantener): ")

            if actNombre:
                jugador['nombre'] = actNombre
            if actApellido:
                jugador['apellido'] = actApellido
            if actEdad.isdigit():
                jugador['edad'] = int(actEdad)
            if actPosicion:
                jugador['posicion'] = actPosicion

            print("Jugador actualizado exitosamente.")
            return

    print("Jugador no encontrado.")

def bajaJugador():
    """
    Permite eliminar un jugador de la lista buscando por nombre y apellido.

    Si el jugador no se encuentra, informa al usuario.
    """
    if not jugadores:
        print("No hay jugadores cargados para eliminar.")
        return

    nombre_buscar = input("Ingrese el nombre del jugador que quiere eliminar: ")
    apellido_buscar = input("Ingrese el apellido del jugador que quiere eliminar: ")

    for i, jugador in enumerate(jugadores):
        if jugador['nombre'].lower() == nombre_buscar.lower() and jugador['apellido'].lower() == apellido_buscar.lower():
            print(f"Jugador encontrado y eliminado: {jugador}")
            jugadores.pop(i)
            print("Jugador eliminado exitosamente.")
            return

    print("Jugador no encontrado.")
