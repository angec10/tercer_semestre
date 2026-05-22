#solicitar una contraseña hasta que tenga minimo 8 caracteres y conenga al menos un numero.
while True:
    contraseña = input("Ingrese una contraseña (mínimo 8 caracteres y al menos un número): ")
    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres. Intente de nuevo.")
        continue
    tiene_numero = False
    for char in contraseña:
        if char >= "0" and char <= "9":
            tiene_numero = True
    if tiene_numero == False:
        print("La contraseña debe contener al menos un número. Intente de nuevo.")
        continue
    print("Contraseña válida. ¡Gracias!")
    break