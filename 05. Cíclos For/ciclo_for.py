# =======================================
# Universidad del Valle de Guatemala
# Algoritmos y programacion basica
# Seccion 30
#
# Erick Marroquin
# 123456
#
# Ciclos For
# 12/08/24
# =======================================

# Forma 1 de funcion range
for num in range(6):
    print(num)

# Forma 2 de funcion range
for num in range(10, 15):
    print(num)

# Forma 3 de funcion range
for num in range(1, 10, 2):
    print(num)

for num in range(1000, 2000, 100):
    print(num)


cantidad_estudiantes = int(input("¿Cuántos estudiantes tienes? "))
suma = 0

for cualquier_cosa in range(cantidad_estudiantes):
    print("Ingrese la nota del estudiante", (cualquier_cosa + 1), ":")
    nota = int(input(""))

    # suma = suma + nota
    suma += nota

# el promedio va afuera!!! hasta que ya tengo la suma
if cantidad_estudiantes <= 0:
    print("El promedio es: 0")
else:
    promedio = suma / cantidad_estudiantes
    print("El promedio es:", promedio)
