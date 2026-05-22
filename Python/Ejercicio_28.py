#5. Validación de entrada
#Pedir un número positivo. Repetir hasta que el usuario ingrese un valor válido.
while True:
    numero = float(input("Ingrese un número positivo: "))
    if numero > 0:
        print("Número válido ingresado:", numero)
        break
    else:
        print("Número no válido. Por favor, intente nuevamente.")
        