import random

def creadorPrimerizos(jugadores):
    random.shuffle(jugadores)
    mitad = len(jugadores) // 2

    equipo1 = jugadores[:mitad]
    equipo2 = jugadores[mitad:]

    return equipo1, equipo2