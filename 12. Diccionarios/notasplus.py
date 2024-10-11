import os
import pandas as pd

path = os.getcwd()
file = path + "/estudiantes.csv"

#estudiantes = []
estudiantes = pd.read_csv(file)

opcion = ""

while opcion != "6":
    print("")
    print("=== NOTAS ++ ===")
    print("1. Agregar estudiante")
    print("2. Agregar notas")
    print("3. Reporte")
    print("4. Promedio general")
    print("5. Mostrar estudiante")
    print("6. Salir")
    print("")
    
    opcion = input("Seleccione una opción del menú anterior: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        carnet = input("Ingrese el carnet del estudiante: ")
        
        est = {
            "nombre": nombre,
            "carnet": carnet,
            "tarea1": 0,
            "tarea2": 0,
            "tarea3": 0
        }
        
        estudiantes.append(est)
        
    elif opcion == "2":
        carnet = input("Ingrese el número de carnet del estudiante: ")
        
        for estudiante in estudiantes:
            if estudiante["carnet"] == carnet:
                
                tarea = input("Ingrese la tarea para agregar la nota: ")
                nota = int(input("Ingrese la nota de la tarea: "))
                
                estudiante[tarea] = nota
        
        
    elif opcion == "3":
        #df = pd.DataFrame(estudiantes)
        
        print(estudiantes)
        print(estudiantes.describe())
        
    elif opcion == "4":
        print("general")
        
    elif opcion == "5":
        for estudiante in estudiantes:
            print(estudiante)
        
    elif opcion == "6":
        print("Nos vemos!")
        
    else:
        print("Opción incorrecta...")
    
    
    
    
    
    
    
    