# Promedio, busqueda de elementos en un arreglo.
# Diseña un programa en Python que:
# 1. Permita declarar y crear un arreglo con calificaciones de un grupo de estudiantes (valores enteros del 0 al 100)
# 2. Calcule el promedio de las calificaciones de cada alumno y de las calificaciones almacenadas en el arreglo.
# 3. Que permita buscar si una calificación especifica (ingresada por el usuario) se encuentra en el arreglo.
# 4. Que muestre los resultados de forma clara en la pantalla.

# pedir numero de alumnos y calificaciones que hay que ingresar por el numero de materias.
# ver en pantalla el promedio del grupo, y despues poder hacer una busqueda por calificacion.

numAlumnos = int(input("Ingresar el número de alumnos:"))
numCalificaciones = int(input("Ingresa el número de materias a calificar:"))

matriz = [[0 for _ in range(numCalificaciones + 1)] for _ in range(numAlumnos + 1)]

matriz[0][0] = "Alumnos"

for j in range(1, numAlumnos + 1):
    alumnos = input(f"Inserta el nombre del alumno {j}:")
    matriz[j][0] = alumnos

for i in range(1, numCalificaciones + 1):
    calificaciones = input(f"Insertar el nombre de la materia {i}:")
    matriz[0][i] = calificaciones

for i in range (1, numAlumnos + 1):
    for k in range (1, numCalificaciones + 1):
        datoCal = int(input(f"Ingresa la calificación para el alumno {matriz[i][0]} en la materia {matriz[0][k]}:"))
        if datoCal > 100:
            print("El máximo de calificación es 100. Ingresando 100 como calificación.")
            datoCal = 100
        elif datoCal < 0:
            print("Calificación no puede ser menor a 0, registrando calificación como 0.")
            datoCal = 0
        else:
            matriz[i][k] = datoCal

for recorrer in matriz:
    print(recorrer)

sumaGeneral = 0
totalCalif = 0
for i in range(1, numAlumnos + 1):
    suma = 0
    for k in range(1, numCalificaciones + 1):
        suma += matriz[i][k]
        sumaGeneral += matriz[i][k]
        totalCalif += 1
    promedio = suma / numCalificaciones
    print(f"El promedio total de {matriz[i][0]} es: {promedio}")

promedioGrupo = sumaGeneral / totalCalif
print(f"\nEl promedio general del grupo es: {promedioGrupo}")

calBuscar = int(input("Ingresa la calificación que quieres buscar: "))
if calBuscar > 100:
    ("El máximo de calificación es 100. Ingresando 100 como calificación.")
    calBuscar = 100
elif calBuscar < 0:
    print("Calificación no puede ser menor a 0, registrando calificación como 0.")
    calBuscar= 0
else:
     print("Buscando calificación...")

totalBuscar = 0
for i in range (1, numAlumnos + 1):
    for k in range (1, numCalificaciones + 1):
        if calBuscar == matriz[i][k]:
            totalBuscar += 1
            print(f"\nEl alumno {matriz[i][0]} tiene {calBuscar} en la materia {matriz[0][k]}")
print(f"Se encontró un total de {totalBuscar} calificaciones iguales")
