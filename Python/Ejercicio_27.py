#4. Promedio de valores
#Solicitar números hasta que el usuario ingrese un número negativo. Calcular el promedio.
suma = 0
contador = 0
while True:
    numero = float(input("Ingrese un número (negativo para finalizar): "))
    if numero < 0:
        break
    suma += numero
    contador += 1
if contador > 0:
    promedio = suma / contador
    print("El promedio de los números ingresados es:", promedio)
else:
    print("No se ingresaron números válidos para calcular el promedio.")
    