numAlumnos = int(input("Ingresar el número de alumnos: "))
numCalificaciones = int(input("Ingresa el número de materias a calificar: "))

# Creamos matriz (filas = alumnos, columnas = materias + nombre)
matriz = [[0 for _ in range(numCalificaciones + 1)] for _ in range(numAlumnos + 1)]

matriz[0][0] = "Alumnos"

for i in range(1, numCalificaciones + 1):
    calificaciones = input(f"Insertar el nombre de la materia {i}: ")
    matriz[0][i] = calificaciones

for j in range(1, numAlumnos + 1):
    alumnos = input(f"Inserta el nombre del alumno {j}: ")
    matriz[j][0] = alumnos

for i in range(1, numAlumnos + 1):
    for k in range(1, numCalificaciones + 1):
        datoCal = int(input(f"Ingresa la calificación para el alumno {matriz[i][0]} en la materia {matriz[0][k]}: "))
        if datoCal > 100:
            print("El máximo de calificación es 100. Ingresando 100 como calificación.")
            datoCal = 100
        elif datoCal < 0:
            print("Calificación no puede ser menor a 0, registrando calificación como 0.")
            datoCal = 0
        matriz[i][k] = datoCal

print("\n--- MATRIZ DE CALIFICACIONES ---")
for fila in matriz:
    print(fila)

# Promedios por alumno
print("\n--- PROMEDIOS POR ALUMNO ---")
suma_general = 0
total_calif = 0
for i in range(1, numAlumnos + 1):
    suma = 0
    for k in range(1, numCalificaciones + 1):
        suma += matriz[i][k]
        suma_general += matriz[i][k]
        total_calif += 1
    promedio = suma / numCalificaciones
    print(f"El promedio de {matriz[i][0]} es: {promedio:.2f}")

# Promedio general del grupo
promedio_grupo = suma_general / total_calif
print(f"\nEl promedio general del grupo es: {promedio_grupo:.2f}")

# Búsqueda de calificación
buscar = int(input("\nIngresa la calificación que deseas buscar en la matriz: "))
encontrado = False
for i in range(1, numAlumnos + 1):
    for k in range(1, numCalificaciones + 1):
        if matriz[i][k] == buscar:
            print(f"Se encontró la calificación {buscar} en {matriz[i][0]} ({matriz[0][k]}).")
            encontrado = True

if not encontrado:
    print(f"La calificación {buscar} no se encuentra en la matriz.")
