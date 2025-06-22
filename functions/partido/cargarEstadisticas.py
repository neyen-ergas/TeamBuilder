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
            jugador["asistencias"] = int(input("Asistencias: "))
            jugador["calificacion"] = int(input("Calificación (1 a 10): "))
        except ValueError:
            print("❌ Ingreso inválido. Se deja en 0.")

    with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)

    print("\n✅ Estadísticas guardadas correctamente.")