class Persona:
    especie = "Humano"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        return f"hola, soy {self.nombre} y tengo {self.edad} años"
    
    def __str__(self):
        return f"{self.nombre}, {self.edad}"

class Empleado (Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre,edad)
        self.salario = salario

    def presentar(self):
        return f"hola, soy {self.nombre} y gano {self.salario}"
    

persona1 = Persona("Jessica", 33)
empleado1 = Empleado("Roberto", 45, 3000)


print(persona1.presentar())
print(empleado1.presentar())
print(persona1)
print(empleado1)