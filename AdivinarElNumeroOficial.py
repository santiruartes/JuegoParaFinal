import random

def juego_adivina_numero():
    print("¡Hola! Bienvenido al Juego de Adivina el Número Mágico!")
    print("Estoy pensando en un número secreto entre 1 y 100.")
    print("¿Puedes adivinarlo?")

    nivel = input("Elige un nivel: 1 (fácil), 2 (medio), 3 (difícil): ")
    if nivel == "1":
        max_num = 10
    elif nivel == "2":
        max_num = 50
    else:
        max_num = 100

    numero_secreto = random.randint(1, max_num)
    intentos = 0
    
    

    while True:

        numero_usuario = int(input("Adivine el número: "))
        intentos += 1
        diferencia = abs(numero_usuario - numero_secreto)

        if numero_usuario < numero_secreto:
            if diferencia <= 10:
                print("¡Estás muy cerca! El número secreto es un poco mayor.")
            elif diferencia <= 20:
                print("¡Estás cerca! El número secreto es algo mayor.")
            else:
                print("¡Estás frío! El número secreto es mucho mayor.")
        elif numero_usuario > numero_secreto:
            if diferencia <= 10:
                print("¡Estás muy cerca! El número secreto es un poco menor.")
            elif diferencia <= 20:
                print("¡Estás cerca! El número secreto es algo menor.")
            else:
                print("¡Estás frío! El número secreto es mucho menor.")
        else:
            print(f"Felicidades! Adivinaste el número en {intentos} intentos")
            print("¡Eres un mago!")
            break

 
        

if __name__ == "__main__":
    juego_adivina_numero()


