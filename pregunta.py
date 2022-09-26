"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import numpy as np
import re

def ingest_data():

    data=open('clusters_report.txt', mode='r')
    lineas=data.readlines()
    lista=[]
    cluster=[None, None, None, '']

    for linea in lineas:
        if re.match('^ +[0-9]+ +', linea):
            numero, cantidad, porcentaje, *palabras = linea.split()
            cluster[0] = int(numero)
            cluster[1] = int(cantidad)
            cluster[2] = float(porcentaje.replace(',','.'))

            palabras.remove('%')
            palabras = ' '.join(palabras)
            cluster[3] += palabras
        elif re.match('^\n', linea) or re.match('^ +$', linea):
            cluster[3] = cluster[3].replace('.', '')
            lista.append(cluster)
            cluster = [None, None, None, ''] 
        elif re.match('^ +[a-z]', linea):
            palabras = linea.split()
            palabras = ' '.join(palabras)
            cluster[3] += ' ' + palabras
    lista.pop(0)

    clusters=pd.DataFrame(lista, columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    return clusters

print(ingest_data())
