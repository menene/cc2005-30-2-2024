# =======================================
# Universidad del Valle de Guatemala
# Algoritmos y programacion basica
# Seccion 30
#
# Erick Marroquin
# 123456
#
# Funciones
# 19/08/24
# =======================================

def volumen_viga(l, h, a):
    return l * h * a

def volumen_columna(r, h):
    area = (3.14 * r ** 2) * h
    
    return area

def volumen_cubo(l):
    return l ** 3

print(volumen_cubo(1))
print(volumen_cubo(2))
print(volumen_cubo(3))
print(volumen_cubo(4))
print(volumen_cubo(5))
print(volumen_cubo(6))
print(volumen_cubo(7))
print(volumen_cubo(8))
print(volumen_cubo(9))
print(volumen_cubo(10))
print(volumen_cubo(11))


opcion = ""
while opcion != "4":
    print("")
    print("")
    print("=== UVG Construction ===")    
    print("1. Volúmen viga")
    print("2. Volúmen columna")
    print("3. Volúmen cubo")
    print("4. Salir")
    
    opcion = input("Ingrese una acción: ")
    
    if opcion == "1":
        largo = int(input("Ingrese el largo de la viga: "))
        alto = int(input("Ingrese el alto de la viga: "))
        ancho = int(input("Ingrese el ancho de la viga: "))

        volumen = volumen_viga(largo, alto, ancho)
        
        print("El volúmen es:", volumen)
        
    elif opcion == "2":
        radio = int(input("Ingrese el radio de la columna: "))
        alto = int(input("Ingrese el alto de la columna: "))
        
        volumen = volumen_columna(radio, alto)
        
        print("El volúmen es:", volumen)
        
    elif opcion == "3":
        largo = int(input("Ingrese el largo del cubo: "))
        
        volumen = volumen_cubo(largo)
        
        print("El volúmen es:", volumen)
        
    elif opcion == "4":
        print("Nos vemos pronto")
        
    else:
        print("Opción incorrecta... intentalo nuevamente!") 







    
            
            