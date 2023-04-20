'''Escribe un programa que, al recibir como dato un número entero positivo N, calcule el resultado de la siguiente serie:
1 + (1/2) + (1/3) + (1/4) + ... + (1/N) donde N es el número que el usuario ingrese
Si el usuario escribe un número incorrecto, el programa no se ejecuta. En cambio, pregunta de nuevo por la información hasta que el dato ingresado sea correcto.'''

print("BIENVENIDO AL PROGRAMA\n")

while True:
    try:
        num = int(input("Ingrese un número positivo: "))
        if num <= 0:
            raise ValueError
            break
        except ValueError
        print("Por favor ingrese un número positivo válido: ") 

suma = 0
 for i in range (1, num + 1):
            suma += 1/

 print("El resultado de la suma de la serie es: ", suma)

print("\nFIN DEL PROGRAMA")
