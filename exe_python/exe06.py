def cantidadOcurrencias(num, n):
    cont = 0
    while num != 0:
        temp = num % 10
        if temp == n:
            cont += 1
        num = int(num / 10)
    return cont

numero = int(input("Ingrese un numero natural positiva de varios digitos"))
digito = int(input("Ingrese solo un digito"))

cantidad= cantidadOcurrencias(numero,digito)
if cantidad == 1:
    print(f"El {digito} se encuenta una vez")
else:
    print(f"El numero {digito} se encuentra {cantidad} veces")




