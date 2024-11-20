def gp():
    preguntas_y_respuestas=[
        {
            "pregunta":"1) ¿CUAL DE ESTOS MATERIALES NO SE PUEDE RECICLAR?",
            "opciones": ["A) Papel", "B) Plastico", "C) Vidrio","D)Papel Higienico"],
            "respuesta_correcta": "D",
            "mensaje": "Sabías que, lo mejor es tirarlo en la basura normal porque, aunque no lo podamos reciclar, se descompone poco a poco en el basurero sin causar tanto daño"
        },
        {
            "pregunta":"2) ¿QUE ES LA DEFORESTACION?",
            "opciones": ["A) Plantar arboles", "B) Cortar arboles ilegalmente", "C) Cuidar los bosques","D) Ninguna es correcta"],
            "respuesta_correcta": "B",
            "mensaje":"Sabías que los árboles ayudan mucho al medioambiente? Ellos ayudan a que el aire sea más limpio, ayudan a que no se produzcan inundaciones, nos dan comida y medicina."
        },
        {
            "pregunta":"3) ¿QUE ES EL CAMBIO CLIMATICO?",
            "opciones": ["A) Cambio del clima en la tierra", "B) Clima de un solo dia", "C) Cambio de estacion","D) Aumento de lluvias"],
            "respuesta_correcta": "A",
            "mensaje": "El clima es como el “Humor” de la tierra, por eso el cambio climático significa que el clima está cambiando de humor de forma extraña y no tan buena para la Tierra."
        },
        {   "pregunta":"4) SI VES A ALGUIEN TIRANDO BASURA EN LA CALLE, ¿QUE HACES?",
            "opciones": ["A) No hacer nada", "B) Decirle que no lo haga", "C) Recoger la basura y tirarla en el lugar correcto"],
            "respuesta_correcta": "C",
            "mensaje":"sabías que levantando la basura del piso evitas que esta llegue al agua, protege a los animales, ayudas a mantener la ciudad más limpia y bonita, también reducimos la contaminación "

        },
        {
            "pregunta":"5) ¿QUE BOLSA USARIAS?",
            "opciones": ["A) Bolsa de plastico", "B) Bolsa de tela"],
            "respuesta_correcta": "B",
            "mensaje":"¿Sabías que las bolsas de plástico no se deshacen fácilmente y pueden quedarse en la Tierra durante muchos, muchos años? Eso significa que si las dejamos en el suelo, o se van al mar, pueden dañar a los animales, como los peces y las tortugas, que pueden tragarlas sin querer. ¡Y eso no está bien"
        },
        {
            
            "pregunta":"6) ¿POR QUE ES TAN IMPORTANTE APAGAR LA LUZ?",
            "opciones": ["A) Ahorrar energia", "B) No importa si las dejo prendidas","No tiene desperdicio"],
            "respuesta_correcta": "A",
            "mensaje":"Las luces usan energía, y mucha de esa energía viene de cosas que contaminan el aire, como las plantas que queman carbón o gas. Si apagamos las luces cuando no las necesitamos, usamos menos energía y ayudamos a que el aire esté más limpio. ¡Así cuidamos el planeta"
        },
        {
            "pregunta":"7) ¿QUE SIGNIFICA RECICLAR?",
            "opciones": ["A) Hacer objetos nuevos con algo viejo", "B) Tirar basura","C) Comprar productos nuevos"],
            "respuesta_correcta": "A",
            "mensaje":"Cuando reciclamos, evitamos que cosas como el plástico, el papel y el vidrio terminen en la basura o en el mar, donde pueden contaminar la tierra y el agua. Reciclando, mantenemos el planeta más limpio, como si estuviéramos limpiando nuestra habitación"
        },
        {
            "pregunta":"8) ¿CUALES DE ESTOS ANIMALES VIVE EN  EL AGUA Y ESTA EN PELIGRO DE EXTINCION ?",
            "opciones": ["A) Leon", "B) Tortuga marina","C) Elefante ", "D) Cebra"],
            "respuesta_correcta": "B",
            "mensaje":"Si cuidamos el ambiente, podemos salvar muchas tortugas marinas. Al mantener el mar limpio de plásticos, cuidar las playas y luchar contra el cambio climático, ayudamos a que las tortugas sigan viviendo felices y a que más bebés tortugas nazcan y crezcan sanos."
        },
        {
            "pregunta":"9) ¿POR QUE ES IMPOTANTE CUIDAR EL AGUA?",
            "opciones": ["A) Porque es ilimitada", "B) No necesitamos agua ","C)Es un recurso que debemos cuidar  ", "D) Es solo para beber"],
            "respuesta_correcta": "C",
            "mensaje":"Debemos ahorrar agua porque es un recurso limitado y si no la cuidamos, puede faltar en el futuro. Ahorrando agua, ayudamos a los animales, las plantas, el medioambiente y hasta a nosotros mismos"
        },
        {
            "pregunta":"10) ¿COMO PODEMOS PROTEGER LA FAUNA DEL PLANETA?",
            "opciones": ["A) No destruir bosques y selvas", "B) No contaminar","C) Reducir la caza de animales  ", "D) Todas son correctas"],
            "respuesta_correcta": "D",
            "mensaje":"Debemos proteger a los animales porque son esenciales para el equilibrio de la Tierra, porque nos ayudan de muchas maneras y porque merecen vivir felices y seguros en su hogar. Si cuidamos a los animales, estamos cuidando nuestro planeta y asegurándonos de que todo siga funcionando bien para todos"
        }


    ]


    def guardianes_del_planeta():
        total_puntos=0
        for pregunta in preguntas_y_respuestas:
            print(pregunta["pregunta"])

            for opcion in pregunta["opciones"]:
                    print(opcion)
            
            respuesta_nino = input("Elige una opción (A, B, C, D): ")
            print()

            if respuesta_nino.upper() == pregunta["respuesta_correcta"]:
                print("Correcto")
                total_puntos=total_puntos+1
            else:
                print(f"Incorrecto. Debiste haber puesto la opcion: {pregunta['respuesta_correcta']}.")
            print()       
            print(pregunta['mensaje'])
            print()

        print("El total de puntos es: ",total_puntos)
        if total_puntos>=6 and total_puntos<8:
            print("Bueno")
        elif total_puntos>=8 and total_puntos<10:
            print("muy bueno")
        elif total_puntos==10:
            print ("Felicidades, sos un GUARDIAN DEL PLANETA estupendo ")
        else:
            print(":( ")

        opcion = input("¿Te gustaria jugar una vez mas? (SI/NO): ")
        if opcion.upper() == "SI":
            guardianes_del_planeta()
        else:
            if opcion.upper() == "NO":
                print("Muchas gracias por jugar a Guardianes del planeta :D")
            
        

    guardianes_del_planeta()
            
    

