import json
import os

RUTA_JSON = os.path.join(os.path.dirname(__file__), "../../src/json/registroPartido.json")

def guardarRegistro(jugadores, equipo1, equipo2):
    datos = {"jugadores": []}
    
    for jugador in jugadores:
        
        nombre_completo = f"{jugador['nombre']} {jugador['apellido']}"
        

        if nombre_completo in equipo1:
            equipo = 1
        elif nombre_completo in equipo2:
            equipo = 2
        
        datos["jugadores"].append({
            "nombre": jugador["nombre"],
            "apellido": jugador["apellido"],
            "goles": 0,
            "asistencias": 0,
            "calificacion": 0,
<<<<<<< HEAD
            "equipo": equipo
=======
            "ganados": 0,
            "perdidos": 0,
            "empatados": 0
>>>>>>> e22fca4eab503e539a4d607e949e18203e453c7f
        })

    with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)