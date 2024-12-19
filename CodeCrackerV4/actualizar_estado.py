def actualizar_estado(estado, intento, picas, fijas):
    #Actualiza el estado de la IA basado en las respuestas de picas y fijas.
    #estado_ Instancia de estadoIA que contiene el estado actual.
    #intento: Lista de numeros del ultimo intento
    #picas: numero de picas obtenidas, es decir numeros presentes pero en pos. incorrecta
    #fijas: numero de fijas obtenidas, es decir numeros presentes y en posicion correcta.
    
    # Crear un conjunto de los numeros del intento actual
    numeros_intento = set(intento)
    print(f"Numeros intento {numeros_intento}")
    
    #Caso 1: 0 picas y 0 fijas -> se elminan todos los numeros intentados en todas las posiciones posibles
    if picas == 0 and fijas == 0:
        for i in range(4):
            estado.posibles_por_posicion[i] -= numeros_intento
            print(f"Descartados los numeros {numeros_intento} de todas las posiciones")
        return
            
    #Caso 1.5: 0 fijas y picas ==4 se elimina la posiblidad del numero en la posicion en la que se encuentra
    if picas == 4 and fijas == 0:
        for i, numero in enumerate(intento):
            estado.picas_confirmadas = intento
            estado.posibles_por_posicion[i] = numeros_intento - numero ##Cuando hay 4 picas significa que los 4 numeros estan presentes
            print(f"Ya tengo los numeros, estoy a un paso! {estado.posibles_por_posicion}")
            
    #Caso: Fijas 0 y picas mayor a 1 
    
    
    
    #Caso 2: Hay fijas -> Restringir posibles pero mantener abiertas las posiciones
    for i, numero in enumerate(intento):
        if estado.fijas_confirmadas[i] is None and numero in numeros_intento:
            #Confirmar si este numero debe ser fijo en la posicion
            if sum(1 for j in range(4) if numero in estado.posibles_por_posicion[j]) == 1:
                estado.fijas_confirmadas[i] = numero
                estado.posibles_por_posicion = {numero}

    #Caso 3: Manejo de picas
    for i, posibles in enumerate(estado.posibles_por_posicion):
        if estado.fijas_confirmadas[i] is None: #Solo restringir si la posicion no esta confirmada
            #Mantener los numeros que podiran ser picas o que no han sido descartados
            estado.posibles_por_posicion[i] &= numeros_intento
            
    #Ajustar posibilidades segun restricciones de fijas y picas
    #Garantizar que los numeros intentados como picas se distribuyan correctamente
    for i, numero in enumerate(intento):
        if numero in numeros_intento and numero not in estado.fijas_confirmadas:
            for j in range(4):
                if j!=i and numero in estado.posibles_por_posicion[j]:
                    estado.posibles_por_posicion[j].add(numero)            
    

    print(f"Estado actualizado: {estado}")                
    