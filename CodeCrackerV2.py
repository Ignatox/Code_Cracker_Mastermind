import random

# Función para generar un código secreto
def generar_codigo():
    return random.sample(range(10), 4)


# Función para calcular picas y fijas
def calcular_picas_y_fijas(intentado, secreto):
    #Agrupa los valores de cada posicion en intentado y secreto y suma 1 si son iguales
    fijas = sum(a == b for a, b in zip(intentado, secreto))
    #Setea la longitud de la cantidad de numeros que coinciden de ambos codigos y le resta la cantidad de fijas
    picas = len(set(intentado) & set(secreto)) - fijas
    return picas, fijas

# Modo fácil: IA hace intentos aleatorios
def ia_facil(intentos_previos):
    while True:
        intento = random.sample(range(10), 4)
        if intento not in intentos_previos:
            return intento

# Modo difícil: IA usa probabilidades basadas en pistas
def ia_dificil(intentos_previos, respuestas_previas, code_length=4):
    # Diccionarios para rastrear posibles dígitos por posición
    posibles_por_posicion = [set(range(10)) for _ in range(code_length)]
    fijas_confirmadas = [None] * code_length
    descartados_globales = set()
    

    # Procesar las respuestas previas para refinar posibilidades
    for intento, (picas, fijas) in zip(intentos_previos, respuestas_previas):
        for idx, num in enumerate(intento):
            # Si ya hay una fija confirmada en esta posición, no modificar
            if fijas_confirmadas[idx] is not None:
                continue
            
            # Si el número es incorrecto para la posición actual, descartarlo
            if intento.count(num) > 1 or (fijas == 0 and num in intento):
                posibles_por_posicion[idx].discard(num)
                descartados_globales.add(num)
                print(f"Descartados globales: {descartados_globales}")
            elif fijas > 0:  # Fijas indican posibles valores para esta posición
                posibles_por_posicion[idx].add(num)
                print(f"posibles por posicion {posibles_por_posicion}")
            
        # Confirmar valores que son definitivamente "fijos" en ciertas posiciones
        for i in range(code_length):
            if len(posibles_por_posicion[i]) == 1:
                fijas_confirmadas[i] = list(posibles_por_posicion[i])[0]
                print(f"Fijas confirmadas {fijas_confirmadas}")

    # Generar nuevo intento basándose en posibilidades refinadas
    while True:
        intento = [
            fijas_confirmadas[i] if fijas_confirmadas[i] is not None
            else random.choice(list(posibles_por_posicion[i]))
            for i in range(code_length)
        ]
        
        
        
        # Verificar que el intento sea único y válido
        if intento not in intentos_previos and len(set(intento)) == code_length:
            return intento


# Turno del jugador
def turno_jugador():
   while True:
        try:
            entrada = input("\nIngresa tu intento (4 dígitos únicos o escribe 'EXIT' para salir): ").strip()
            if entrada.upper() == "EXIT":
                print("Saliendo del juego. ¡Gracias por jugar!")
                exit()  # Finaliza el programa
            
            # Convierte la entrada a una lista de números
            codigo = list(map(int, entrada))
            
            # Valida que sean 4 dígitos únicos
            if len(codigo) == 4 and len(set(codigo)) == 4:
                return codigo
            else:
                print("Código inválido. Asegúrate de ingresar 4 dígitos únicos.")
        except ValueError:
            print("Entrada inválida. Ingresa solo números o escribe 'EXIT' para salir.")

# Validación para el código del jugador
# Validación para el código del jugador
def ingresar_codigo_secreto():
    while True:
        try:
            entrada = input("Ingresa tu código secreto (4 dígitos únicos o escribe 'EXIT' para salir): ").strip()
            
            if entrada.upper() == "EXIT":
                print("Saliendo del juego. ¡Gracias por jugar!")
                exit()  # Finaliza el programa
            
            # Convierte la entrada a una lista de números
            codigo = list(map(int, entrada))
            
            # Valida que sean 4 dígitos únicos
            if len(codigo) == 4 and len(set(codigo)) == 4:
                return codigo
            else:
                print("Código inválido. Asegúrate de ingresar 4 dígitos únicos.")
        except ValueError:
            print("Entrada inválida. Ingresa solo números o escribe 'EXIT' para salir.")


# Juego principal
def jugar():
    print("¡Bienvenido a Code Cracker!")  
    codigo_ia = generar_codigo()
    ##PARA TEST
    #print(f"¡El juego comienza! La IA ha generado su código secreto: {codigo_ia}")
    print("El juego comienza! La IA ha generado su código secreto!")
    
    #Input con manejo de errores de codigo de jugador
    codigo_jugador = ingresar_codigo_secreto()
    
    print(f"El código que la IA debe adivinar es:{codigo_jugador}")
    
    
    intentos_ia = []
    respuestas_ia = []
    turno = 0  # Alternar entre jugador (0) y IA (1)

        
    
    while True:
        if turno == 0:  # Turno del jugador
            print("\nTu turno:")
            intento = turno_jugador()
            picas, fijas = calcular_picas_y_fijas(intento, codigo_ia)
            print(f"Resultado: {picas} Picas, {fijas} Fijas")
            if fijas == 4:
                print("¡Felicidades! Has adivinado el código de la IA.")
                break
        else:  # Turno de la IA
            print("\nTurno de la IA:")
            print(f"Intentos previos: {intentos_ia}")
            print(f"Respuestas previas: {respuestas_ia}")
            intento = ia_dificil(intentos_ia, respuestas_ia)  # Cambiar a ia_medio/ia_dificil según nivel
            intentos_ia.append(intento)
            picas, fijas = calcular_picas_y_fijas(intento, codigo_jugador)
            respuestas_ia.append((picas,fijas))
            #respuestas_ia.append((intento, (picas, fijas)))
            print(f"Segun tu codigo: {codigo_jugador}")
            print(f"La IA intentó: {intento} → {picas} Picas, {fijas} Fijas")
            if fijas == 4:
                print("¡La IA adivinó tu código! Mejor suerte la próxima vez.")
                break
        
        turno = 1 - turno  # Alternar turno

# Iniciar el juego
if __name__ == "__main__":
    jugar()
