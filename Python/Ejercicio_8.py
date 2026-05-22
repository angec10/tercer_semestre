def acceso() :
    Contraseña = "admin123"
    entrada = input ("Ingrese la contraseña: ")

    if entrada == Contraseña:
        print ("Acceso permitido")
    else:
        print("Acesso no permitido")

acceso()
