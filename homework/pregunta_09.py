"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    with open("files/input/data.csv", mode="r", newline="\n") as archivo:
        lineas = archivo.readlines()

    lineas = [linea.rstrip("\n") for linea in lineas]

    tabla = [linea.split("\t") for linea in lineas]

    diccionario_cantidad_registros = {}

    for registro in tabla:
        codigos = registro[4].split(sep=",")

        for codigo_valor in codigos:
            codigo, _ = codigo_valor.split(":")

            if codigo in diccionario_cantidad_registros.keys():
                diccionario_cantidad_registros[codigo] = (
                    diccionario_cantidad_registros[codigo] + 1
                )
            else:
                diccionario_cantidad_registros[codigo] = 1

    return diccionario_cantidad_registros

    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
