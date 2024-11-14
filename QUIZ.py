    # Defini las preguntas y respuestas del quiz
def juegoquiz ():
    quiz = [
        {
            "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
            "opciones": ["A) Venus", "B) Marte", "C) Júpiter", "D) Saturno"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿Qué órgano del cuerpo humano es responsable de bombear la sangre?",
            "opciones": ["A) Hígado", "B) Riñón", "C) Corazón", "D) Pulmón"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "¿En qué año comenzó la Primera Guerra Mundial?",
            "opciones": ["A) 1914", "B) 1920", "C) 1939", "D) 1945"],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "¿Quién escribió 'Don Quijote de la Mancha'?",
            "opciones": ["A) Gabriel García Márquez", "B) Miguel de Cervantes", "C) Julio Cortázar", "D) Pablo Neruda"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál es el elemento químico cuyo símbolo es 'O'?",
            "opciones": ["A) Oro", "B) Oxígeno", "C) Osmio", "D) Hidrógeno"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "¿Cuál es el país más grande en extensión territorial?",
            "opciones": ["A) Canadá", "B) China", "C) Rusia", "D) Estados Unidos"],
            "respuesta_correcta": "C"
        }
    ]

    # Función para ejecutar el quiz recibiendo la respuesta del usuario
    def ejecutar_quiz():
        puntaje = 0
        for pregunta in quiz:
            print(pregunta["pregunta"])
            for opcion in pregunta["opciones"]:
                print(opcion)
            
            # Solicitar al usuario que ingrese su respuesta
            respuesta_usuario = input("Elige una opción (A, B, C, D): ").upper()
            
            # Verificar si la respuesta es correcta o incorrecta
            if respuesta_usuario == pregunta["respuesta_correcta"]:
                print("¡Correcto!\n")
                puntaje += 1
            else:
                print(f"Incorrecto. La respuesta correcta era {pregunta['respuesta_correcta']}.\n")
        
        print(f"Tu puntaje final es: {puntaje}/{len(quiz)}")

    # Ejecutamos la función del quiz
    ejecutar_quiz()
    if __name__=="__main__":
        juegoquiz()