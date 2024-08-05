# =======================================
# Universidad del Valle de Guatemala
# Algoritmos y programacion basica
# Seccion 30
#
# Erick Marroquin
# 123456
#
# Sistema que convierte notas a letras
# 02/08/24
# =======================================

opcion = ""

while opcion != "2":
    print("=== UVG Letras ===")
    print("1. Calcular letra")
    print("2. Salir")
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        nota = int(input("Ingrese la nota del estudiante: "))
        faltas = int(input("¿Cuantas veces ha faltado el estudiante? "))
        tareas = int(input("¿Cual fue su porcentaje de entrega de tareas?"))
        
        bono = 0
        penalizacion = 0
        
        if faltas > 3:
            penalizacion = penalizacion + 5
             
        if tareas == 100 and faltas == 0:
            bono = bono + 5
            
        print("Bonos:", bono)
        print("Penalizaciones:", penalizacion)
        
        nota_final = nota + bono - penalizacion
        
        print("Nota final:", nota_final)
        
        if nota_final > 100:
            nota_final = 100
            
        if nota_final < 0:
            nota_final = 0
            
        print("Nota final ajustada:", nota_final)
        
        letra = ""
        
        if nota_final >= 90:
            letra = "A"
        elif nota_final >= 80 and nota_final < 90:
            letra = "B"
        elif nota_final >= 70 and nota_final < 80:
            letra = "C"
        elif nota_final >= 60 and nota_final < 70:
            letra = "D"
        else:
            letra = "F"
            
        print("Letra:", letra)
        
    elif opcion == "2":
        print("Hasta luego...")
        
    else:
        print("Opción incorrecta... intentalo nuevamente 😰")
    









