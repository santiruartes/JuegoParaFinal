from mastermind import game
from animalesDeLaSelva import juego_preguntas
from AdivinarElNumeroOficial import juego_adivina_numero
from QUIZ import juegoquiz

var = 0

while var == 0:
    sigue = ''
    print("""
          --------------------------
          Bienvenidos a Five 4 Play:
          
          ¿Qué juego quieres jugar?

          1) Mastermind
          2) Animales de la selva
          3) Adivina el número
          4) Quiz
         --------------------------- 
          """)

    juego = int(input("Ingresa el juego elegido: "))

    if juego == 1:
        game()
    elif juego == 2:
        juego_preguntas()
    elif juego == 3:
        juego_adivina_numero()
    elif juego == 4:
        juegoquiz()

    sigue = input("¿Quiere seguir jugando? s (si) o n (no): ").lower()
    if sigue == 's':
        sigue = ''  # Permite repetir el ciclo de selección de juegos
    elif sigue == 'n':
        var = 1  # Salir del bucle principal y terminar el programa
        break
