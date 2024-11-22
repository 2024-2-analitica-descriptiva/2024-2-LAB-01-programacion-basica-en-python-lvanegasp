"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    with open("files/input/data.csv", mode="r", newline="\n") as archivo:
        lineas = archivo.readlines()

    lineas = [linea.rstrip("\n") for linea in lineas]

    tabla = [linea.split("\t") for linea in lineas]

    diccionario_cantidad_registros: dict[int, list[int]] = {}

    for registro in tabla:
        cantidad = int(registro[1])
        letra = registro[0]

        if cantidad in diccionario_cantidad_registros.keys():
            if letra not in diccionario_cantidad_registros[cantidad]:
                diccionario_cantidad_registros[cantidad].append(letra)
        else:
            diccionario_cantidad_registros[cantidad] = [letra]

        diccionario_cantidad_registros[cantidad] = sorted(
            diccionario_cantidad_registros[cantidad]
        )

    lista_cantidad_registros = [
        (key, valor) for key, valor in diccionario_cantidad_registros.items()
    ]

    return sorted(lista_cantidad_registros)

    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
