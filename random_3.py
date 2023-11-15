from random import randint
numero_secreto = randint(1, 10)
intentos = 0
max_intentos = 3

print("Bienvenido al juego de adivinanza de números entre 1 y 10. ¡Tienes 3 intentos!")

while intentos < max_intentos:
    
    intento = int(input("Intenta adivinar el número: "))

    intentos += 1

    if intento == numero_secreto:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        break
    else:
        print("Intento incorrecto. Sigue intentando...")


if intentos == max_intentos:
    print(f"Lo siento, te has quedado sin intentos. El número secreto era {numero_secreto}. ¡Mejor suerte la próxima vez!")
