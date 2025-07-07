import csv
import json
import os

def exportarStats():
    RUTA_JUGADORES = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/json/jugadores.json"))
    
    with open(RUTA_JUGADORES, "r", encoding="utf-8") as f:
        data = json.load(f)

    ruta_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../export/estadisticas.csv"))
    os.makedirs(os.path.dirname(ruta_csv), exist_ok=True)

    campos = [
        "Nombre", "Apellido", "Edad", "Posición", "Partidos Jugados",
        "Goles", "Asistencias", "Promedio de Calificación",
        "Partidos Ganados", "Partidos Perdidos", "Partidos Empatados"
    ]

    with open(ruta_csv, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(campos)
        for jugador in data["jugadores"]:
            fila = [
                jugador.get("nombre", ""),
                jugador.get("apellido", ""),
                jugador.get("edad", ""),
                jugador.get("posición", ""),
                jugador.get("partidos_jugados", 0),
                jugador.get("goles", 0),
                jugador.get("asistencias", 0),
                f"{jugador.get('promedio', 0):.2f}",
                jugador.get("ganados", 0),
                jugador.get("perdidos", 0),
                jugador.get("empatados", 0),
                jugador.get("rachas", 0),
            ]
            writer.writerow(fila)

    print(f"✅ Exportado a: {ruta_csv}")