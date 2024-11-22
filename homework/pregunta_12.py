"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    with open("files/input/data.csv", mode="r", newline="\n") as archivo:
        lineas = archivo.readlines()

    lineas = [linea.rstrip("\n") for linea in lineas]

    tabla = [linea.split("\t") for linea in lineas]

    diccionario_cantidad_registros = {}

    for registro in tabla:
        letra_mayuscula = registro[0]
        codigos = registro[4].split(sep=",")

        for codigo in codigos:
            valor_codigo = int(codigo.split(sep=":")[1])
            if letra_mayuscula in diccionario_cantidad_registros.keys():
                diccionario_cantidad_registros[letra_mayuscula] = (
                    diccionario_cantidad_registros[letra_mayuscula] + valor_codigo
                )
            else:
                diccionario_cantidad_registros[letra_mayuscula] = valor_codigo

    return diccionario_cantidad_registros

    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
