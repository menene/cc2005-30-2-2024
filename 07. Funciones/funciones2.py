# =======================================
# Universidad del Valle de Guatemala
# Algoritmos y programacion basica
# Seccion 30
#
# Erick Marroquin
# 123456
#
# Funciones 2
# 23/08/24
# =======================================

import math

def hipotenusa(cateto_a, cateto_b):
    a2 = cateto_a * cateto_a
    b2 = cateto_b * cateto_b
    
    c = math.sqrt(a2 + b2)

    return c

def cateto(hipotenusa, cateto_b):
    c2 = hipotenusa ** 2
    b2 = cateto_b ** 2
    
    a = math.sqrt(c2 - b2)
    
    return a

# --------------------------------------------

opcion = ""
hipotenusas = 0
catetos = 0

while opcion != "2":
    print("\nOpciones disponibles:")
    print("1. Calcular")
    print("2. Salir")
    
    opcion = input("Ingrese la opción deseada: ")
    
    if opcion == "1":
        print("\n Acciones disponibles:")
        print("1. Hipotenusa desconocida")
        print("2. Hipotenusa conocida")
        
        accion = input("Ingrese una accion: ")
        
        if accion == "1":
            a = int(input("Ingrese el valor del cateto a: "))
            b = int(input("Ingrese el valor del cateto b: "))
            
            r = hipotenusa(a, b)
            
            print("El resultado es:", r)
            
            hipotenusas += 1
        
        elif accion == "2":
            c = int(input("Ingrese el valor de la hipotenusa: "))
            b = int(input("Ingrese el valor del cateto b: "))
            
            r = cateto(c, b)
            
            print("El resultado es:", r)
            
            catetos += 1
            
        else:
            print("Acción inválida")
        
    elif opcion == "2":
        print("Gracias por participar...")
        print("Consultaste hipotenusa conocida un total de:", hipotenusas, "veces")
        print("Consultaste hipotenusa desconocida un total de:", catetos, "veces")
        
    else:
        print("Opción inválida 🙄 Intentalo nuevamente")











