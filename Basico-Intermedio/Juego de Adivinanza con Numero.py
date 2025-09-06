import random
print("***Juego de Adivinanza de Numero***\n")


intentos = 0
max_intentos = 10
puntos = 100
numero_secreto = random.randint (1,50)


while intentos < max_intentos :
    juego = int(input("Juego de adivina. Ingresa un numero entre 1 y 50 : "))
    intentos += 1

    if juego == numero_secreto:
        print("Felicidades lo adivinaste ")
        print("Lo lograste en", intentos, "intentos.")
        print("Tu puntuacion es",puntos)
        break
    elif juego < numero_secreto :
        print("Numero incorrecto. El numero secreto es mayor")
    else:
        print("Numero incorrecto, El numero secreto es menor")
    puntos -= 10
if intentos == max_intentos:
    print("Se acabaron los intentos. Mas suerte para la proxima." )
    print("el numero secreto era", numero_secreto )
    print("Tu puntuacion final es",puntos,"puntos")