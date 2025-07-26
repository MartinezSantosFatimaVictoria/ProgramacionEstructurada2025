"""
Uso de diccionarios en listas
"""

#lista
frutas=["Manzana","Platano","Pera"]

#Diccionario

persona={"nombre":"Ana", "Edad": 17}




estudiantes = [
    {"nombre": "Ana", "edad": 17, "calificacion": 8.5},
    {"nombre": "Luis", "edad": 18, "calificacion": 9.0},
    {"nombre": "Sofía", "edad": 17, "calificacion": 7.8},
    {"nombre": "Carlos", "edad": 19, "calificacion": 8.9}
]


print("Listado de estudiantes:")
for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Calificación: {estudiante['calificacion']}")


suma = 0
for estudiante in estudiantes:
    suma += estudiante["calificacion"]

promedio = suma / len(estudiantes)
print(f"\nPromedio de calificaciones: {promedio:.2f}")
