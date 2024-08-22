# =======================================
# Universidad del Valle de Guatemala
# Algoritmos y programacion basica
# Seccion 30
#
# Erick Marroquin
# 123456
#
# Programa de tablas de multiplicar while
# 19/08/24
# =======================================

print("Ingrese un entero positivo")
numero = int(input())

if numero < 0:
    print("Número inválido")
else:
    n = 1
    while (n <= 10):
        m = n * numero
        
        print(numero, "*", n, "=", m)
        
        n = n + 1

