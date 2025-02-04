class triangulo:

    #inicializamos
    def inicializar(self):
        self.lado1 = int(input("ingrese valor del primer lado"))
        self.lado2 = int(input("inserte valor del segundo lado"))
        self.lado3 = int(input("Ingrese el valor del tercer lado"))

    #imprimimos
    def imprimir(self):
        print("Los lados del triangulo tienen el valor de: ")
        print(f"Lado 1: {self.lado1}")
        print(f"Lado 2: {self.lado2}")
        print(f"Lado 3: {self.lado3}")


    def valido(self):
        if self.lado1 + self.lado2 <= self.lado3 or self.lado1 + self.lado3 <= self.lado2 or self.lado2 + self.lado2 + self.lado3 <= self.lado1:
            print("no es un triangulo valido")

    #comprobamos el lado mayor
    def mayor(self):
        print("El lado mayor es: ")
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(f"lado 1: {self.lado1}")
        elif self.lado2 > self.lado3:
            print(f"lado 2: {self.lado2}")
        else:
            print(f"lado 3: {self.lado3}")

#comprobamos tipo de triangulo
    def tipoTriangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("Es un triangulo equilatero")
        elif self.lado1 != self.lado2 and self.lado1 != self.lado3 and self.lado2 != self.lado3:
            print("Es un triangulo escaleno")
        else:
            print("Es un triangulo isosceles")