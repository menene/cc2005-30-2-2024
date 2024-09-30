# =======================================
# Universidad del Valle de Guatemala
# Algoritmos y programacion basica
# Seccion 30
#
# Erick Marroquin
# 123456
#
# Cadenas 1
# 16/09/24
# =======================================

saludo = "Hola"

print(saludo)

saludo = "Adios"

print(saludo)


cadena1 = "Hola"
cadena2 = "Mundo"
cadena3 = cadena1 + " " + cadena2

print(cadena3)

largo = len(cadena3)
print(largo)

cadena4 = "HoLa MuNdO"

minusculas = cadena4.lower()
mayusculas = cadena4.upper()
titulo = cadena4.title()

print(minusculas, mayusculas, titulo)

cadena5 = "Universidad del Valle de Guatemala"
letras_e = cadena5.count("e")

print(letras_e)

cadena5 = "Universidad del Valle de Guatemala"
letras_e = cadena5.count("el")

print(letras_e)

cadena6 = "Universidad del Valle de Guatemala"
reemplazada = cadena6.replace("a", "e")

print(reemplazada)

r = cadena6.find("V")
print(r, len(cadena6))

print(cadena6[5])
print()
print()

#for i in range(len(cadena6)):
#    print(cadena6[i])
    
    
    
#print(cadena6[-2])

# ESTO DA ERROR
#cadena6[0] = "X"

for letra in cadena6:
    print(letra)






