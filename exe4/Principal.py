from Funciones import *

# Solicitar el primer número primo al usuario
numero = int(input("Ingrese un número primo: "))

# Verificar si el primer número es primo antes de proceder
if primo(numero):
    while primo(numero):
        print(f"La suma de los dígitos de {numero} es: {sumaDigitos(numero)}")

        digito = int(input("Ingrese un dígito: "))

        print(f"El dígito {digito} aparece {frecuencia(numero, digito)} veces en el número {numero}.")

        # Verificar y actualizar el mayor número primo ingresado
        if mayor is None or numero > mayor:
            mayor = numero

        numero = int(input("Ingrese otro número primo (o un número que no sea primo para terminar): "))

    # Al finalizar, mostrar el factorial del mayor número primo ingresado
    print(f"El factorial del mayor número ingresado ({mayor}) es: {factorial(mayor)}")
else:
    print("No se ingresó ningún número primo.")




















