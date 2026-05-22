#13. Validar contraseña
#Pedir una contraseña hasta que coincida con una predefinida.
contraseña_predefinida = "Daniel123"
while True:
    contraseña_ingresada = input("Ingrese la contraseña: ")
    if contraseña_ingresada == contraseña_predefinida:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Intente de nuevo.")