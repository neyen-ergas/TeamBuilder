import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from functions.armado import seleccionJugadoresEquipo, creadorEquipos
from functions.archivos import manejoJson
from functions.archivos.exportarEstadisticas import exportarStats
from functions.jugadores import jugadores as j
from functions.ratings import top5
from functions.partido.cargarEstadisticas import cargarEstadisticas
from functions.partido.guardarRegistros import guardarRegistro
from functions.partido.actualizarEstadisticas import actualizar_estadisticas


def menuCrearPartido():
    print()
    print()
    print("¿Que acción quiere realizar?") 
    print("1. Crear Partido")
    print("2. Volver al menú principal")

    while True:
        try:
            n = int(input("Ingresar acción: "))
            if n == 1 or n == 2:
                break
            else:
                print("Ingresar una acción válida.")
        except ValueError:
            print("❌ Ingresá un número válido.")

    if n == 1:
        crearPartido()
    elif n == 2:
        main()


def crearPartido():
    if os.path.exists("registroPartido.json"):
        os.remove("registroPartido.json")

    print("\n=== CREAR PARTIDO ===")
    print("¿Cuántos jugadores por equipo? (5 a 11)")
    
    while True:
        try:
            num = int(input("Ingresar cantidad: "))
            if 5 <= num <= 11:
                break
            else:
                print("❌ Debe estar entre 5 y 11.")
        except ValueError:
            print("❌ Ingresá un número válido.")

    total_jugadores = len(manejoJson.cargar_jugadores())

    while total_jugadores < num * 2:
        print(f"⚠️ No hay suficientes jugadores para 2 equipos de {num}. (Total disponibles: {total_jugadores})")
        try:
            num = int(input("Elegí un número menor de jugadores por equipo: "))
            if num < 5 or num > 11:
                print("❌ Número fuera de rango (5-11).")
        except ValueError:
            print("❌ Ingresá un número válido.")

    jugadoresPartido = seleccionJugadoresEquipo.agregar_jugador_a_partido(num * 2)
    equipo1, equipo2, puntaje1, puntaje2 = creadorEquipos.creadorEquipos(jugadoresPartido)

    print("\n" + "=" * 40)
    print(f"{'Equipos de Fútbol':^40}")
    print("=" * 40)
    print(f"{'Equipo 1':<20} {'Equipo 2':<20}")
    print("-" * 40)

    for j1, j2 in zip(equipo1, equipo2):
        print(f"{j1:<20} {j2:<20}")

    print("-" * 40)
    print(f"{'Promedio Equipo 1:':<20} {puntaje1:<20.1f}")
    print(f"{'Promedio Equipo 2:':<20} {puntaje2:<20.1f}")
    print("=" * 40)

    guardarRegistro(jugadoresPartido, equipo1, equipo2)

    print("")
    while True:
        try:
            n = int(input("Presione 1 para finalizar el partido: "))
            if n == 1:
                break
            else:
                print("❌ Ingresar '1' para finalizar.")
        except ValueError:
            print("❌ Ingresá un número.")

    print("\nIngrese el resultado final del partido")
    try:
        goles1 = int(input("Goles del Equipo 1: "))
        goles2 = int(input("Goles del Equipo 2: "))
    except ValueError:
        print("❌ Entrada inválida. Se asignan 0 por defecto.")
        goles1, goles2 = 0, 0

    RUTA_REGISTRO = os.path.join(os.path.dirname(__file__), "../src/json/registroPartido.json")

    with open(RUTA_REGISTRO, "r", encoding="utf-8") as f:
        data = json.load(f)

    if goles1 == goles2:
        print("🤝 Empate: se registra empate para todos los jugadores.")
        for jugador in data["jugadores"]:
            jugador["empatados"] += 1
    else:
        equipo_ganador = equipo1 if goles1 > goles2 else equipo2
        equipo_perdedor = equipo2 if goles1 > goles2 else equipo1

        for jugador in data["jugadores"]:
            nombre_completo = f"{jugador['nombre']} {jugador['apellido']}"
            if nombre_completo in equipo_ganador:
                jugador["ganados"] += 1
            elif nombre_completo in equipo_perdedor:
                jugador["perdidos"] += 1

        print("✅ Resultado registrado correctamente.")

    with open(RUTA_REGISTRO, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    error = True
    while error:
        error = cargarEstadisticas(goles1, goles2)
        if error:
            print("⚠️ Intente nuevamente ⚠️")

    actualizar_estadisticas()
    print("✅ Estadísticas actualizadas correctamente.")
    print("✅ Registro guardado correctamente.")

    main()


def menuJugadores():
    print()
    print()
    print("¿Que acción quiere realizar?") 
    print("1. Mostrar lista de jugadores")
    print("2. Alta de jugador")
    print("3. Editar jugador")
    print("4. Baja de jugador")
    print("5. Volver al menú principal")

    while True:
        try:
            n = int(input("Ingresar acción: "))
            if 1 <= n <= 5:
                break
            else:
                print("Ingresar una acción válida.")
        except ValueError:
            print("❌ Ingresá un número válido.")

    if n == 1:
        j.mostrar_lista()
        menuJugadores()
    elif n == 2:
        j.altaJugador()
        menuJugadores()
    elif n == 3:
        j.editarJugador()
        menuJugadores()
    elif n == 4:
        j.bajaJugador()
        menuJugadores()
    elif n == 5:
        main()


def main():
    print()
    print()
    print()
    print("------Bienvenido a la aplicación de TeamBuilder------")
    print("¿Que acción quiere realizar?")
    print("1. Crear Partido")
    print("2. Administración de jugadores")
    print("3. Estadísticas")                   
    print("4. Salir")

    while True:
        try:
            n = int(input("Ingresar acción: "))
            if 1 <= n <= 4:
                break
            else:
                print("Ingresar una acción válida.")
        except ValueError:
            print("❌ Ingresá un número válido.")

    if n == 1:
        menuCrearPartido()
    elif n == 2:
        menuJugadores()
    elif n == 3:            
        menuEstadisticas()
    else:
        print("¡Hasta pronto!")


def menuEstadisticas():
    print()
    print()
    print("¿De qué quiere ver estadísticas?")
    print("1. Top 5 goleadores")
    print("2. Top 5 asistidores") 
    print("3. Top 5 más activos")
    print("4. Top 5 mas ganadores")
    print("5. Top 5 mas perdedores")
    print("6. Descargar estadísticas")
    print("7. Volver atras")

    while True:
        try:
            n = int(input("Ingresar acción: "))
            if 1 <= n <= 7:
                break
            else:
                print("Ingresar una acción válida.")
        except ValueError:
            print("❌ Ingresá un número válido.")

    if n == 1:
        top5.goleadores()
    elif n == 2:
        top5.asistidores()
    elif n == 3:
        top5.activos()
    elif n == 4:
        top5.ganadores()
    elif n == 5:
        top5.perdedores()
    elif n == 6:
        exportarStats()
        print("El archivo 'estadisticas.csv' ya está ubicado en la carpeta 'export'")
    elif n == 7:
        main()
        return

    while True:
        try:
            n2 = int(input("Escriba '1' para volver atras: "))
            if n2 == 1:
                menuEstadisticas()
                break
            else:
                print("Acción inválida. Intente nuevamente:")
        except ValueError:
            print("❌ Ingresá un número válido.")


main()
