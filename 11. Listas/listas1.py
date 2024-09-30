# =======================================
# Algoritmos y programacion basica
# Seccion 30
#
# Erick Marroquin
# 123456
#
# Listas 1
# 23/09/24
# =======================================

lista_vacia = []
lista_llena = [1, 2, 3, 4, 5]

print(len(lista_llena))
print(lista_llena)
print(lista_llena[0], lista_llena[1])

# agregar elementos
lista_llena.append(6)
print(lista_llena)

lista_llena.append(8)
print(lista_llena)

lista_llena.insert(6, 7)
print(lista_llena)

lista_llena.insert(690097, 9)
print(lista_llena)

# eliminar de una lista

lista_llena.remove(2)
print(lista_llena)

del lista_llena[0]
print(lista_llena)

# ordenar una lista
nueva_lista = [9, 7, 5, 2, 1, 3]
nueva_lista.sort()

nueva_lista = [9, 7, 5, 2, 1, 3]
nueva_lista.sort(reverse = True)

print(nueva_lista)

# slices

top_3 = nueva_lista[0:3]

print(top_3)






