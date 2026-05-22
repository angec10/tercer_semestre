def calcular_areas():
    print("Calculadora de áreas")
    print("1. Área del círculo") 
    print("2. Área del cuadrado")
    print("3. Área del triángulo")
    opcion = int(input("Seleccione una opción (1-3): "))
    try:
        match opcion:
            case 1:
                radio = float(input("Ingrese el radio del círculo: "))
                area_circulo = 3.1416 * radio ** 2
                print("El área del círculo es: ", area_circulo)
            case 2:
                lado = float(input("Ingrese el lado del cuadrado: "))
                area_cuadrado = lado ** 2
                print("El área del cuadrado es: ", area_cuadrado)
            case 3:
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                area_triangulo = (base * altura) / 2
                print("El área del triángulo es: ", area_triangulo)
            case _:
                print("Opción no válida. Por favor, seleccione una opción entre 1 y 3.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
calcular_areas()