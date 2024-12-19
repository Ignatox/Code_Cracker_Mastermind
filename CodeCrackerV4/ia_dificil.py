import random
def ia_dificil(intentos_previos, respuestas_previas, nro_intento, estado):
    #Logica para determinar el proximo intento de la IA.
    #intentos_previos: lista de intentos anteriores
    #respuestas_previas: Lista de respuestas anteriores asociadas a los intentos (picas y fijas)
    #nro_intento: Número del intento actual.
    #estado: Instancia de EstadoIA que contiene el estado persistente
    #return: El siguiente intento como una lista de 4 números no repetidos del 0 al 9.
    
    print(f"Intento {nro_intento}: Pensando...")
    print(f"Estado actual:\n{estado}")
    
    #Construir el proximo intento basado en el estado actual
    if nro_intento == 1:
        intento = random.sample(range(10),4)
        return intento
    else:
        intento = []
        
        for i, posibles in enumerate(estado.posibles_por_posicion):
            if estado.fijas_confirmadas[i] is not None:
                intento.append(estado.fijas_confirmadas[i]) #Uso de la fija que ya esta confirmada en la posicion i
            else: 
                if posibles:
                    intento.append(random.choice(list(posibles)))
                else:
                    raise ValueError(f"No hay valores posibles para la posicion {i}, verifique la logica del mismo")
        
        print(f"Nuevo intento generado:{intento}")
        return intento