#Consumo de combustible
#Pide los kilómetros recorridos y los litros de gasolina consumidos.
#Calcula el consumo por kilómetro.

kilometros_recorridos = float(input("Introduce los kilómetros recorridos: "))
litros_consumidos = float(input("Introduce los litros de gasolina consumidos: "))

def calcular_consumo(kilometros, litros):
    return litros / kilometros

consumo_por_kilometro = calcular_consumo(kilometros_recorridos, litros_consumidos)
print("El consumo por kilómetro es: " + str(consumo_por_kilometro) + " litros/km")