#saludo personalizado
def nombre():
    return input("Ingrese su nombre: ")
def edad():
    return int(input("Ingrese su edad: "))

print("Bienvenido " + nombre() + " al nuevo grupo de clases de python desde (0)\n" + "tienes " + str(edad()) + " años.")