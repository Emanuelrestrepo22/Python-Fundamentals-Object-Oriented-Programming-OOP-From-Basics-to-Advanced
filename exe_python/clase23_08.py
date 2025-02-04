def sumaDivPropios (n):
    suma=0
    for i in range(1,n):
        if n % i == 0:
            suma += i
    return suma

def tipoNumero(n):
    if sumaDivPropios(n) < n:
        result = "defectuoso"
    elif sumaDivPropios(n) == n:
        result = "Perfecto"
    else:
        result = " Abundante"
    return result

def verificaAmistad(n1, n2):
    if sumaDivPropios(n1)== n2 and sumaDivPropios(n2)==n1:
        resultado1 = True
    else:
        resultado1 = False
    return resultado1

numero = int(input("Ingrese un numero para saber si el mismo es perfecto, defectuoso o abundante: _____"))
resultado = tipoNumero(numero)
print(f"el numero {numero} es de tipo {resultado}")


N1 = int(input(" ingrese primer numero natural positivo para verificar amistad"))
N2= int(input("Ingrese segundo numero para verificar amistad"))
print(f"la suma de divisores propios de {N1} es {sumaDivPropios(N1)} ")
print(f"la suma de divisores propios de {N2} es {sumaDivPropios(N2)}")
if verificaAmistad(N1,N2):
    print("son amigos")
else:
    print("no son amigos")