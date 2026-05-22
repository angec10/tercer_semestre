
def acceso() :
    contraseña = "admin123"
    entrada = input ("Ingrese la contraseña: ")

    if entrada == contraseña:
        print ("Acceso permitido")
    else:
        print("Acesso no permitido")

acceso()
