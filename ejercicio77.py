"""
    autor = @erickgjs99
    file = ejercicio55.py

"""

import csv


def lineasDiccionario(archivo):
    return csv.DictReader(archivo, delimiter = "\t")


with open("data/trabajadores.csv") as midata:
    dicc = list(lineasDiccionario(midata))
    condition = filter(lambda x: len(list(x.items())[2][1]) >=10, dicc)
    print(list(sorted(condition, key = lambda x: list(x.items()) [1][1].split("-")[2])))
