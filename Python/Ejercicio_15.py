# Conversión de dólares a euros
tasa = 0.85  # Tasa fija de conversión
dolares = float(input("Ingresa la cantidad en dólares: "))

def convertir_a_euros(dolares, tasa):
    return dolares * tasa
euros = convertir_a_euros(dolares, tasa)
print("Los " + str(dolares) + " dólares son equivalentes a " + str(euros) + " euros.")
