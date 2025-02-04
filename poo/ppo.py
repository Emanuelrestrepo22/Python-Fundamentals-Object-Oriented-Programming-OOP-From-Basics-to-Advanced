class Alumno:

    #metodo para inicializar atributos de cada alumno
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    #metodo para imprimir los datos del alumno
    def imprimir(self):
        print("nombre: ", self.nombre)
        print("nota: ", self.nota)

    def resultado(self):
        if self.nota < 5:
            print(f"El alumno, {self.nombre} debe recuperar")
        else:
            print(f"El alumno {self.nombre} aprobo con nota {self.nota}")

#crear instancias del alumno
alumno1 = Alumno()
alumno2 = Alumno()

#inicializar y mostar datos de cada alumno
alumno1.inicializar("Eduardo", 9)
alumno2.inicializar("Jessica", 4)

alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()