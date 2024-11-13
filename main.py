from mastermind import game

var = 0

while var == 0:
    sigue = ''
    print("""
          --------------------------
          Bienvenidos a Five 4 Play:
          
          ¿Qué juego quieres jugar?

          1) Mastermind
         --------------------------- 
          """)

    juego = int(input("Ingresa el juego elegido: "))

    if juego == 1:
        game()

    sigue = input("¿Quiere seguir jugando? s (si) o n (no): ").lower()
    if sigue == 's':
        sigue = ''  # Permite repetir el ciclo de selección de juegos
    elif sigue == 'n':
        var = 1  # Salir del bucle principal y terminar el programa
        break
    else:
        print("Opción no válida. Ingresa 's' para sí o 'n' para no.")
        sigue = ''  # Reinicia sigue para pedir entrada nuevamente
