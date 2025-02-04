class Calculadora:

    #inicializamos metodo __init__
    def  __init__(self):
        self.valor1 = int(input("Ingrese primer valor"))
        self.valor2 = int(input("Ingrese segundo valor"))

    #funcion para sumar
    def sumar(self):
        suma = self.valor1 + self.valor2
        print(f"El resultado de la sema es {suma}")
            
    #funcion para restar
    def restar(self):
        restar = self.valor1 - self.valor2
        print(f"La resta de su operacion es: {restar}")

    #funcion para multiplicar
    def multiplicar(self):
        multiplicacion = self.valor1 * self.valor2
        print(f"El resultado de su multiplicacion es {multiplicacion}")

    #funcion para dividir
    def dividir(self):
        if self.valor2 != 0:
            div = self.valor1 / self.valor2
            print(f"El resultado de la dicision es {div}")
        else:
            print("No se puede dividir por 0")

    #funcion para imprimir
    def imprimir(self):
        print("los valores son:")
        print(f"Valor 1: {self.valor1}")
        print(f"Valor 2: {self.valor2}")

#bloque principal
calcular = Calculadora()
calcular.imprimir()
calcular.restar()
calcular.sumar()
calcular.dividir()
calcular.multiplicar()
    