#20. Matriz y suma de filas
#Crear una matriz de n x m con valores ingresados por el usuario y mostrar la suma de cada fila.
n = int(input("Ingrese el número de filas: "))
m = int(input("Ingrese el número de columnas: "))
matriz = []
for i in range(n):
    fila = []
    for j in range(m):
        valor = int(input(f"Ingrese el valor para la posición ({i}, {j}): "))
        fila.append(valor)
    matriz.append(fila)
for i in range(n):
    suma_fila = sum(matriz[i])
    print(f"La suma de la fila {i} es: {suma_fila}")
    