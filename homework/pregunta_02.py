"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    with open("files/input/data.csv", mode="r", newline="\n") as archivo:
        lineas = archivo.readlines()

    tabla = [linea.split("\t") for linea in lineas]

    diccionario_cantidad_registros = {}

    for registro in tabla:
        if registro[0] in diccionario_cantidad_registros.keys():
            diccionario_cantidad_registros[registro[0]] = (
                diccionario_cantidad_registros[registro[0]] + 1
            )
        else:
            diccionario_cantidad_registros[registro[0]] = 1

    lista_cantidad_registros = [
        (key, valor) for key, valor in diccionario_cantidad_registros.items()
    ]

    return sorted(lista_cantidad_registros)

    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
