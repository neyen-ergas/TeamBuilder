import json
import os

RUTA_JSON = os.path.join(os.path.dirname(__file__), "../../src/json/registroPartido.json")
RUTA_JUGADORES = os.path.join(os.path.dirname(__file__), "../../src/json/jugadores.json")

def cargarEstadisticas():
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

    print("\n=== CARGA DE ESTADÍSTICAS ===")

    equipoganador = input("¿Qué equipo ganó el partido? (1 o 2): ")

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


        jugador_principal = None
        for j in jugadores_data["jugadores"]:
            if j["nombre"] == jugador["nombre"] and j["apellido"] == jugador["apellido"]:
                jugador_principal = j
                break

        if jugador_principal:

            if "rachas" not in jugador_principal:
                jugador_principal["rachas"] = 0


            equipo_jugador = jugador.get("equipo", 0)  
            

            try:
                equipo_ganador_num = int(equipoganador)
            except ValueError:

                equipo_ganador_num = 1 if equipoganador.lower() in ["1", "equipo 1", "equipo1"] else 2
            
            if equipo_jugador == equipo_ganador_num:

                jugador_principal["rachas"] += 1
                print(f"✅ {jugador['nombre']} (Equipo {equipo_jugador}) ganó. Racha actual: {jugador_principal['rachas']}")
            else:

                jugador_principal["rachas"] = 0
                print(f"❌ {jugador['nombre']} (Equipo {equipo_jugador}) perdió. Racha reseteada a 0.")


    with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)


    with open(RUTA_JUGADORES, "w", encoding="utf-8") as archivo:
        json.dump(jugadores_data, archivo, indent=4, ensure_ascii=False)

    print("\n✅ Estadísticas guardadas correctamente.")
    print("✅ Rachas actualizadas en el archivo de jugadores.")