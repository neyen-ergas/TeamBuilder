def creadorEquipos(jugadores):
    jugadores_ordenados = sorted(jugadores, key=lambda x: x[4], reverse=True)

    equipo1 = []
    equipo2 = []
    puntaje1 = 0
    puntaje2 = 0

    for jugador in jugadores_ordenados:
        if len(equipo1) < len(jugadores) // 2 and (puntaje1 <= puntaje2 or len(equipo2) >= len(jugadores) // 2):
            equipo1.append(jugador)
            puntaje1 += jugador[4]
        else:
            equipo2.append(jugador)
            puntaje2 += jugador[4]

    return equipo1, equipo2, puntaje1, puntaje2
#test