import json
import os

RUTA_JSON = os.path.join(os.path.dirname(__file__), "../../src/json/registroPartido.json")
RUTA_JUGADORES = os.path.join(os.path.dirname(__file__), "../../src/json/jugadores.json")


def cargarEstadisticas(goles1, goles2):
    if not os.path.exists(RUTA_JSON) or os.path.getsize(RUTA_JSON) == 0:
        print("❌ El archivo de registro no existe o está vacío.")
        return

    with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)

    if not os.path.exists(RUTA_JUGADORES) or os.path.getsize(RUTA_JUGADORES) == 0:
        print("❌ El archivo de jugadores no existe o está vacío.")
        return

    with open(RUTA_JUGADORES, "r", encoding="utf-8") as archivo:
        jugadores_data = json.load(archivo)

    print(f"Goles del Equipo 1: {goles1}")
    print(f"Goles del Equipo 2: {goles2}")

    if goles1 == goles2:
        equipoganador = 0
        print("🤝 Partido empatado.")
    else:
        equipoganador = 1 if goles1 > goles2 else 2
        print(f"🏆 Ganó el Equipo {equipoganador}")

    goles_equipo_1 = 0
    goles_equipo_2 = 0

    for jugador in data["jugadores"]:
        print(f"\nJugador: {jugador['nombre']} {jugador['apellido']}")

        try:
            jugador["goles"] = int(input("Goles: "))
        except ValueError:
            print("❌ Ingreso inválido. Se asigna 0 por defecto.")
            jugador["goles"] = 0

        try:
            jugador["asistencias"] = int(input("Asistencias: "))
        except ValueError:
            print("❌ Ingreso inválido. Se asigna 0 por defecto.")
            jugador["asistencias"] = 0

        while True:
            try:
                calificacion = int(input("Calificación (1 a 10): "))
                if 1 <= calificacion <= 10:
                    jugador["calificacion"] = calificacion
                    break
                else:
                    print("❌ Número inválido, debe estar entre 1 y 10.")
            except ValueError:
                print("❌ Ingreso inválido. Escribí un número del 1 al 10.")

        equipo_jugador = jugador.get("equipo", 0)
        if equipo_jugador == 1:
            goles_equipo_1 += jugador["goles"]
        elif equipo_jugador == 2:
            goles_equipo_2 += jugador["goles"]

        jugador_principal = next((j for j in jugadores_data["jugadores"]
                                  if j["nombre"] == jugador["nombre"] and j["apellido"] == jugador["apellido"]), None)

        if jugador_principal:
            if "rachas" not in jugador_principal:
                jugador_principal["rachas"] = 0

            if equipoganador != 0 and equipo_jugador == equipoganador:
                jugador_principal["rachas"] += 1
                print(f"✅ {jugador['nombre']} (Equipo {equipo_jugador}) ganó. Racha actual: {jugador_principal['rachas']}")
            elif equipoganador != 0:
                jugador_principal["rachas"] = 0
                print(f"❌ {jugador['nombre']} (Equipo {equipo_jugador}) perdió. Racha reseteada a 0.")
            else:
                print(f"🤝 {jugador['nombre']} empató. Racha se mantiene en {jugador_principal['rachas']}.")

    if goles_equipo_1 != goles1 or goles_equipo_2 != goles2:
        print("\n❌ Error: los goles ingresados por jugador no coinciden con los del resultado del partido.")
        print(f"Goles equipo 1 (ingresados): {goles_equipo_1} | Resultado oficial: {goles1}")
        print(f"Goles equipo 2 (ingresados): {goles_equipo_2} | Resultado oficial: {goles2}")
        return True
        

    with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)

    with open(RUTA_JUGADORES, "w", encoding="utf-8") as archivo:
        json.dump(jugadores_data, archivo, indent=4, ensure_ascii=False)

    print("\n✅ Estadísticas guardadas correctamente.")
    print("✅ Rachas actualizadas en el archivo de jugadores.")

    return False
