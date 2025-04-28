import random

def manejar_impar(jugadores):
    """
    Gestiona el caso en que la cantidad de jugadores sea impar seleccionando un suplente.

    Args:
        jugadores (list): Lista de jugadores.

    Returns:
        tuple: (jugadores_actualizados, suplente)
            - jugadores_actualizados (list): Lista con cantidad par de jugadores.
            - suplente (str or None): El jugador removido o None si no fue necesario.

    Notas:
        - Si la cantidad es impar, se elige aleatoriamente un suplente.
        - Si es par, no se realiza ninguna modificación.
    """
    if len(jugadores) % 2 != 0:
        suplente = random.choice(jugadores)
        jugadores.remove(suplente)
        return jugadores, suplente
    else:
        return jugadores, None