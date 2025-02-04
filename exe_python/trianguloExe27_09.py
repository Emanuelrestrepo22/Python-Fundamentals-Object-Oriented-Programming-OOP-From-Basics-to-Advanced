# Validación de si es un triángulo válido
def validarTriangulo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True

# Determinar el lado mayor del triángulo
def mayorLado(a, b, c):
    if a > b and a > c:
        mayor = a
    elif b > c:
        mayor = b
    else:
        mayor = c
    return mayor

# Determinar el tipo de triángulo
def tipoTriangulo(a, b, c):
    if a == b == c:
        resultado = "Triángulo Equilátero"
    elif a == b or b == c or a == c:
        resultado = "Triángulo Isósceles"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        resultado = "Triángulo Rectángulo"
    else:
        resultado = "Triángulo Escaleno"
    return resultado

# Algoritmo principal
print("A continuación, ingrese las medidas de los tres lados del triángulo para determinar si es válido y su tipo.")
while True:
    # Pedir datos al usuario
    a = float(input("Ingrese la medida del primer lado: "))
    b = float(input("Ingrese la medida del segundo lado: "))
    c = float(input("Ingrese la medida del tercer lado: "))

    # Salir del bucle si todos los lados son 0
    if a == 0 and b == 0 and c == 0:
        print("Cerrando el programa.")
        break

    # Validar si los valores ingresados forman un triángulo
    if validarTriangulo(a, b, c):
        triangulo = tipoTriangulo(a, b, c)
        print(f"Los datos suministrados corresponden a un {triangulo}.")
    else:
        print("Los lados ingresados no forman un triángulo válido.")






