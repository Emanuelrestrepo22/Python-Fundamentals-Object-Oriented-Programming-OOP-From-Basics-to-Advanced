# creamos la clase CuentaBancaria
class CuentaBancaria:
    # inicializamos
    def __init__(self,numero,nombre):
        self.cuenta = numero
        self.titular = nombre
        self.saldo = 0

    # función para depositar dinero en la cuenta bancaria.
    def depositar(self,monto):
        if monto > 0:
            self.saldo = self.saldo + monto
 
    # función para extraer dinero de la cuenta bancaria.  El saldo de la cuenta puede quedar en negativo.
    def extraer(self,monto):
        self.saldo = self.saldo - monto

    # función para hacer una transferencia bancaria a otra cuenta
    def transferencia(self, cuenta_destino, monto):
        if self.saldo >= monto:
            self.saldo = self.saldo - monto
            cuenta_destino.saldo = cuenta_destino.saldo + monto
            print("Transferencia ok!")
        else:
          print("No se puede efectuar la transaccion")

    # función para obtener estado de la cuenta bancaria
    def estadoCuenta(self):
        if self.saldo >= 0:
            print("Su saldo es acreedor")
        else:
            print("Su saldo es deudor")
        
    # función para imprimir los datos del cliente
    def imprimirDatos(self):
        print(f"{self.titular}, titular de la cuenta {self.cuenta}, tiene un saldo de ${self.saldo}")

# programa principal
print()
cuenta1=CuentaBancaria(123,"Juan Perez")
cuenta2=CuentaBancaria(456,"Roberto Gómez")

cuenta1.depositar(1000)
cuenta1.extraer(1250)
cuenta1.imprimirDatos()
cuenta1.estadoCuenta()
print()
cuenta2.depositar(3500)
cuenta2.extraer(1800)
cuenta2.imprimirDatos()
cuenta2.estadoCuenta()
print()
cuenta2.transferencia(cuenta1,600)
cuenta1.imprimirDatos()
cuenta1.estadoCuenta()
cuenta2.imprimirDatos()
cuenta2.estadoCuenta()


