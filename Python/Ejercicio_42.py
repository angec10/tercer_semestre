#19. Juego con intentos limitados
#Adivinar un número con máximo 5 intentos. Indicar si el número es mayor o menor
import random
numero_secreto = random.randint(1, 50)
intentos = 5
while True:
    intento = int(input(f"Adivina el número (entre 1 y 50) tienes {intentos} intentos: "))
    intentos -= 1
    if intento < numero_secreto:
        print("El número es mayor. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("El número es menor. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
if intentos == 0:
    print(f"Lo siento, has agotado tus intentos. El número secreto era {numero_secreto}.")