def mostrar_cartelera():
    print("\n CARTELERA ")
    print("1. Avengers Endgame - 19:00 - $6")
    print("2. Batman - 20:30 - $5")
    print("3. Interestelar - 21:00 - $7")

def obtener_precio(pelicula):
    precios = {
        "Avengers Endgame": 6,
        "Batman": 5,
        "Interestelar": 7
    }

    return precios.get(pelicula, 0)

def calcular_total(cantidad, precio):
    return cantidad * precio

def mostrar_reserva(nombre, pelicula, cantidad):
    print("\n RESUMEN RESERVA ")
    print(f"Cliente : {nombre}")
    print(f"Película: {pelicula}")
    print(f"Entradas: {cantidad}")

def validar_cupos(cantidad, cupos_disponibles):

    if cantidad <= cupos_disponibles:
        return True
    else:
        return False


def Imprimir_ticket(nombre, pelicula, cantidad, total):

    print("\n TICKET ")
    print(f"Cliente  : {nombre}")
    print(f"Película : {pelicula}")
    print(f"Cantidad : {cantidad}")
    print(f"Total    : ${total:.2f}")

mostrar_cartelera()

nombre = input("\nIngrese su nombre: ")
opcion = int(input("Seleccione una película (1-3): "))

match opcion:
    case 1:
        pelicula = "Avengers Endgame"
    case 2:
        pelicula = "Batman"
    case 3:
        pelicula = "Interestelar"
    case _:
        print("Opción inválida")
        exit()

cantidad = int(input("Cantidad de entradas: "))
cupos_disponibles = 50

if not validar_cupos(cantidad, cupos_disponibles):
    print("No hay suficientes cupos.")
    exit()

def aplicar_descuento(total, tipo_cliente):
    if tipo_cliente == "menor":
        descuento = 0.35
    elif tipo_cliente == "estudiante":
        descuento = 0.10
    elif tipo_cliente == "adulto mayor":
        descuento = 0.25
    else:
        descuento = 0
    nuevo_total = total - (total * descuento)
    return nuevo_total

print("\nTipos de cliente:")
print("*menor")
print("*estudiante")
print("* adulto mayor")
print("* normal")

def ejecutar_sistema():
    tipo_cliente = input("Ingrese tipo de cliente: ").lower()
    precio = obtener_precio(pelicula)
    total = calcular_total(cantidad, precio)
    total_final = aplicar_descuento(total, tipo_cliente)
    Imprimir_ticket(nombre, pelicula, cantidad, total_final)


ejecutar_sistema()