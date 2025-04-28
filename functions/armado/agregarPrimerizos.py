import random

def asignarPrimerizos(equipo1, equipo2, primerizos):

    """
    Distribuye aleatoriamente jugadores primerizos entre dos equipos de forma alternada.

    Args:
        equipo1 (list): Lista inicial para el primer equipo.
        equipo2 (list): Lista inicial para el segundo equipo.
        primerizos (list): Lista de jugadores primerizos a repartir.

    Returns:
        tuple: Dos listas actualizadas (equipo1, equipo2) con los jugadores distribuidos.

    Notas:
        - Los jugadores primerizos se mezclan aleatoriamente antes de ser asignados.
        - Se asignan alternadamente basándose en el índice.
    """
    
    random.shuffle(primerizos) 

    for i, jugador in enumerate(primerizos):
        if i % 2 == 0:
            equipo1.append(jugador)
        else:
            equipo2.append(jugador)

    return equipo1, equipo2