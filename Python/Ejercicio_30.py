#7. Suma de pares
#Calcular la suma de todos los números pares entre 1 y 100.
suma_pares = 0
for i in range(1, 101):
    if i % 2 == 0:
        suma_pares += i
numeros_pares = [i for i in range(1, 101) if i % 2 == 0]
print("La suma de todos los números pares entre 1 y 100 es:", suma_pares)
print("Los números pares entre 1 y 100 son:", numeros_pares)