import json
import os

RUTA_JSON = os.path.join(os.path.dirname(__file__), "../../src/json/jugadores.json")

def cargar_jugadores():
    with open(RUTA_JSON, "rt", encoding="utf-8") as file:
        return json.load(file)

def guardar_jugadores(jugadores):
    with open(RUTA_JSON, "wt", encoding="utf-8") as file:
        json.dump(jugadores, file, indent=2, ensure_ascii=False)

def agregar_jugador(nuevo_jugador):
    jugadores = cargar_jugadores()
    jugadores.append(nuevo_jugador)
    guardar_jugadores(jugadores)

def borrar_jugador(nombre, apellido):
    jugadores = cargar_jugadores()
    jugadores = [j for j in jugadores if not (j["nombre"] == nombre and j["apellido"] == apellido)]
    guardar_jugadores(jugadores)

def modificar_jugador(nombre, apellido, nuevos_datos):
    jugadores = cargar_jugadores()
    for j in jugadores:
        if j["nombre"] == nombre and j["apellido"] == apellido:
            j.update(nuevos_datos)
            break
    guardar_jugadores(jugadores)
