import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.archivos import manejoJson


def buscar_jugador_por_nombre(nombre):
    """
    Busca jugadores por nombre ignorando mayúsculas y minúsculas.

    Args:
        nombre (str): Nombre del jugador a buscar.

    Returns:
        list: Lista de jugadores cuyo nombre coincide exactamente, sin distinguir mayúsculas.

    Notas:
        - Si hay varios jugadores con el mismo nombre, se devuelven todos.
        - No filtra por apellido.
    """
    jugadores = manejoJson.cargar_jugadores()
    return [j for j in jugadores if j["nombre"].lower() == nombre.lower()]


def buscar_jugador(nombre, apellido):
    """
    Busca un jugador por nombre y apellido (case-insensitive).

    Args:
        nombre (str): Nombre del jugador.
        apellido (str): Apellido del jugador.

    Returns:
        dict or None: El jugador encontrado o None si no existe.

    Notas:
        - La comparación no distingue mayúsculas ni minúsculas.
        - Devuelve solo el primer jugador que coincida exactamente.
    """
    jugadores = manejoJson.cargar_jugadores()
    for jugador in jugadores:
        if jugador["nombre"].lower() == nombre.lower() and jugador["apellido"].lower() == apellido.lower():
            return jugador
    return None


def agregar_jugador_a_partido(cantidad):
    """
    Permite seleccionar manualmente una cantidad de jugadores para un partido.

    Args:
        cantidad (int): Número total de jugadores que deben ser seleccionados.

    Returns:
        list: Lista de diccionarios con los datos de los jugadores seleccionados.

    Notas:
        - Se realiza una búsqueda por nombre y, si hay ambigüedad, se pide el apellido.
        - No permite seleccionar al mismo jugador más de una vez.
        - Valida que el jugador exista antes de agregarlo.
    """
    jugadores_partido = []
    print(f"\n--- Selección de {cantidad} jugadores para el partido ---")

    i = 0
    while i < cantidad:
        print(f"\nJugador {i+1} de {cantidad}")

        nombre = input("Ingrese nombre: ").strip()
        candidatos = buscar_jugador_por_nombre(nombre)

        if len(candidatos) == 0:
            print(f"⚠️ No hay jugadores con el nombre '{nombre}'. Intente nuevamente.")
            continue
        elif len(candidatos) == 1:
            jugador = candidatos[0]
        else:
            # Hay más de uno con ese nombre, pedimos apellido para desambiguar
            apellido = input(f"Hay {len(candidatos)} jugadores con el nombre '{nombre}'. Ingrese apellido: ").strip()
            jugador = None
            for j in candidatos:
                if j["apellido"].lower() == apellido.lower():
                    jugador = j
                    break
            if jugador is None:
                print(f"⚠️ No se encontró jugador con nombre '{nombre}' y apellido '{apellido}'. Intente nuevamente.")
                continue

        if jugador in jugadores_partido:
            print("⚠️ Ese jugador ya fue agregado.")
        else:
            jugadores_partido.append(jugador)
            print("✅ Jugador agregado.")
            i += 1

    return jugadores_partido
