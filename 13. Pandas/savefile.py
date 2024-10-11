import os
import pandas as pd

path = os.getcwd()
print(path)

canciones = [
    {"titulo": "Cancion 1", "autor": "Autor 1", "duracion": 3.5},
    {"titulo": "Cancion 2", "autor": "Autor 1", "duracion": 2.5},
    {"titulo": "Cancion 3", "autor": "Autor 3", "duracion": 4.2},
    {"titulo": "Cancion 4", "autor": "Autor 1", "duracion": 1.9},
]

# print(canciones)

df = pd.DataFrame(canciones)
print(df)

file = path + "/canciones.csv"
print(file)

df.to_csv(file, index=False)
print("Archivo escrito extiosamente")




