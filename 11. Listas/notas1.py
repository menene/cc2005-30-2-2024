# =======================================
# Algoritmos y programacion basica
# Seccion 30
#
# Erick Marroquin
# 123456
#
# Calculadora de notas 1
# 23/09/24
# =======================================

def calcular_promedio(lista_notas):
    suma = 0
    n = len(lista_notas)
    
    for numero in lista_notas:
        suma += numero
        
    return (suma / n)



opcion = ""
notas = []

while opcion != "6":
    print("\n=== CALCULADORA DE NOTAS ===")
    print("1. Agregar nota")
    print("2. Mostrar notas")
    print("3. Calcular promedio")
    print("4. Limpiar lista")
    print("5. Top 3")
    print("6. Salir\n")
    
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        nota = input("Ingrese una nota de 0 a 100: ")
        
        while not nota.isdigit():
            nota = input("Ingrese una nota de 0 a 100: ")
            
        nota = int(nota)
        
        if nota >= 0 and nota <= 100:
            notas.append(nota)
            
            print("Nota agregada exitosamente")
            
        else:
            print("Nota inválida, no se agrega a la lista")
        
    elif opcion == "2":
        print("Notas actuales:")
        print(notas)
    
    elif opcion == "3":
        if len(notas) == 0:
            promedio = 0
        else:
            promedio = calcular_promedio(notas)
            
        print("El promedio es de:", promedio)
        
    elif opcion == "4":
        notas.clear()
        
    elif opcion == "5":
        notas.sort(reverse = True)
        top_3 = notas[0:3]
        
        print(top_3)
        
    elif opcion == "6":
        print("Nos vemos pronto!")
    
    else:
        print("Opción inválida... intentalo nuevamente")
    
    
    
    
    
    
    
    
    
    