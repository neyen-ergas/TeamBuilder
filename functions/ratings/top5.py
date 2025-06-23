from functions.archivos import manejoJson

def goleadores():
    """
    Muestra en consola el Top 5 de jugadores con más goles convertidos.

    Notas:
        - Ordena la lista de jugadores por la clave 'goles' en orden descendente.
        - Solo se muestran los primeros cinco jugadores.
        - En caso de empate en goles, el orden dependerá del orden en la lista original.
    """
    jugadores = manejoJson.cargar_jugadores()
    top = sorted(jugadores, key=lambda j: j["goles"], reverse=True)[:5]
    print("\nTop 5 Goleadores:")
    for j in top:
        print(f"- {j['nombre']} {j['apellido']}: {j['goles']} goles")


def asistidores():
    """
    Muestra en consola el Top 5 de jugadores con más asistencias realizadas.

    Notas:
        - Ordena la lista de jugadores por la clave 'asistencias' en orden descendente.
        - Solo se muestran los cinco primeros jugadores.
    """
    jugadores = manejoJson.cargar_jugadores()
    top = sorted(jugadores, key=lambda j: j["asistencias"], reverse=True)[:5]
    print("\nTop 5 Asistidores:")
    for j in top:
        print(f"- {j['nombre']} {j['apellido']}: {j['asistencias']} asistencias")


def activos():
    """
    Muestra en consola el Top 5 de jugadores con más partidos jugados.

    Notas:
        - Ordena por la cantidad de partidos jugados en orden descendente.
        - Refleja qué jugadores participaron más activamente en los encuentros registrados.
    """
    jugadores = manejoJson.cargar_jugadores()
    top = sorted(jugadores, key=lambda j: j["partidos_jugados"], reverse=True)[:5]
    print("\nTop 5 Jugadores Más Activos:")
    for j in top:
        print(f"- {j['nombre']} {j['apellido']}: {j['partidos_jugados']} partidos")


def ganadores():
    """
    Muestra en consola el Top 5 de jugadores con mejor promedio general.

    Notas:
        - Ordena por la clave 'promedio' en orden descendente.
        - El promedio representa el rendimiento global del jugador en partidos anteriores.
    """
    jugadores = manejoJson.cargar_jugadores()
    top = sorted(jugadores, key=lambda j: j["promedio"], reverse=True)[:5]
    print("\nTop 5 Jugadores Más Ganadores (Promedio más alto):")
    for j in top:
        print(f"- {j['nombre']} {j['apellido']}: promedio {j['promedio']}")


def perdedores():
    """
    Muestra en consola el Top 5 de jugadores con peor promedio general.

    Notas:
        - Ordena por la clave 'promedio' en orden ascendente.
        - Refleja a los jugadores con menor rendimiento en el sistema.
    """
    jugadores = manejoJson.cargar_jugadores()
    top = sorted(jugadores, key=lambda j: j["promedio"])[:5]
    print("\nTop 5 Jugadores Más Perdedores (Promedio más bajo):")
    for j in top:
        print(f"- {j['nombre']} {j['apellido']}: promedio {j['promedio']}")