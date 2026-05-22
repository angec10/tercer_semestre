# Realizar un programa en el que valide la identidad del usuairio solo con la contraseña, 
# si el usuario es correcto se le dará la bienvenida, caso contrario se le indicará que la contraseña es incorrecta.

def login(usuario, contraseña):
    clave = "1234"
    if contraseña == clave:
        print("Bienvenido a clases de Python señor " + usuario)
    else:
        print("Contraseña incorrecta")  
password_ingresado = input("Ingresa tu contraseña: ")
login("Juan", password_ingresado)

