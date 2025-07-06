import json
import os

RUTA_JSON = os.path.join(os.path.dirname(__file__), "../../src/json/registroPartido.json")

def guardarRegistro(jugadores):
    datos = {"jugadores": []}
    for jugador in jugadores:
        datos["jugadores"].append({
            "nombre": jugador["nombre"],
            "apellido": jugador["apellido"],
            "goles": 0,
            "asistencias": 0,
            "calificacion": 0,
            "ganados": 0,
            "perdidos": 0,
            "empatados": 0
        })

    with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)