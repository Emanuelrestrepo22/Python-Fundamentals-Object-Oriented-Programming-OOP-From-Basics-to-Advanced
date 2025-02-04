class CuentaBancaria:
    def __init__(self, nombreTitular, numeroCuenta, saldo):
        self.nombreTitular = nombreTitular
        self.numeroCuenta = numeroCuenta
        self._saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
    
    def retirar(self, cantidad):
        if self._saldo <= 0:
            print("Saldo insuficiente para realizar esta operacion")
        else:
            self._saldo -= cantidad
    
    def consultarSaldo(self):
        return f"Tiene un saldo de {self._saldo}"
    
cuenta1 = CuentaBancaria("maria", 1111, 500)

print(cuenta1.consultarSaldo())
cuenta1.depositar(1000)
cuenta1.retirar(900)
print(cuenta1.consultarSaldo())