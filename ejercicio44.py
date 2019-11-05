"""
    autor = @erickgjs99
    file = ejercicio44.py

"""

import csv

def lineas(archivo):
    return csv.reader(archivo, delimiter = ";")

with open("data/data-estudiantes.csv") as midata:
    lista = (list(lineas(midata)))
    print(list(map(lambda x: x[1], filter(lambda x: x[1] != "email", lista))))
    
#midata = open("data/data-estudiantes.csv") " en uso de grandes volumenes de datos
#necesarios para cerrar el archivp

#print(list(lineas(midata)))
#midata.close