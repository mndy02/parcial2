'''Escriba un programa que, al recibir como dato un número entero positivo N, calcule el resultado de la siguiente serie:
1 + (1/2) + (1/3) + (1/4) + ... + (1/N) donde N es el número que el usuario ingresa
Si el usuario escribe un número incorrecto, el programa no se ejecuta. En cambio, pregunta de nuevo por la información hasta que el dato ingresado sea correcto.'''

print("BIENVENIDO AL PROGRAMA\n")

while True:
    try:
        n = int(input("Ingresa un número positivo: "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print("Por favor ingresa un número positivo válido.")

suma = 0
for i in range(1, n+1):
    suma += 1/i

print("La suma de la serie es:", suma)

print("\nFIN DEL PROGRAMA") 

