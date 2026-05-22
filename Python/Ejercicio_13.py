#Cálculo de salario
#Pide el número de horas trabajadas y el pago por hora.
#Calcula el salario total.
#Si quieres subir dificultad: agrega un descuento del 10%.


# Solicitar al usuario el número de horas trabajadas y el pago por hora
horas = float(input("Ingrese el número de horas trabajadas: "))
pago = float(input("Ingrese el pago por hora: "))

def calcular_salario(horas_trabajadas, pago_por_hora):
    salario_total = horas_trabajadas * pago_por_hora
    descuento = salario_total * 0.10
    salario_con_descuento = salario_total - descuento
    return salario_con_descuento

# Calcular el salario final después del descuento
salario_final = calcular_salario(horas, pago)
print("El salario final después del descuento del 10% es: " + str(salario_final))