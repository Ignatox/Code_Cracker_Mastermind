class EstadoIA:
    def __init__(self, posibles_por_posicion, fijas_confirmadas, picas_confirmadas):
        #Inicializa el estado global de la lógica de la IA
        #posibles por posicion: Lista de conjuntos, con los números posibles por posición
        #fijas confirmadas: Lista que mantiene las fijas confirmadas en las 4 posiciones posibles
        #picas cconfirmadas: lista de palabras que estane nla palabra pero aun con posicion desconocida
        
        self.posibles_por_posicion = posibles_por_posicion
        self.fijas_confirmadas = fijas_confirmadas
        self.picas_confirmadas = picas_confirmadas
        
    def __str__(self):
        return (f"Posibles por posición: {self.posibles_por_posicion}\n"
                f"Fijas confirmadas: {self.fijas_confirmadas}\n"
                f"Picas confirmadas: {self.picas_confirmadas}")
            
