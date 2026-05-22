#Conversión de tiempo
#Solicita una cantidad de minutos y conviértela a horas y minutos.

minutos_input = int(input("Introduce la cantidad de minutos: "))
def convertir_tiempo(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

horas, minutos_restantes = convertir_tiempo(minutos_input)
print(str(minutos_input) + " minutos son: " + str(horas) + " horas y " + str(minutos_restantes) + " minutos.")