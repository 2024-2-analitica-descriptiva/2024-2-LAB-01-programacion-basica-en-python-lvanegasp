"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    with open("files/input/data.csv", mode="r", newline="\n") as archivo:
        lineas = archivo.readlines()

    tabla = [linea.split("\t") for linea in lineas]

    diccionario_cantidad_registros = {}

    for registro in tabla:
        letra = registro[0]
        cantidad = int(registro[1])

        if letra in diccionario_cantidad_registros.keys():
            if cantidad > diccionario_cantidad_registros[letra][0]:
                diccionario_cantidad_registros[letra][0] = cantidad
            if cantidad < diccionario_cantidad_registros[letra][1]:
                diccionario_cantidad_registros[letra][1] = cantidad
        else:
            diccionario_cantidad_registros[letra] = [cantidad, cantidad]

    lista_cantidad_registros = [
        (key, int(valor[0]), int(valor[1]))
        for key, valor in diccionario_cantidad_registros.items()
    ]

    return sorted(lista_cantidad_registros)

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
