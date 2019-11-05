"""
    autor = @erickgjs99
    file = ejercicio33.py

"""

import csv

def lineas(archivo):
    return csv.reader(archivo, delimiter = ";")

with open("data/data-estudiantes.csv") as midata:
    print(list(lineas(midata)))
    
#midata = open("data/data-estudiantes.csv") " en uso de grandes volumenes de datos
#necesarios para cerrar el archivp

#print(list(lineas(midata)))
#midata.close