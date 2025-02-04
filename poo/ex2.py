class Persona:
    #inicializamos nuestros atributos
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #imprimos los datos
    def imprimir (self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)

    #comprobamos si es mayor de edad o no
    def mayor_edad(self):
        if self.edad >= 18:
            print(f"El usuario {self.nombre}, es mayor de edad")
        else:
            print(f"El usuario {self.nombre} es menor de edad")


#bloque principal
persona1 = Persona()
persona1.inicializar("luis", 30)

persona2 = Persona()
persona2.inicializar("Irupe", 27)

#imprimimos y comprobamos si es mayor de edad
print(persona1.imprimir())
print(persona1.mayor_edad())

print(persona2.imprimir())
print(persona2.mayor_edad())