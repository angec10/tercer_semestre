#15. Acumulador de compras
#Permitir ingresar precios de productos hasta que el usuario decida terminar. Mostrar el total.
total = 0
while True:
    precio = float(input("Ingrese el precio del producto: "))
    total += precio
    terminar_compra = input("¿Desea terminar la compra? (s/n): ")
    if terminar_compra == "s":
        break
print(f"El total de la compra es: {total}")
