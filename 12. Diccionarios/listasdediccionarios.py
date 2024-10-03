

actividad1 = {
    "id": 1,
    "nombre": "Partido de fut",
    "fecha": "03/10/24"
}

actividad2 = {
    "id": 2,
    "nombre": "Partido de bolley ball",
    "fecha": "04/10/24"
}

actividad3 = {
    "id": 3,
    "nombre": "Partido de Paddle",
    "fecha": "05/10/24"
}


# print(actividad1["nombre"])

actividades = []
actividades.append(actividad1)
actividades.append(actividad2)
actividades.append(actividad3)

# print(actividades)


# for i in range(len(actividades)):
#     print(actividades[i]["nombre"])
  

# for actividad in actividades:
#     print(actividad["nombre"])
    
    
for actividad in actividades:
    if actividad["id"] == 3:
        actividad["fecha"] = "10/10/24"
        
        
print(actividades)
    
    
    
    