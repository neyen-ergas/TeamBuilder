import json
import os

BASE_DIR = os.path.dirname(__file__)
RUTA_REGISTRO = os.path.join(BASE_DIR, "../../src/json/registroPartido.json")
RUTA_JUGADORES = os.path.join(BASE_DIR, "../../src/json/jugadores.json")

def actualizar_estadisticas():
    if not os.path.exists(RUTA_REGISTRO):
        print(f"❌ No existe el registro de partido: {RUTA_REGISTRO}")
        return
    if not os.path.exists(RUTA_JUGADORES):
        print(f"❌ No existe el archivo de jugadores: {RUTA_JUGADORES}")
        return

    with open(RUTA_REGISTRO, "r", encoding="utf-8") as f:
        registro = json.load(f)

    with open(RUTA_JUGADORES, "r", encoding="utf-8") as f:
        maestros = json.load(f)

    for part in registro.get("jugadores", []):
        nom = part["nombre"]
        ape = part["apellido"]
        goles = part.get("goles", 0)
        asist = part.get("asistencias", 0)
        calif = part.get("calificacion", 0)
        ganados = part.get("ganados", 0)
        perdidos = part.get("perdidos", 0)
        empatados = part.get("empatados", 0)

        encontrada = next(
            (j for j in maestros["jugadores"]
             if j["nombre"] == nom and j["apellido"] == ape),
            None
        )
        if not encontrada:
            print(f"⚠️ Jugador no encontrado: {nom} {ape}")
            continue

        encontrada["goles"] += goles
        encontrada["asistencias"] += asist
        encontrada["partidos_jugados"] += 1
        encontrada["ganados"] += ganados
        encontrada["perdidos"] += perdidos
        encontrada["empatados"] += empatados

        pj = encontrada["partidos_jugados"]
        total_prev = encontrada["promedio"] * (pj - 1)
        nueva_media = (total_prev + calif) / pj
        encontrada["promedio"] = round(nueva_media, 2)

    with open(RUTA_JUGADORES, "w", encoding="utf-8") as f:
        json.dump(maestros, f, indent=4, ensure_ascii=False)

    print("✅ jugadores.json actualizado correctamente.")

if __name__ == "__main__":
    actualizar_estadisticas()