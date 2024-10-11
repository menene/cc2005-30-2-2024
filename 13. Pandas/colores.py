import pandas as pd

colores = pd.Series(
    ["rojo", "morado", "azul", "verde", "amarillo"],
    index=[1, 2, 3, 5,8]
)

#print(colores)

print(colores.loc[1])
print(colores.iloc[1])