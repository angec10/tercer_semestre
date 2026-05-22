#Contador positivos, negativos y ceros
positivos = 0
negativos = 0
ceros = 0
while True:
    numero = int(input("ingrese un numero o 999 para finalizar el programa:"))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1
    if numero == 999:
        break  
print("la cantidad de numeros positivos es:",positivos)
print("la cantidad de numeros negativos es:",negativos)
print("la cantidad de numeros ceros es:",ceros)