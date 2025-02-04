def tipoTriangulo(a,b,c):
    if a + b <= c or a + c <= b or c + b <= a:
        resultado = "Es un triangulo invalido"
    elif a == b == c:
        resultado = "Triangulo Equilatero"
    elif a == b or b == c or a == c:
        resultado = "Este es un triangulo Isosceles"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        resultado = "Triangulo Rectangulo"
    else: 
        resultado = "Triangulo Escaleno"
    return resultado

print("A continuacion pediremos valores de 3 medidas de trangulos para determinar si el triangulo es valido, y que tipo de triangulo es")
a = float(input("Ingrese medidas de la primera cara del triangulo a determinar"))
b = float(input("Ingrese medidas de la segundo lado"))
c = float(input("Ingrese medidas del ultimo lado"))
triangulo = tipoTriangulo(a,b,c)
print(f"los datos suministrados corresponden a {triangulo} ")