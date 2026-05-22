#Área de un triángulo
#Pide la base y la altura de un triángulo y calcula su área.

base = float(input("Introduce la base del triángulo: "))
altura = float(input("Introduce la altura del triángulo: "))

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area
area = calcular_area_triangulo(base, altura)
print("El área del triángulo es: " + str(area))