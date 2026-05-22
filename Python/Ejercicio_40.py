#17. Pirámide invertida
#Mostrar una pirámide invertida de asteriscos según un número ingresado.

altura = int(input("Ingrese la altura de la pirámide invertida: "))
for i in range(altura, 0, -1):
    print(" " * (altura - i) + "*" * (2 * i - 1))
    