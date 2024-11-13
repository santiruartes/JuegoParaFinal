
import random


def game():
    aux = 0

    while aux == 0:
        print("¡Bienvenido a Mastermind!")
        print("Elija la dificultad: (1 = Facil, 2 = Medio, 3 = Dificil.)")
        dificultad = int(input("Dificultad: "))

        # Determinamos la cantidad de dígitos según la dificultad
        if dificultad == 1:
            cant_dig = 3
        elif dificultad == 2:
            cant_dig = 4
        else:
            cant_dig = 5

        # Creamos el código secreto sin dígitos repetidos
        digitos = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        codigo = ''
        for i in range(cant_dig):
            elegido = random.choice(digitos)
            while elegido in codigo:
                elegido = random.choice(digitos)
            codigo += elegido

        print(f"Debes adivinar un código de {cant_dig} dígitos diferentes.")
        jugada = input("Ingresa tu jugada: ")

        intentos = 1

    # Bucle para continuar hasta adivinar el código
        while jugada != codigo:
            intentos += 1
            aciertos = 0
            coincidencias = 0
            for i in range(cant_dig):
                if jugada[i] == codigo[i]:
                    aciertos += 1
                elif jugada[i] in codigo:
                    coincidencias += 1
            print(f"Tu jugada {jugada} tiene {aciertos} aciertos y {
                coincidencias} coincidencias.")
            jugada = input("Haz otra jugada: ")

        print(f"¡Bien hecho! Adivinaste el código {
            codigo} en {intentos} intentos.")
        aux = int(input("¿Quieres seguir jugando? (0 = sí, 1 = no): "))


if __name__ == "__main__":
    game()
