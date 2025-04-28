def creadorEquipos(jugadores):
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