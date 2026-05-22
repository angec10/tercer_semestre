#9. Contar letras
#Contar cuántas veces aparece una letra específica en una palabra
palabra = input("Ingrese una palabra: ")
letra = input("Ingrese la letra que desea contar: ")
contador = 0
for caracter in palabra:
    if caracter == letra:
        contador += 1
print(f"La letra '{letra}' aparece {contador} veces en la palabra '{palabra}'.")