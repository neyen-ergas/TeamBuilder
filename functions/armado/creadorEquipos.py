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
    jugadores_ordenados = sorted(jugadores, key=lambda x: x['rating'], reverse=True)

    equipo1 = []
    equipo2 = []
    puntaje1 = 0
    puntaje2 = 0

    for jugador in jugadores_ordenados:
        if len(equipo1) < len(jugadores) // 2 and (puntaje1 <= puntaje2 or len(equipo2) >= len(jugadores) // 2):
            equipo1.append(jugador['nombre'])
            puntaje1 += jugador['rating']
        else:
            equipo2.append(jugador['nombre'])
            puntaje2 += jugador['rating']

    return equipo1, equipo2, puntaje1, puntaje2