# =======================================
# Universidad del Valle de Guatemala
# Algoritmos y programacion basica
# Seccion 30
#
# Erick Marroquin
# 123456
#
# Operadores logicos
# 22/07/24
# =======================================


x = 2
y = 3

r = ((x + 5) < (y + 1)) and (x != 8)
print(r)


x = 28
y = 15
z = 10

r = ((x <= 10) or (x == 6)) and ((y <= 1) and (y > 0)) or ((z < 100) and (z > 60))
print(r)

dia = 1
hora = 10
clase_progra = ((dia == 1) and ((hora >= 8.4) and (hora <= 10.15))) or ((dia == 5) and ((hora >= 8.4) and (hora <= 10.15)))

print(clase_progra)

#if clase_progra:
#    print("Vamos a clase")
    
if clase_progra:
    print("Vamos a clase")
    
    if dia == 1:
        print("Feliz inicio de semana")
    else:
        print("Feliz fin de semana")
else:
    print("Descansemos")
