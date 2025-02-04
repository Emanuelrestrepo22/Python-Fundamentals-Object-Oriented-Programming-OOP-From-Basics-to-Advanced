def sumaDivPropios(n):
    resultado = 0
    for i in range(1, n):
        if n % i == 0:
            resultado += i
    return resultado

print (sumaDivPropios(8))

def tipoNumero(n):
    suma = sumaDivPropios(n)
    if suma < n:
        resultado = "Defectuoso"
    elif suma > n:
        resultado = "Abundante"
    else:
        resultado = "perfecto"

#algoritmo principal
num = int(input("Ingrese un numero entero: "))
print(f"El numero {num} es {tipoNumero(num)}")