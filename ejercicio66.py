"""
    autor = @erickgjs99
    file = ejercicio66.py

"""

import csv

def lineasDiccionario(archivo):
    return csv.DictReader(archivo, delimiter = ";")

with open("data/data-estudiantes.csv") as midata:
    dicc = list(lineasDiccionario(midata))
    #nombre =  list(lambda x: list(x.items()) [0][1].split(" ")[1], dicc))
    #correos = list(map(lambda x: list(x.items()) [1][1].split(".")[0], dicc))
    #print(list(zip(nombre, correos)))
    resultado = map(lambda x : "%s - %s" %(list(x.items())[0][1].split(" ")[1], list(x.items())[1][1].split(".")[0]),dicc)
    print(list(resultado))