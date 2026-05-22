#suma de pares e impares
suma_pares=0
suma_impares=0
numeros = [int(input("ingrese 10 numeros:")) for i in range(10)]
for j in range(len(numeros)):
    if numeros[j] % 2 == 0:
        suma_pares += numeros[j]
    else:
        suma_impares += numeros[j]
print("la suma de los numeros pares es:",suma_pares)
print("la suma de los numeros impares es:",suma_impares)