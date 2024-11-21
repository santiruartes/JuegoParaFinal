# Juego de preguntas sobre animales de la selva 

def juego_preguntas():
    preguntas = [
        {"pregunta": "¿Cuál es el animal más rápido de la selva?", "respuesta": "guepardo", "respuesta": "chita"},
        {"pregunta": "¿Cuál es el mamífero más grande de la selva?", "respuesta": "elefante"},
        {"pregunta": "¿Qué animal es conocido como el 'rey de la selva'?", "respuesta": "león", "respuesta":"leon", "respuesta":"leon"},
        {"pregunta": "¿Qué animal se cuelga de los árboles con su cola?", "respuesta": "mono"},
        {"pregunta": "¿Qué animal tiene una lengua muy larga para comer hormigas?", "respuesta": "oso hormiguero"},
        {"pregunta": "¿Qué animal es conocido por su habilidad de cambiar de color?", "respuesta": "camaleón", "respuesta": "cameleon"},
        {"pregunta": "¿Qué animal es conocido por su habilidad de nadar y atacar en el agua?", "respuesta": "cocodrilo", "respuesta": "coco"},
    ]
    
    puntaje = 0
    
    print("Bienvenido al juego de preguntas sobre animales de la selva!")
    print("Responde correctamente las preguntas para ganar puntos.\n")
    
    for pregunta in preguntas:
        respuesta_usuario = input(pregunta["pregunta"] + " ").strip().lower()
        if respuesta_usuario == pregunta["respuesta"]:
            print("Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {pregunta['respuesta']}.")
    
    print(f"\nJuego terminado. Obtuviste {puntaje} de {len(preguntas)} puntos.")
    if puntaje == len(preguntas):
        print("Excelente, conoces muy bien a los animales de la selva")
    elif puntaje > len(preguntas) // 2:
        print("Muy bien, tenes buenos conocimientos sobre los animales de la selva")
    else:
        print("Esta bien, aunque podes mejorar")

# Iniciar el juego
if __name__ == "__main__":
    juego_preguntas()
