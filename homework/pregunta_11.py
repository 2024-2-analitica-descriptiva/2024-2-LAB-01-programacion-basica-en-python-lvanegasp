"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    with open("files/input/data.csv", mode="r", newline="\n") as archivo:
        lineas = archivo.readlines()

    lineas = [linea.rstrip("\n") for linea in lineas]

    tabla = [linea.split("\t") for linea in lineas]

    diccionario_cantidad_registros = {}

    for registro in tabla:
        cantidad = int(registro[1])
        letras_minuculas = registro[3].split(sep=",")

        for letra_minucula in letras_minuculas:
            if letra_minucula in diccionario_cantidad_registros.keys():
                diccionario_cantidad_registros[letra_minucula] = (
                    diccionario_cantidad_registros[letra_minucula] + cantidad
                )
            else:
                diccionario_cantidad_registros[letra_minucula] = cantidad

    lista_cantidad_registros = {
        (key, valor) for key, valor in diccionario_cantidad_registros.items()
    }

    return diccionario_cantidad_registros

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
