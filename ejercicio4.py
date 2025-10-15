def llenar_matriz(h, a, fila=0, matriz=None):
    if matriz is None: 
        matriz = [[0] * a for _ in range(h)]
    
    if fila == h:
        return matriz
    
    def llenar_fila(fila, col=0):
        if col == a:
            return
        valor = int(input(f"Ingrese el número en posición [{fila}][{col}]: "))
        matriz[fila][col] = valor
        llenar_fila(fila, col + 1)
    
    llenar_fila(fila)
    return llenar_matriz(h, a, fila + 1, matriz)


def imprimir_matriz(matriz, fila=0, col=0):
    if fila == len(matriz):  # ya no hay más filas
        return
    
    if col == len(matriz[0]):  # fin de la fila → salto de línea
        print()
        imprimir_matriz(matriz, fila + 1, 0)
        return
    
    print(matriz[fila][col], end=" ")  
    imprimir_matriz(matriz, fila, col + 1)


def suma_fila(matriz, fila, col=0):
    if col == len(matriz[fila]) - 1:
        return matriz[fila][col]
    return matriz[fila][col] + suma_fila(matriz, fila, col + 1)


def mostrar_sumas(matriz, fila=0): 
    if fila == len(matriz):
        return
    print(f"Suma de la fila {fila}: {suma_fila(matriz, fila)}")
    mostrar_sumas(matriz, fila + 1)

h = int(input("Ingresa la altura de tu arreglo: "))
a = int(input("Ingresa el ancho de tu arreglo: "))

if h == 0 or a == 0:
    print("Número inválido, no se puede hacer el arreglo")
else:
    matriz = llenar_matriz(h, a)
    print("\nMatriz ingresada:")
    imprimir_matriz(matriz)
    print("\n\nSuma de los elementos por fila:")
    mostrar_sumas(matriz)