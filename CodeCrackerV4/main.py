from ia_dificil import ia_dificil
from estado_ia import EstadoIA
from actualizar_estado import actualizar_estado
import random

#Inicializar estado
# posibles por posicion = [[0..9],[0..9],[0..9],[0..9]]
# fijas confirmadas = [None, None, None, None]
estado = EstadoIA(
    posibles_por_posicion=[set(range(10)) for _ in range(4)],
    fijas_confirmadas = [None] * 4,
    picas_confirmadas = []
)

# Función para generar un código secreto
def generar_codigo():
    return random.sample(range(10), 4)

#Calcular respuesta
def calcular_respuesta(intentado, secreto):
     #Agrupa los valores de cada posicion en intentado y secreto y suma 1 si son iguales
    fijas = sum(a == b for a, b in zip(intentado, secreto))
    #Setea la longitud de la cantidad de numeros que coinciden de ambos codigos y le resta la cantidad de fijas
    picas = len(set(intentado) & set(secreto)) - fijas
    return picas, fijas

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
    #Simular intento
    intentos_previos = []
    respuestas_previas = []
    turno = 0
    nro_intento = 0
    codigo_ia = generar_codigo()
    print("El juego comienza! La IA ha generado su secret code!")
    
    codigo_jugador = ingresar_codigo_secreto()
    
    print(f"El código que la IA debe adivinar es:{codigo_jugador}")

    #Bucle principal
    while True:
        print("\n" + "="*20)
        if turno == 0:
            print("\nTu turno:")
            intento = turno_jugador()
            picas, fijas = calcular_respuesta(intento, codigo_ia)
            print(f"Resultado: {picas} Picas, {fijas} Fijas")
            if fijas == 4:
                print("¡Felicidades! Has adivinado el código de la IA.")
                break
        else: 
            nro_intento += 1
            print("Turno de la IA:")
            intento_ia = ia_dificil(intentos_previos, respuestas_previas, nro_intento, estado)
            picas, fijas = calcular_respuesta(intento_ia, codigo_jugador)
            intentos_previos.append(intento_ia)
            respuestas_previas.append((picas, fijas))
            print(f"La IA intentó: {intento_ia} → {picas} Picas, {fijas} Fijas")
            actualizar_estado(estado, intento_ia, picas, fijas)
            
            if fijas == 4:
                print(f"¡La IA adivinó tu código en {nro_intento} intentos! Mejor suerte la próxima vez.")
                break
            
        turno = 1 - turno #Alternar turno
 

 
#Iniciar el juego
if __name__ == "__main__":
    jugar()   
        
