def primo(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def frecuencia(n, digito):
    contador = 0 
    while n != 0:
        ultDigito = n % 10
        if ultDigito == digito:
            contador += 1
        n = n // 10
    return contador

def factorial(n):
    f=1
    for i in range(1,n+1):
        f= f*i
    return f

#Falta definir la función que devuelve la suma de los digitos de un número



def sumaDigitos(n):
    resultado = 0
    n= str(n)
    for i in range (len(n)):
        
        resultado += int(n[i])
    return resultado
print(sumaDigitos(123456))
    
    

















    
