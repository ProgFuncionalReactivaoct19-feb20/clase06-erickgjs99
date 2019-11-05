"""
    autor = @erickgjs99
    file = ejercicio55.py

"""

import csv


def lineasDiccionario(archivo):
    return csv.DictReader(archivo, delimiter=";")


with open("data/data-estudiantes.csv") as midata:
    dicc = list(lineasDiccionario(midata))
    print(list(map(lambda x: list(x.items()) [0][1], dicc)))


# midata = open("data/data-estudiantes.csv") " en uso de grandes volumenes de datos
# necesarios para cerrar el archivp

# print(list(lineas(midata)))
# midata.close
