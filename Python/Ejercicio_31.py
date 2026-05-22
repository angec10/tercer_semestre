#8. Factorial
#Calcular el factorial de un número ingresado.
def factorial(n):
    for i in range (1, n):
        n *= i
    return n
numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es: {factorial(numero)}")