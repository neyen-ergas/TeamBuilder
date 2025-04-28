import random

def creadorPrimerizos(jugadores):
    """
    Divide aleatoriamente una lista de jugadores en dos equipos iguales.

    Args:
        jugadores (list): Lista de jugadores a repartir.

    Returns:
        tuple: Dos listas (equipo1, equipo2) representando cada equipo.

    Notas:
        - La lista de jugadores se mezcla antes de ser dividida.
        - Si el número de jugadores es impar, uno de los equipos puede tener un jugador menos.
    """
    random.shuffle(jugadores)
    mitad = len(jugadores) // 2

    equipo1 = jugadores[:mitad]
    equipo2 = jugadores[mitad:]

    return equipo1, equipo2