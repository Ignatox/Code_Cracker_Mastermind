import random

# Función para generar un código secreto
def generar_codigo():
    return random.sample(range(10), 4)


# Función para calcular picas y fijas
def calcular_picas_y_fijas(intentado, secreto):
    fijas = sum(a == b for a, b in zip(intentado, secreto))
    picas = len(set(intentado) & set(secreto)) - fijas
    return picas, fijas

# Modo fácil: IA hace intentos aleatorios
def ia_facil(intentos_previos):
    while True:
        intento = random.sample(range(10), 4)
        if intento not in intentos_previos:
            return intento

# Modo medio: IA reduce posibilidades según pistas
def ia_medio(intentos_previos, respuestas_previas):
    # Simplificado: refinar el algoritmo según pistas
    return ia_facil(intentos_previos)  # Placeholder

# Turno del jugador
def turno_jugador(codigo_ia):
    while True:
        try:
            intento = list(map(int, input("Introduce tu intento (4 dígitos únicos): ")))
            if len(intento) == 4 and len(set(intento)) == 4:
                break
            else:
                print("Entrada inválida. Asegúrate de ingresar 4 dígitos únicos.")
        except ValueError:
            print("Entrada inválida. Ingresa solo números.")
    return intento

# Juego principal
def jugar():
    print("¡Bienvenido a Code Cracker!")  
    codigo_ia = generar_codigo()
    codigo_jugador = list(map(int,input("Ingresa tu codigo secreto:")))
    ##codigo_jugador = generar_codigo()
    print(f"el numero que debera adivinar la IA es:{codigo_jugador}")
    print("¡El juego comienza! La IA ha generado su código secreto.")
    
    intentos_ia = []
    respuestas_ia = []
    turno = 0  # Alternar entre jugador (0) y IA (1)

        
    
    while True:
        if turno == 0:  # Turno del jugador
            print("\nTu turno:")
            intento = turno_jugador(codigo_ia)
            picas, fijas = calcular_picas_y_fijas(intento, codigo_ia)
            print(f"Resultado: {picas} Picas, {fijas} Fijas")
            if fijas == 4:
                print("¡Felicidades! Has adivinado el código de la IA.")
                break
        else:  # Turno de la IA
            print("\nTurno de la IA:")
            intento = ia_facil(intentos_ia)  # Cambiar a ia_medio/ia_dificil según nivel
            intentos_ia.append(intento)
            picas, fijas = calcular_picas_y_fijas(intento, codigo_jugador)
            respuestas_ia.append((intento, (picas, fijas)))
            print(f"Segun tu codigo: {codigo_jugador}")
            print(f"La IA intentó: {intento} → {picas} Picas, {fijas} Fijas")
            if fijas == 4:
                print("¡La IA adivinó tu código! Mejor suerte la próxima vez.")
                break
        
        turno = 1 - turno  # Alternar turno

# Iniciar el juego
if __name__ == "__main__":
    jugar()
