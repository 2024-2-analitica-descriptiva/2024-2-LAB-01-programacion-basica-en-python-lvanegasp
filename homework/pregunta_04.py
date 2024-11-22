"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    with open("files/input/data.csv", mode="r", newline="\n") as archivo:
        lineas = archivo.readlines()

    tabla = [linea.split("\t") for linea in lineas]

    diccionario_cantidad_registros = {}

    for registro in tabla:
        mes = registro[2].split(sep="-")[1]

        if mes in diccionario_cantidad_registros.keys():
            diccionario_cantidad_registros[mes] = (
                diccionario_cantidad_registros[mes] + 1
            )
        else:
            diccionario_cantidad_registros[mes] = 1

    lista_cantidad_registros = [
        (key, valor) for key, valor in diccionario_cantidad_registros.items()
    ]

    return sorted(lista_cantidad_registros)

    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
