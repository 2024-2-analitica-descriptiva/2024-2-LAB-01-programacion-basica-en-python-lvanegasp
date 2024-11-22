"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    with open("files/input/data.csv", mode="r", newline="\n") as archivo:
        lineas = archivo.readlines()

    lineas = [linea.rstrip("\n") for linea in lineas]

    tabla = [linea.split("\t") for linea in lineas]

    diccionario_cantidad_registros = {}

    for registro in tabla:
        codigos = registro[4].split(sep=",")

        for codigo_valor in codigos:
            codigo, valor = codigo_valor.split(":")
            valor = int(valor)

            if codigo in diccionario_cantidad_registros.keys():
                if valor < diccionario_cantidad_registros[codigo][0]:
                    diccionario_cantidad_registros[codigo][0] = valor
                if valor > diccionario_cantidad_registros[codigo][1]:
                    diccionario_cantidad_registros[codigo][1] = valor
            else:
                diccionario_cantidad_registros[codigo] = [valor, valor]

    lista_cantidad_registros = [
        (key, int(valor[0]), int(valor[1]))
        for key, valor in diccionario_cantidad_registros.items()
    ]

    return sorted(lista_cantidad_registros)

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
