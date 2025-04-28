import random

def manejar_impar(jugadores):
    if len(jugadores) % 2 != 0:
        suplente = random.choice(jugadores)
        jugadores.remove(suplente)
        return jugadores, suplente
    else:
        return jugadores, None