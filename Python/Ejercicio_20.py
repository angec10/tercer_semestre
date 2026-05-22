#Solicita el precio de 3 productos y calcula el total a pagar.
#Agrega un 15% de IVA al resultado final.    

precio1 = float(input("Ingresa el precio del primer producto: "))
precio2 = float(input("Ingresa el precio del segundo producto: "))
precio3 = float(input("Ingresa el precio del tercer producto: "))

def calculo_iva(precio1, precio2, precio3):
    total = precio1 + precio2 + precio3
    iva = total * 0.15
    total_con_iva = total + iva
    return total_con_iva 
total_a_pagar = calculo_iva(precio1, precio2, precio3)
print("El total a pagar con IVA incluido es: " + str(total_a_pagar))