#6. Tabla de multiplicar
#Mostrar la tabla de multiplicar de un número ingresado por el usuario.
multiplicador = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {multiplicador}:")
for i in range(1, 11):
    resultado = multiplicador * i
    print(f"{multiplicador} * {i} = {resultado}")   