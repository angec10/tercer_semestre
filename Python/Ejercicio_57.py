def iniciar_juego():
    print("BIENVENIDO JUGADOR")
    print("1. Jugar")
    print("2. Salir")

def clases_disponibles():
    print("CLASES DISPONIBLES:")
    print("- Guerrero")
    print("- Mago")
    print("- Arquero")
    print("- Asesino")
    print("- Clerigo")
    print("- Domador de bestias")
    print("- Invocador")

def mostrar_personaje(nombre, clase, nivel):
    print(f"Nombre: {nombre} | Clase: {clase} | Nivel: {nivel}")

def calcular_experiencia(misiones, enemigos):
    xp = (misiones * 50) + (enemigos * 20)
    return xp

def subir_nivel(xp, nivel):
    nuevo_nivel = nivel
    while (xp >= 500):
        xp -= 500
        nuevo_nivel += 1
    if nivel != nuevo_nivel:
        print(f"NUEVO NIVEL ALCANZADO! | nv{nuevo_nivel}")
        return xp, nuevo_nivel
    else:
        return xp, nivel

ejecutando = True
while ejecutando:
    iniciar_juego()
    opcion = input("Opcion: ")

    if opcion == "1":
        jugando = True
        experiencia_total = 0
        nivel_personaje = 0

        nombre_personaje = input("Nombre para tu personaje: ")
        clases_disponibles()
        clase_personaje = input("A que clase corresponde tu personaje? ")
        
        while jugando:
            print("* ESTADISTICAS DE TU PERSONAJE *")
            mostrar_personaje(nombre_personaje, clase_personaje, nivel_personaje)

            misiones_completadas = int(input("Cuantas misiones has completado? "))
            enemigos_derrotados = int(input("Cuantos enemigos has derrotado? "))

            experiencia_total += calcular_experiencia(misiones_completadas, enemigos_derrotados)
            experiencia_total, nivel_personaje = subir_nivel(experiencia_total, nivel_personaje)

            while True:
                opcion = input("Continuar (1) / Retirarse (2)? ")
                if opcion == "1":
                    break
                elif opcion == "2":
                    print("* ESTADISTICAS FINALES DE TU PERSONAJE *")
                    mostrar_personaje(nombre_personaje, clase_personaje, nivel_personaje)
                    print("GRACIAS POR JUGAR!")
                    ejecutando = False
                    jugando = False
                    break
                else:
                    print("Opcion invalida.")
    elif opcion == "2":
        print("Cerrando juego...")
        break
    else:
        print("Opcion invalida.")