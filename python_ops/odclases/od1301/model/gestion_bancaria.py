class CuentaBancaria:
    def __init__(self, saldo, nombre):
        """
        Docstring for __init__: Inicializa el objeto
        
        :param self: Apunta al propio objeto
        :param saldo: Salario inicial
        """
        self._saldo = saldo
        self._movimientos = []
        self._nombre = nombre

    def depositar(self, cantidad):
        """
        Docstring for depositar: Ingresa saldo a la cuenta
        
        :param self: Apunta al propio objeto
        :param cantidad: Cantidad que hay que depositar
        """
        self._saldo += cantidad
        self._movimientos.append({"Tipo": "Deposito", "Cantidad": cantidad})
        print(f"Has depositado {cantidad} euros.")

    def retirar(self, cantidad):
        """
        Docstring for retirar: Retira saldo de la cuenta 
        
        :param self: Apunta al propio objeto
        :param cantidad: Cantidad que hay que retirar
        """
        if cantidad > self._saldo:
            print("Fondos insuficientes.")
        else:
            self._saldo -= cantidad
            self._movimientos.append({"Tipo": "Retiro", "Cantidad": -cantidad})
            print(f"Has retirado {cantidad} euros.")

    def mostrar_saldo(self):
        """
        Docstring for mostrar_saldo: Muestra el saldo restante
        
        :param self: Apunta al propio objeto
        """
        print(f"Saldo actual: {self._saldo} euros")
    
    def mostrar_movimientos(self):
        """
        Docstring for mostrar_movimientos: Muestra todos los movimientos de la cuenta
        
        :param self: Apunta al propio objeto
        """
        print("Historial de movimientos:")
        for movimiento in self._movimientos:
            print(movimiento)
    
    def __str__(self):
        return f"Nombre: {self._nombre}, Saldo: {self._saldo}"

