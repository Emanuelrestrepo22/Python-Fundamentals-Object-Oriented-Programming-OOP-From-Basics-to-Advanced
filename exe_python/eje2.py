#definimos la funcion
def contarNumerosComoCadena(n):
    cadena = str(n)
    suma = 0
    for caracter in cadena:
        suma += int(caracter)
    return suma
    
#solicitar numero al usuario
numero = int(input("Inserte numero desea hacer la sumatoria de digitos: "))
resultado = contarNumerosComoCadena(numero)
# hacer llamdo de nuestra funcion e imprimir 
print("la suma de cada uno de los digitos como cadena es: ", resultado)