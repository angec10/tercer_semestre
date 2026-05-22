#14. Número dentro de rango
#Solicitar un número entre 10 y 50 hasta que sea válido.
while True:
    numero = int(input("Ingrese un número entre 10 y 50: "))
    n = 22
    if numero == n:
        print(f"Número válido: {numero}")
        break
    else:
        print("Número no valido. Intente de nuevo.")
        