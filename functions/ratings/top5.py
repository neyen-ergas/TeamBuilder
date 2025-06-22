from functions.archivos import manejoJson

def goleadores():
    """
    Muestra el Top 5 de jugadores con más goles.
    """
    jugadores = manejoJson.cargar_jugadores()
    top = sorted(jugadores, key=lambda j: j["goles"], reverse=True)[:5]
    print("\nTop 5 Goleadores:")
    for j in top:
        print(f"- {j['nombre']} {j['apellido']}: {j['goles']} goles")


def asistidores():
    """
    Muestra el Top 5 de jugadores con más asistencias.
    """
    jugadores = manejoJson.cargar_jugadores()
    top = sorted(jugadores, key=lambda j: j["asistencias"], reverse=True)[:5]
    print("\nTop 5 Asistidores:")
    for j in top:
        print(f"- {j['nombre']} {j['apellido']}: {j['asistencias']} asistencias")


def activos():
    """
    Muestra el Top 5 de jugadores con más partidos jugados.
    """
    jugadores = manejoJson.cargar_jugadores()
    top = sorted(jugadores, key=lambda j: j["partidos_jugados"], reverse=True)[:5]
    print("\nTop 5 Jugadores Más Activos:")
    for j in top:
        print(f"- {j['nombre']} {j['apellido']}: {j['partidos_jugados']} partidos")


def ganadores():
    """
    Muestra el Top 5 de jugadores con mejor promedio.
    """
    jugadores = manejoJson.cargar_jugadores()
    top = sorted(jugadores, key=lambda j: j["promedio"], reverse=True)[:5]
    print("\nTop 5 Jugadores Más Ganadores (Promedio más alto):")
    for j in top:
        print(f"- {j['nombre']} {j['apellido']}: promedio {j['promedio']}")


def perdedores():
    """
    Muestra el Top 5 de jugadores con peor promedio.
    """
    jugadores = manejoJson.cargar_jugadores()
    top = sorted(jugadores, key=lambda j: j["promedio"])[:5]
    print("\nTop 5 Jugadores Más Perdedores (Promedio más bajo):")
    for j in top:
        print(f"- {j['nombre']} {j['apellido']}: promedio {j['promedio']}")