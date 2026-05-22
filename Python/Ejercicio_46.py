#6. Tabla de multiplicar
#Pedir un número al usuario y mostrar su tabla de multiplicar del 1 al numero que el usuario indique.
multiplicador = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
limite = int(input("Ingrese el límite de la tabla de multiplicar: "))
print(f"Tabla de multiplicar del {multiplicador}:")
for i in range(1, limite + 1):
    resultado = multiplicador * i
    print(f"{multiplicador} * {i} = {resultado}")   