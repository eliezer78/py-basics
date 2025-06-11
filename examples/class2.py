class CuentaBancaria:
    def __init__(self, cliente, tipo, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado
        self._tipo = tipo # Atributo protegido
        self.cliente = cliente # Atributo público
        
    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            return True
        return False

    def obtener_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria("Lopez", "CC", 1000)
cuenta.depositar(500)
print(cuenta.obtener_saldo()) # 1500
cuenta.retirar(300)
print(cuenta.obtener_saldo()) # 1200

# No se puede acceder directamente al saldo:
# print(cuenta.__saldo)  # Error: AttributeError