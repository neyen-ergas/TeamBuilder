def creadorEquipos(jugadores):
    """
    Crea dos equipos equilibrados basados en el rating de los jugadores.

    Args:
        jugadores (list): Lista de diccionarios, cada uno con las claves 'nombre' y 'rating'.

    Returns:
        tuple: (equipo1, equipo2, puntaje1, puntaje2)
            - equipo1 (list): Nombres de los jugadores del primer equipo.
            - equipo2 (list): Nombres de los jugadores del segundo equipo.
            - puntaje1 (int): Suma de los ratings del primer equipo.
            - puntaje2 (int): Suma de los ratings del segundo equipo.

    Notas:
        - Los jugadores se ordenan de mayor a menor rating.
        - El sistema intenta balancear tanto en número de jugadores como en puntaje total.
    """
    jugadores_ordenados = sorted(jugadores, key=lambda x: x["promedio"], reverse=True)

    equipo1 = []
    equipo2 = []
    puntaje1 = 0.0
    puntaje2 = 0.0

    for jugador in jugadores_ordenados:
        nombre_completo = f"{jugador['nombre']} {jugador['apellido']}"
        if len(equipo1) < len(jugadores) // 2 and (puntaje1 <= puntaje2 or len(equipo2) >= len(jugadores) // 2):
            equipo1.append(nombre_completo)
            puntaje1 += jugador["promedio"]
        else:
            equipo2.append(nombre_completo)
            puntaje2 += jugador["promedio"]

    return equipo1, equipo2, puntaje1, puntaje2