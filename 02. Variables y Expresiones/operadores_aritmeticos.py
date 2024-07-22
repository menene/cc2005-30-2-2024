# =======================================
# Universidad del Valle de Guatemala
# Algoritmos y programacion basica
# Seccion 30
#
# Erick Marroquin
# 123456
#
# Operadores aritmeticos
# 19/07/24
# =======================================

num1 = 10
num2 = 2

# suma de 2 valores numericos
suma = num1 + num2
print("Suma: ", suma)

# resta de 2 valores numericos
resta = num1 - num2
print("Resta: ", resta)

# multiplicacion
multi = num1 * num2
print("Multi: ", multi)

# division
divi = num1 / num2
print("Divi: ", divi)

# exponente
expo = num1**2
print("Cuadrado: ", expo)

expo2 = num1**num2
print("Cuadrado2 : ", expo2)

raiz = num1**0.5
print("Raiz : ", raiz)

# operaciones con cadenas
num3 = "3"
num4 = "4"

# concatenar
resultado = num3 + num4
print(resultado)

cadena = "120"
resultado = cadena * num1
print(resultado)

nombre = input("Ingrese su nombre: ")
print("Hola", nombre)

num5 = input("ingrese un numero de 1 a 10: ")
print(num5)

tipo = type(num5)
print(tipo)

precio = input("Ingrese el precio: ")
descuento = input("Ingrese el descuento: ")

precio = int(precio)
descuento = float(descuento)
print(type(precio))

total = precio - descuento
print("El total es: ", total)

x = 10
y = 20

resultado = x + y
print(resultado)

x = True
y = False
resultado = x + y
print(resultado)

x = "Hola"
y = "Mundo"
resultado = x + y
print(resultado)

x = 10
y = 20
z = 30
resultado = ((x + y) - (y * 3) + (z / 2)) + 8
print(resultado)
