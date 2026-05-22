def mostrar_rutinas():
    print("Rutinas disponibles:")
    print("- Cardio")
    print("- Fuerza")
    print("- Resistencia")

def mostrar_usuario(nombre, rutina):
    print(f"Usuario: {nombre} | Rutina: {rutina}")

def calcular_calorias(minutos, intensidad):
    return minutos * intensidad * 5

def evaluar_rendimiento(calorias):
    if calorias < 200:
        return "Bajo"
    elif calorias <= 500:
        return "Medio"
    else:
        return "Alto"

# Desafío extra
# Guardar:
# • historial de entrenamientos
historial = []
def guardar_entrenamiento(nombre, rutina, calorias):
    historial.append({"nombre": nombre, "rutina": rutina, "calorias": calorias})

# • promedio semanal
def promedio_semanal():
    total = 0
    for e in historial:
        total += e["calorias"]
    return total / len(historial)

# • rutina más utilizada
def rutina_mas_utilizada():
    conteos = {"Cardio": 0, "Fuerza": 0, "Resistencia": 0}
    for e in historial:
        conteos[e["rutina"]] += 1
    mayor = ""
    maximo = 0
    for rutina in conteos:
        if conteos[rutina] > maximo:
            maximo = conteos[rutina]
            mayor = rutina
    return mayor

mostrar_rutinas()

while True:
    print("\n--- NUEVO REGISTRO ---")
    nombre = input("Ingrese el nombre: ")
    rutina = input("Ingrese su rutina (Cardio/Fuerza/Resistencia): ").capitalize()
    minutos = int(input("Ingrese los minutos: "))
    intensidad = int(input("Ingrese la intensidad (1-5): "))

    mostrar_usuario(nombre, rutina)

    calorias = calcular_calorias(minutos, intensidad)
    rendimiento = evaluar_rendimiento(calorias)

    print(f"Calorías quemadas: {calorias}")
    print(f"Rendimiento: {rendimiento}")

    guardar_entrenamiento(nombre, rutina, calorias)

    continuar = input("\n¿Desea registrar otro entrenamiento? (si/no): ").lower()
    if continuar != "si":
        print("Saliendo del simulador...")
        break

print("\n--- ESTADÍSTICAS GLOBALES ---")
print(f"Total de entrenamientos registrados: {len(historial)}")
print(f"Promedio de calorías quemadas: {promedio_semanal():.2f}")
print(f"Rutina más utilizada: {rutina_mas_utilizada()}")