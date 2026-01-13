class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo} euros")

cuenta = CuentaBancaria("Carlos", 1500)
cuenta.mostrar_saldo()