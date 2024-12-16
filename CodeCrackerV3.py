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

def ia_dificil(intentos_previos, respuestas_previas, nro_intento, code_length=4):
    # Diccionario de datos para proximos intentos
    #Ver forma de persistir entre intentos como va quedando ese diccionario
    # numeros_posibles= list(range(10))
    posibles_por_posicion = [set(range(10)) for _ in range(code_length)]
    fijas_confirmadas = [None] * code_length
    descartados_globales = set()
    descartados_por_posicion = [set() for _ in range(code_length)]  # Lista de 4 conjuntos para descartados por posición
    
    for intento, (picas, fijas) in zip(intentos_previos, respuestas_previas):
        for idx, num in enumerate(intento):
            # Si ya hay una fija confirmada , no modificar
            if fijas_confirmadas[idx] is not None:
                continue
            
            #Si el numero no esta en la palabra lo descarto
            if fijas == 0 and picas == 0:
                for i in range(code_length):
                    if num in posibles_por_posicion[i]:
                        posibles_por_posicion[i].discard(num) ##Eliminar de posibles por pos.
                    descartados_por_posicion[i].add(num) ##Agregar a descartados por pos.
                    descartados_globales.add(num) #Agregar a numeros descartados de todas las pos.
            elif fijas > 0 or picas > 0:
                #Si hay fijas o picas se agrega como posible en la posicion actual
                if num not in posibles_por_posicion[idx]:
                    posibles_por_posicion[idx].add(num)
                    print(f"Posibles por posicion {posibles_por_posicion}")
                    
#Confirmar valores definitivamente fijos                    
    for i in range(code_length):
        if len(posibles_por_posicion[i]) == 1:
            #Obtengo el valor del posible fijo de esta posicion
            num_fijo = list(posibles_por_posicion[i])[0]
            print(f"Numero fijo encontrado: {num_fijo}")
            
            #Verificar que no este descartado en otras posiciones
            descartado_en_otras = all(num_fijo in descartados_por_posicion[j] for j in range(code_length) if j != i)
            if descartado_en_otras:
                fijas_confirmadas[i] = num_fijo
                print(f"Fijas confirmadas: {fijas_confirmadas}")
     
    #while True:
    if(nro_intento == 1):
        primer_intento = random.sample(range(10),4)
        if len(set(primer_intento)) == code_length:
            print(f"Primer intento: {primer_intento}")
        return primer_intento
    else: 
        siguiente_intento = []
        for i in range(code_length):
            if fijas_confirmadas[i] is not None:
                siguiente_intento.append(fijas_confirmadas[i])
            else:
                if not posibles_por_posicion[i]: 
                    posibles = [num for num in range(10) if num not in descartados_globales and num not in descartados_por_posicion[i]]
                    num_elegido = random.choice(posibles)
                    siguiente_intento.append(num_elegido)
                else:
                    num_elegido = random.choice(list(posibles_por_posicion[i]))
                    siguiente_intento.append(num_elegido)
                    # Verificar que no haya repetidos
    while len(set(siguiente_intento)) < code_length:
                # Si hay repetidos, regenerar el intento
        siguiente_intento = []
        for i in range(code_length):
            if fijas_confirmadas[i] is not None:
                siguiente_intento.append(fijas_confirmadas[i])
            else:
                if not posibles_por_posicion[i]:
                    posibles = [num for num in range(10) if num not in descartados_globales and num not in descartados_por_posicion[i]]
                    num_elegido = random.choice(posibles)
                    siguiente_intento.append(num_elegido)
                else:
                    num_elegido = random.choice(list(posibles_por_posicion[i]))
                    siguiente_intento.append(num_elegido)           
    print(f"Siguiente intento: {siguiente_intento}")        
    return siguiente_intento
        
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
    nro_intento = 0 #Nro de intento para IA

        
    
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
            nro_intento += 1
            print("\nTurno de la IA:")
            print(f"Intentos previos IA: {intentos_ia}")
            print(f"Respuestas previas IA: {respuestas_ia}")
            intento = ia_dificil(intentos_ia, respuestas_ia, nro_intento)  # Cambiar a ia_medio/ia_dificil según nivel
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
