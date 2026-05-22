
def mostrar_restaurantes():
    print("\nRESTAURANTES DISPONIBLES")
    print("1. Burger Zone (Hamburguesas)")
    print("2. Pizza Planet (Pizzas)")
    print("3. Green Salad (Saludable)")
    print("4. Sushi Roll (Asiática)")
    print("--------------------------------")

def mostrar_menu(opcion_restaurante):
    if opcion_restaurante == 1:
        print("\n--- MENÚ DE Burger Zone ---")
        print("1. Classic Burger - $8.50")
        print("2. Cheese Burger - $9.00")
        print("3. Bacon Burger - $10.00")
    elif opcion_restaurante == 2:
        print("\n--- MENÚ DE Pizza Planet ---")
        print("1. Pepperoni Pizza - $12.00")
        print("2. Veggie Pizza - $11.00")
        print("3. BBQ Chicken Pizza - $13.00")
    elif opcion_restaurante == 3:
        print("\n--- MENÚ DE Green Salad ---")
        print("1. Caesar Salad - $7.50")
        print("2. Greek Salad - $8.00")
        print("3. Quinoa Salad - $9.00")
    elif opcion_restaurante == 4:
        print("\n--- MENÚ DE Sushi Roll ---")
        print("1. California Roll - $10.00")
        print("2. Spicy Tuna Roll - $11.50")
        print("3. Avocado Roll - $9.00")
    else:
        print("Opción de restaurante inválida. Cerrando programa...")
        exit()
    print("--------------------------------")

def obtener_nombre_y_precio(opcion_restaurante, opcion_platillo):
    if opcion_restaurante == 1:
        restaurante_nombre = "Burger Zone"
        if opcion_platillo == 1:
            return restaurante_nombre, "Classic Burger", 8.50
        elif opcion_platillo == 2:
            return restaurante_nombre, "Cheese Burger", 9.00
        elif opcion_platillo == 3:
            return restaurante_nombre, "Bacon Burger", 10.00
        else:
            print("Opción de platillo inválida")
            exit()
            
    elif opcion_restaurante == 2:
        restaurante_nombre = "Pizza Planet"
        if opcion_platillo == 1:
            return restaurante_nombre, "Pepperoni Pizza", 12.00
        elif opcion_platillo == 2:
            return restaurante_nombre, "Veggie Pizza", 11.00
        elif opcion_platillo == 3:
            return restaurante_nombre, "BBQ Chicken Pizza", 13.00
        else:
            print("Opción de platillo inválida")
            exit()
            
    elif opcion_restaurante == 3:
        restaurante_nombre = "Green Salad"
        if opcion_platillo == 1:
            return restaurante_nombre, "Caesar Salad", 7.50
        elif opcion_platillo == 2:
            return restaurante_nombre, "Greek Salad", 8.00
        elif opcion_platillo == 3:
            return restaurante_nombre, "Quinoa Salad", 9.00
        else:
            print("Opción de platillo inválida")
            exit()
            
    elif opcion_restaurante == 4:
        restaurante_nombre = "Sushi Roll"
        if opcion_platillo == 1:
            return restaurante_nombre, "California Roll", 10.00
        elif opcion_platillo == 2:
            return restaurante_nombre, "Spicy Tuna Roll", 11.50
        elif opcion_platillo == 3:
            return restaurante_nombre, "Avocado Roll", 9.00
        else:
            print("Opción de platillo inválida")
            exit()
    else:
        print("Opción de restaurante inválida")
        exit()
    
def mostrar_pedido(cliente, restaurante, pedido):
    print("\n========================================")
    print("           RESUMEN DEL PEDIDO           ")
    print("========================================")
    print(f"Cliente:     {cliente}")
    print(f"Restaurante: {restaurante}")
    print(f"Detalle:     {pedido}")
    print("----------------------------------------")

def calcular_envio(distancia):
    if distancia <= 3:
        return 2.00
    else:
        if distancia <= 10:
            return 5.00
        else:
            return 8.00

def aplicar_cupon(cupon, subtotal):
    if cupon == "050512":
        print("¡Cupón aplicado! 10% de descuento en tu comida.")
        return subtotal * 0.10
    elif cupon == "050513":
        print("¡Cupón aplicado! $3 de descuento en tu comida.")
        if subtotal > 3:
            return 3.00
        else:
            return subtotal
    else:
        if cupon != "":
            print("Cupón inválido o expirado.")
        return 0.00

def calcular_tiempo_estimado(distancia, prioridad):
    tiempo_por_distancia = 0
    kilometros_enteros = int(distancia) 
    for i in range(kilometros_enteros):
        tiempo_por_distancia = tiempo_por_distancia + 5
    tiempo_base = tiempo_por_distancia + 15  
    if prioridad == 1: 
        tiempo_base = tiempo_base - 10
        if tiempo_base < 15:
            tiempo_base = 15
        return f"{tiempo_base} a {tiempo_base + 5} minutos"
    else:
        return f"{tiempo_base} a {tiempo_base + 10} minutos"

def calcular_total(comida, envio, descuento, prioridad):
    cargo_prioridad = 0.00
    if prioridad == 1:
        cargo_prioridad = 2.50
    total = (comida - descuento) + envio + cargo_prioridad
    if total < 0:
        total = 0.00
    return total, cargo_prioridad

def ejecutar_sistema_delivery():
    print("--- BIENVENIDO A LA APP DE DELIVERY ---")
    nombre_cliente = input("Ingrese su nombre: ")
    mostrar_restaurantes()
    id_restaurante = int(input("Seleccione el NÚMERO del restaurante (1-4): "))
    mostrar_menu(id_restaurante) 
    id_platillo = int(input("Seleccione el NÚMERO del platillo (1-3): "))
    restaurante_txt, platillo_txt, costo_comida = obtener_nombre_y_precio(id_restaurante, id_platillo)   
    distancia_entrega = float(input("Ingrese la distancia de entrega en km: "))
    codigo_cupon = input("Ingrese el código de cupón (o presione Enter para continuar): ")
    envio_prioritario = int(input("¿Desea envío prioritario? (1 para Sí, 0 para No): "))  
    mostrar_pedido(nombre_cliente, restaurante_txt, platillo_txt)
    costo_envio = calcular_envio(distancia_entrega)
    monto_descuento = aplicar_cupon(codigo_cupon, costo_comida)
    tiempo_llegada = calcular_tiempo_estimado(distancia_entrega, envio_prioritario)
    total_pagar, extra_prioridad = calcular_total(costo_comida, costo_envio, monto_descuento, envio_prioritario)
    print(f"Subtotal Comida:   ${costo_comida:.2f}")
    if monto_descuento > 0:
        print(f"Descuento:        -${monto_descuento:.2f}")
    print(f"Costo de Envío:    ${costo_envio:.2f} ({distancia_entrega} km)")
    if envio_prioritario == 1:
        print(f"Cargo Prioridad:   ${extra_prioridad:.2f}")
    print("----------------------------------------")
    print(f"TOTAL A PAGAR:     ${total_pagar:.2f}")
    print("----------------------------------------")
    print(f"Tiempo estimado:   {tiempo_llegada}")
    print("========================================\n")

# Ejecutar el programa
ejecutar_sistema_delivery()