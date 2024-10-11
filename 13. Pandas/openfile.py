import os
import pandas as pd

path = os.getcwd()
print(path)

file = path + "/canciones.csv"

datos = pd.read_csv(file)

#print(datos)

#print(datos.info())

#print(datos.shape)

#print(datos.describe())

#print(datos.autor.value_counts())

print(datos.duracion.mean())
print(datos.duracion.sum())

