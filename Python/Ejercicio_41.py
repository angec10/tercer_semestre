#18. Números primos en rango
#Mostrar todos los números primos entre 1 y 100.

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print("Números primos entre 1 y 100:")
for numero in range(1, 101):
    if es_primo(numero):
        print(numero) 