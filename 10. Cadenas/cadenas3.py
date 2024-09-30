# Algoritmos y programacion basica
# Seccion 30
#
# Erick Marroquin
# 123456
#
# Cadenas 3
# 20/09/24
# =======================================

import random

numero = random.randint(1, 10)
print(numero)

guess = input("Ingese un numero de 1 a 10: ")
intentos = 1
while not guess.isdigit():
    guess = input("Te he dicho " + str(intentos) + " veces que es un número 1 a 10 🤦🏻‍♂️: ")
    
    intentos += 1


guess = int(guess)

if guess > 10:
    print("El numero no puede ser mayor que 10")
elif guess < 1:
    print("El numero no puede ser menor que 1")
else:
    if guess == numero:
        print("Felicidades! has ganado")
    else:
        print("Looser")
