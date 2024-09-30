

estudiantes = []

opcion = ""

while opcion != "6":
    print("")
    print("=== NOTAS ++ ===")
    print("1. Agregar estudiante")
    print("2. Agregar notas")
    print("3. Mostrar promedio")
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
            "notas": []
        }
        
        estudiantes.append(est)
        
    elif opcion == "2":
        carnet = input("Ingrese el número de carnet del estudiante: ")
        
        for estudiante in estudiantes:
            
            if estudiante["carnet"] == carnet:
                nota = int(input("Ingrese la nota del estudiante: "))
                
                estudiante["notas"].append(nota)
        
    elif opcion == "3":
        print("promedio")
        
    elif opcion == "4":
        print("general")
        
    elif opcion == "5":
        for estudiante in estudiantes:
            print(estudiante)
        
    elif opcion == "6":
        print("Nos vemos!")
        
    else:
        print("Opción incorrecta...")
    
    
    
    
    
    
    
    