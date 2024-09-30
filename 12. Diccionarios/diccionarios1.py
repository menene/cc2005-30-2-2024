# =======================================
# Algoritmos y programacion basica
# Seccion 30
#
# Erick Marroquin
# 123456
#
# Diccionarios 1
# 30/09/24
# =======================================

estudiante = {
    "carnet": "123456",
    "nombre": "Erick Marroquin"
}

vacio = {}

print(estudiante)
print(estudiante["carnet"])
print(estudiante.get("carrera", -1))

estudiante["carnet"] = "12345"

print(estudiante)

estudiante["carne"] = "12345"

print(estudiante)

print(estudiante.keys())
print(estudiante.values())

