"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    with open("files/input/data.csv", mode="r", newline="\n") as archivo:
        lineas = archivo.readlines()

    lineas = [linea.rstrip("\n") for linea in lineas]

    tabla = [linea.split("\t") for linea in lineas]

    lista_cantidad_registros = []

    for registro in tabla:
        letra_mayuscula = registro[0]
        cantidas_letras_minusculas = len(registro[3].split(sep=","))
        cantidas_letras_codigos = len(registro[4].split(sep=","))

        lista_cantidad_registros.append(
            (letra_mayuscula, cantidas_letras_minusculas, cantidas_letras_codigos)
        )

    return lista_cantidad_registros

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
