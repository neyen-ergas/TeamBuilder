import json
import os

RUTA_JSON = os.path.join(os.path.dirname(__file__), "../../src/json/jugadores.json")

def cargar_jugadores():
    """
    Carga la lista de jugadores desde un archivo JSON.

    Returns:
        list: Lista de jugadores, donde cada jugador es un diccionario con sus datos.

    Notas:
        - El archivo debe contener una clave "jugadores" que almacene la lista.
        - Si el archivo está vacío o mal formado, puede lanzar una excepción.
    """
    with open(RUTA_JSON, "rt", encoding="utf-8") as file:
        data = json.load(file)
        return data["jugadores"]

def guardar_jugadores(jugadores):
    """
    Guarda una lista de jugadores en el archivo JSON.

    Args:
        jugadores (list): Lista de diccionarios que representan jugadores.

    Notas:
        - Sobrescribe completamente el contenido anterior del archivo.
        - Los datos se guardan con indentación para mayor legibilidad.
        - `ensure_ascii=False` permite mantener caracteres especiales como tildes o eñes.
    """
    with open(RUTA_JSON, "wt", encoding="utf-8") as file:
        json.dump({"jugadores": jugadores}, file, indent=2, ensure_ascii=False)

def agregar_jugador(nuevo_jugador):
    """
    Agrega un nuevo jugador a la base de datos.

    Args:
        nuevo_jugador (dict): Diccionario con los datos del nuevo jugador.

    Notas:
        - El jugador se agrega al final de la lista actual.
        - No se valida si el jugador ya existe; eso se debe hacer antes de llamar a esta función.
    """
    jugadores = cargar_jugadores()
    jugadores.append(nuevo_jugador)
    guardar_jugadores(jugadores)

def borrar_jugador(nombre, apellido):
    """
    Elimina un jugador de la base de datos según su nombre y apellido.

    Args:
        nombre (str): Nombre del jugador.
        apellido (str): Apellido del jugador.

    Notas:
        - Si hay más de un jugador con el mismo nombre y apellido, se eliminan todos.
        - La comparación es sensible a mayúsculas y minúsculas.
    """
    jugadores = cargar_jugadores()
    jugadores = [j for j in jugadores if not (j["nombre"] == nombre and j["apellido"] == apellido)]
    guardar_jugadores(jugadores)

def modificar_jugador(nombre, apellido, nuevos_datos):
    """
    Modifica los datos de un jugador existente.

    Args:
        nombre (str): Nombre actual del jugador.
        apellido (str): Apellido actual del jugador.
        nuevos_datos (dict): Diccionario con los campos a actualizar.

    Notas:
        - Solo modifica el primer jugador que coincida con el nombre y apellido exactos.
        - Si el jugador no se encuentra, no se realiza ninguna modificación.
        - Los campos no especificados en `nuevos_datos` permanecen sin cambios.
    """
    jugadores = cargar_jugadores()
    for j in jugadores:
        if j["nombre"] == nombre and j["apellido"] == apellido:
            j.update(nuevos_datos)
            break
    guardar_jugadores(jugadores)
