#Número invertido (nivel medio)
#Pide un número de 3 cifras (ej: 123) y muestra el número invertido (321).
#(Sugerencia: usar operadores como división entera y módulo).

numero = int(input("Ingresa un número de 3 cifras: "))
def invertir_numero(n):
    # Separamos los dígitos usando matemática pura
    unidades = n % 10
    decenas = (n // 10) % 10
    centenas = n // 100
    # Reconstruimos el número al revés
    resultado = (unidades * 100) + (decenas * 10) + centenas
    return resultado
numero_final = invertir_numero(numero)
print("El número invertido es:", numero_final)