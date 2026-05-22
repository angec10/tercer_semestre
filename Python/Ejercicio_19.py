# Promedio de notas
# Solicita 4 notas de un estudiante y calcula el promedio
#Muestra el resultado con 2 decimales.

def calcular_promedio(n1, n2, n3, n4):
    return (n1 + n2 + n3 + n4) / 4  
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))
nota4 = float(input("Ingresa la cuarta nota: "))
promedio = calcular_promedio(nota1, nota2, nota3, nota4)
decimales = int(promedio * 100) / 100   
print("El promedio de las notas es: " + str(decimales))

    