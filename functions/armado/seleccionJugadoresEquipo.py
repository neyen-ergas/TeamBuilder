import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import jugadoresEjemplo
from functions.jugadores import jugadores

jugadores = jugadores.jugadoresListaADiccionario(jugadoresEjemplo.jugadores)

def buscar_jugador(jugadores, nombre):
    for jugador in jugadores:
        if nombre.lower() == jugador['nombre'].lower():  
            return jugador
    return None  

def agregar_jugador_a_partido(cantidad):
    jugadores_partido = []
    i = 0  
    while i < cantidad:
        nombre = input("Ingrese nombre del jugador: ")
        jugador = buscar_jugador(jugadores, nombre)
        if jugador:  
            jugadores_partido.append(jugador)
            i += 1  
        else:
            print(f"Jugador {nombre} no encontrado. Intenta nuevamente.")
    return jugadores_partido


