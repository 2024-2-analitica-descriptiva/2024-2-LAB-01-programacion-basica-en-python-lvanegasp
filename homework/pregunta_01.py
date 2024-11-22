"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    with open("files/input/data.csv", mode="r", newline="\n") as archivo:
        lineas = archivo.readlines()

    tabla = [linea.split("\t") for linea in lineas]

    suma = 0
    for registro in tabla:
        suma = int(registro[1]) + suma

    return suma
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
