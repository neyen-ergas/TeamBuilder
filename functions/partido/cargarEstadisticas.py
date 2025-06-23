import json
import os

RUTA_JSON = os.path.join(os.path.dirname(__file__), "../../src/json/registroPartido.json")

def cargarEstadisticas():
    if not os.path.exists(RUTA_JSON) or os.path.getsize(RUTA_JSON) == 0:
        print("❌ El archivo de registro no existe o está vacío.")
        return

    with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)

    print("\n=== CARGA DE ESTADÍSTICAS ===")
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

    with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)

    print("\n✅ Estadísticas guardadas correctamente.")