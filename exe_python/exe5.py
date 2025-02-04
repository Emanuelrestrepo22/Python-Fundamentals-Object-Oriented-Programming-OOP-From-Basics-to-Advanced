# Definimos la función para invertir el número
def numeros_invertidos(n):
    resultado = ""  # Inicializamos una cadena vacía para almacenar el resultado
    # Recorremos la cadena desde el último caracter hasta el primero
    for i in range(len(n) - 1, -1, -1):  # len(n) - 1 es el índice del último carácter, -1 es el final, -1 es el paso.
        resultado += n[i]  # Añadimos el carácter en la posición i al resultado
    return resultado

# Algoritmo principal
num = input("Ingrese un número para regresarlo invertido: ")
resultado = numeros_invertidos(num)
print(f"El número invertido es: {resultado}")
