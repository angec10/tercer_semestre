#Pide al usuario su edad actual y calcula qué edad tendrá dentro de 10 años.
def edad_futura():
    edad = int(input("Ingresa tu edad actual: "))
    edad_futura = edad + 10
    print("En 10 años, tendrás " + str(edad_futura) + " años.")

edad_futura()