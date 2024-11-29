import random

attempts = 0
max_attempts = 10
code_length = 4 
numbers = list(range(10))

# Generar código aleatorio
code = random.sample(numbers, code_length)

print(code)

print("Bienvenido a CODE CRACKER MASTERMIND GAME")
print("Números posibles del 0 al 9, ¡no se pueden repetir!")



# Verificar longitud, existencia en la lista válida y ausencia de duplicados
while attempts < max_attempts:
    try:
        guess = input(f"Intento {attempts + 1}. Ingresa tu intento: ").strip()
        
            # Convertir los elementos de guess a enteros
        guess = [int(num) for num in guess]

            # Verificar que el intento sea válido
        if (
            len(guess) != code_length or 
            not all(num in numbers for num in guess) or 
            len(set(guess)) != len(guess)
            ):
                print("Intento inválido, asegúrate de que tienes exactamente 4 dígitos únicos del 0 al 9, que no se repitan (Ej:1234)")
                continue
    
    except ValueError:
        print("Entrada invalida, solo numeros del 0 al 9!")
        continue


    # Calcular fijas y picas
    fijas = sum(a == b for a, b in zip(guess, code))
    picas = len(set(guess) & set(code)) - fijas

    print(f"{fijas} fijas, es decir tienes {fijas} números en su posición correcta.")
    print(f"{picas} picas, es decir tienes {picas} números en su posición incorrecta.")
    
    if fijas == code_length:
        print("¡CODE CRACKED! ¡Felicidades, HAS GANADO!")
        exit()
        
    attempts += 1     

print("Has perdido :(")
