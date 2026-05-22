#CAJERO AUTOMATICO SIMPLE.

saldo_cuenta = 1000

def menu():
    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Retirar dinero")
    print("2. Depositar dinero")
    print("3. Salir")

def cajero(saldo_actual):
    menu()
    opcion = input("Seleccione una opción: ")
    match opcion:
        case "1":
            retirar = float(input("Cantidad a retirar: "))
            if retirar <= saldo_actual:
                saldo_actual -= retirar
                print("Retiro exitoso")
            else:
                print("No hay dinero suficiente")           
        case "2":
            depositar = float(input("Cantidad a depositar: "))
            saldo_actual += depositar
            print("Depósito exitoso")
        case "3":
            print("Gracias por usar el cajero automático")
            
    return saldo_actual
saldo_cuenta = cajero(saldo_cuenta)
print("Tu saldo final es: " + str(saldo_cuenta))


