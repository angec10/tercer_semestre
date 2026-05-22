#Operaciones básicas
#Pide dos números al usuario y muestra: suma, resta, multiplicación y división

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

def operaciones_basicas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2 
    return suma, resta, multiplicacion, division

suma, resta, multiplicacion, division = operaciones_basicas(numero1, numero2)
print("Suma: " + str(suma))
print("Resta: " + str(resta))
print("Multiplicación: " + str(multiplicacion))
print("División: " + str(division))
