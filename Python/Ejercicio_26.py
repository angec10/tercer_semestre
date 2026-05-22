#3. Suma de números
#Pedir números al usuario hasta que ingrese 0. Mostrar la suma total de los números ingresados.
suma = 0
while True:
    numero = int(input("ingrese un numero y luego el 0 para finalizar: "))
    if numero == 0:
        break
    suma += numero
print("La suma total de los números ingresados es:", suma)