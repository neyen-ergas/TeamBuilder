import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.archivos import manejoJson


def mostrar_lista():
    """
    Muestra en consola la lista completa de jugadores registrados con sus estadísticas.

    Notas:
        - Si no hay jugadores cargados, informa al usuario.
        - Muestra nombre, apellido, edad, posición, partidos jugados, goles y asistencias.
    """
    jugadores = manejoJson.cargar_jugadores()
    if not jugadores:
        print("No hay jugadores cargados.")
        return

    print("Lista de jugadores:")
    for i, jugador in enumerate(jugadores, start=1):
        print(f"{i}. Nombre: {jugador['nombre']} {jugador['apellido']}, Edad: {jugador['edad']}, "
              f"Posición: {jugador['posición']}, Partidos: {jugador['partidos_jugados']}, "
              f"Goles: {jugador['goles']}, Asistencias: {jugador['asistencias']}")
    print()

def cantidad_jugadores():
    """
    Devuelve la cantidad total de jugadores registrados.

    Returns:
        int: Número de jugadores actuales en el sistema.
    """
    return len(manejoJson.cargar_jugadores())

def altaJugador():
    """
    Permite cargar un nuevo jugador a través de inputs por consola.

    Notas:
        - Valida que nombre y apellido contengan solo letras.
        - Evita duplicados (mismo nombre y apellido).
        - Solicita la edad y la posición del jugador.
        - Asigna estadísticas iniciales en 0.
        - Agrega el nuevo jugador al archivo JSON.
    """
    jugadores = manejoJson.cargar_jugadores()

    print("\n--- Alta de nuevo jugador ---")

    while True:
        nombre = input("Nombre del jugador: ").strip().capitalize()
        if nombre.isalpha():
            break
        print("El nombre debe contener solo letras.")

    while True:
        apellido = input("Apellido del jugador: ").strip().capitalize()
        if apellido.isalpha():
            break
        print("El apellido debe contener solo letras.")

    for j in jugadores:
        if j["nombre"] == nombre and j["apellido"] == apellido:
            print("⚠️ Ya existe un jugador con ese nombre y apellido.")
            return

    while True:
        edad_input = input("Edad del jugador: ").strip()
        if edad_input.isdigit():
            edad = int(edad_input)
            break
        print("La edad debe ser un número.")

    print("Posición del jugador:")
    print("1. ARQ\n2. DEF\n3. MC\n4. DEL")
    opciones_pos = {"1": "ARQ", "2": "DEF", "3": "MC", "4": "DEL"}

    while True:
        posInput = input("Seleccionar posición (1-4): ").strip()
        if posInput in opciones_pos:
            posicion = opciones_pos[posInput]
            break
        print("Opción inválida. Elegí 1, 2, 3 o 4.")

    jugador = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "posición": posicion,
        "partidos_jugados": 0,
        "goles": 0,
        "asistencias": 0,
        "promedio": 0.0
    }

    manejoJson.agregar_jugador(jugador)
    print("✅ Jugador agregado correctamente.")

def editarJugador():
    """
    Permite editar los datos de un jugador existente.

    Notas:
        - Busca al jugador por nombre y apellido.
        - Permite modificar nombre, apellido, edad y posición.
        - Si un campo se deja vacío, conserva el valor original.
        - Informa si el jugador no existe o si no se realizaron cambios.
    """
    jugadores = manejoJson.cargar_jugadores()

    if not jugadores:
        print("No hay jugadores cargados para editar.")
        return

    print("\n--- Editar jugador ---")
    nombre = input("Nombre del jugador a editar: ").strip().capitalize()
    apellido = input("Apellido del jugador a editar: ").strip().capitalize()

    jugador_encontrado = None
    for jugador in jugadores:
        if jugador["nombre"] == nombre and jugador["apellido"] == apellido:
            jugador_encontrado = jugador
            break

    if not jugador_encontrado:
        print("⚠️ Jugador no encontrado.")
        return

    print(f"\nJugador encontrado: {jugador_encontrado['nombre']} {jugador_encontrado['apellido']}")
    print(f"Edad actual: {jugador_encontrado['edad']}")
    print(f"Posición actual: {jugador_encontrado['posición']}")
    print(f"Partidos jugados: {jugador_encontrado['partidos_jugados']}")
    print(f"Goles: {jugador_encontrado['goles']}")
    print(f"Asistencias: {jugador_encontrado['asistencias']}")
    print(f"Promedio: {jugador_encontrado['promedio']}")

    nuevo_nombre = input("Nuevo nombre (Enter para mantener): ").strip().capitalize()
    nuevo_apellido = input("Nuevo apellido (Enter para mantener): ").strip().capitalize()

    nueva_edad = input("Nueva edad (Enter para mantener): ").strip()
    nueva_posicion = input("Nueva posición (ARQ, DEF, MC, DEL) (Enter para mantener): ").strip().upper()

    nuevos_datos = {}

    if nuevo_nombre:
        nuevos_datos["nombre"] = nuevo_nombre
    if nuevo_apellido:
        nuevos_datos["apellido"] = nuevo_apellido
    if nueva_edad.isdigit():
        nuevos_datos["edad"] = int(nueva_edad)
    elif nueva_edad:
        print("⚠️ Edad inválida. No se modificó.")
    if nueva_posicion in ["ARQ", "DEF", "MC", "DEL"]:
        nuevos_datos["posición"] = nueva_posicion
    elif nueva_posicion:
        print("⚠️ Posición inválida. No se modificó.")

    if nuevos_datos:
        manejoJson.modificar_jugador(nombre, apellido, nuevos_datos)
        print("✅ Jugador modificado con éxito.")
    else:
        print("No se realizaron cambios.")


def bajaJugador():
    """
    Permite eliminar un jugador de la base de datos.

    Notas:
        - Busca por nombre y apellido.
        - Muestra una confirmación antes de eliminar.
        - Si el jugador no existe, informa al usuario.
    """
    jugadores = manejoJson.cargar_jugadores()

    if not jugadores:
        print("No hay jugadores cargados para eliminar.")
        return

    print("\n--- Eliminar jugador ---")
    nombre = input("Nombre del jugador a eliminar: ").strip().capitalize()
    apellido = input("Apellido del jugador a eliminar: ").strip().capitalize()

    jugador_encontrado = None
    for jugador in jugadores:
        if jugador["nombre"] == nombre and jugador["apellido"] == apellido:
            jugador_encontrado = jugador
            break

    if not jugador_encontrado:
        print("⚠️ Jugador no encontrado.")
        return

    print(f"\nJugador encontrado: {jugador_encontrado['nombre']} {jugador_encontrado['apellido']}, "
          f"Edad: {jugador_encontrado['edad']}, Posición: {jugador_encontrado['posición']}")

    confirmacion = input("¿Estás seguro de que querés eliminarlo? (s/n): ").strip().lower()
    if confirmacion == 's':
        manejoJson.borrar_jugador(nombre, apellido)
        print("✅ Jugador eliminado con éxito.")
    else:
        print("❌ Operación cancelada.")




