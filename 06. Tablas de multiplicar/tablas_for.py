# =======================================
# Universidad del Valle de Guatemala
# Algoritmos y programacion basica
# Seccion 30
#
# Erick Marroquin
# 123456
#
# Programa de tablas de multiplicar
# 19/08/24
# =======================================

print("Ingrese un número entero positivo")

numero = int(input())

if numero < 0:
    print("Número inválido")
else:
    for n in range(1, 11):
        m = n * numero
        
        print(numero, "*", n, "=", m)





