#11. Menú simple do-while
#Mostrar un menú con opciones (1. Saludar, 2. Despedirse, 3. Salir). Repetir hasta elegir salir.
while True:
    print("Menú:")
    print("1. Mostrar los días de la semana")
    print("2. Mostrar un saludo personalizado")
    print("3. Mostrar información sobre el programa")
    print("4. Salir")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == '1':
        print("Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo")
    elif opcion == '2':
        nombre = input("Ingrese su nombre: ")
        print(f"¡Hola, {nombre}!")
    elif opcion == '3':
        print("Este es un programa simple que muestra diferentes opciones.")
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
